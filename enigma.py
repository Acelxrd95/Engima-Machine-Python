from utils import *
from rotor import Rotor


"""
The Enigma cipher consists of a few parameters

:param settings: refers to the rotors start positions, which 
consists of 3 characters ex:('F','G','B')

:param rotors: specifies the rotors used and their order. There 
are 8 possible rotors labeled from 1 through 8. More rotors can be 
added using the addCustRotor method

:param reflector: specifies the reflector used More can be 
specified using the addCustReflect method

:param ringstellung: refers to the ring settings and consists of 3 
characters ex:('F','G','B')

:param steckers: specifies the plugboard settings, indicating 
which characters are mapped to eachother. Consists of max 10 
tuples of 2-tuples

:param enc_nums: specifies whether numbers should be ignored (0), encrypted (1) or removed (2)

:param enc_capitals:specifies whether capitals should be ignored (0), encrypted (1)

:param enc_special:specifies whether special characters should be ignored (0), encrypted (1) or removed (2)

:param enc_whitesp:specifies whether spaces should be ignored (0), encrypted (1) or removed (2)
"""

Tup3Str = tuple[str, str, str] | list[str]
Tup3Int = tuple[int, int, int] | list[int]
LiTup2Str = list[tuple[str, str]]

"""
settings to add
7- rotor size bigger than 26
8- reflector into rotor
"""


class Enigma:
    def __init__(
        self,
        settings: Tup3Str = ("A", "A", "A"),
        rotors: Tup3Int | Tup3Str = ("I", "II", "III"),
        reflector: str = "B",
        ringstellung: Tup3Str = ("A", "A", "A"),
        steckers: LiTup2Str = None,
        enc_nums: int = 0,
        enc_capitals: int = 0,
        enc_special: int = 0,
        enc_whitesp: int = 0,
        # reflect2rotor: bool = False,
    ) -> None:

        self.settings: Tup3Str = settings  # TODO could be array

        self.setReflector(reflector)

        self.ringstellung: Tup3Str = ringstellung  # TODO could be array

        if steckers == None:
            steckers = []
        self.steckers: LiTup2Str = steckers  # TODO could be array

        self.rotorkeys_store = {  # TODO could be map
            "1": {"key": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "notch": "Q"},
            "2": {"key": "AJDKSIRUXBLHWTMCQGZNPYFVOE", "notch": "E"},
            "3": {"key": "BDFHJLCPRTXVZNYEIWGAKMUSQO", "notch": "V"},
            "4": {"key": "ESOVPZJAYQUIRHXLNFTGKDCMWB", "notch": "J"},
            "5": {"key": "VZBRGITYUPSDNHLXAWMJQOFECK", "notch": "Z"},
            "6": {"key": "JPGVOUMFYQBENHZRDKASXLICTW", "notch": ("Z", "M")},
            "7": {"key": "NZJHGRCXMYSWBOUFAIVLPEKQDT", "notch": ("Z", "M")},
            "8": {"key": "FKQHTLXOCBJSPDZRAMEWNIUYGV", "notch": ("Z", "M")},
        }
        self.setRotor(*rotors)  # TODO could be array

        self.reflectorkeys_store = {  # TODO could be map
            "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
            "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
        }

        self.initsettings = [  # TODO could be Array
            settings,
            rotors,
            reflector,
            ringstellung,
            steckers,
            self.rotorkeys_store,
            self.reflectorkeys_store,
        ]
        self.enc_settings = [enc_nums, enc_capitals, enc_special, enc_whitesp]
        self.applySettings()

    def resetSettings(self, maintain_storage: bool = True) -> None:
        """
        Resets the settings for the enigma machine to the settings it was initialized with
        """
        iniset = self.initsettings
        self.__init__(iniset[0], iniset[1], iniset[2], iniset[3], iniset[4])
        if maintain_storage:
            self.rotorkeys_store = iniset[5]
            self.reflectorkeys_store = iniset[6]

    def applySettings(self, reset=False) -> None:
        """
        Applies the settings to the individual components of the enigma
        """
        for i in range(3):
            currot = self.rotors[i]
            if reset:
                currot.shiftPosition(c2n(self.settings[i]), -1)
            else:
                currot.shiftPosition(c2n(self.settings[i]))
            currot.changeRingsett(c2n(self.ringstellung[i]))

    def changeEncSettings(
        self,
        enc_nums: int = None,
        enc_capitals: int = None,
        enc_special: int = None,
        enc_whitesp: int = None,
    ):
        if enc_nums is not None:
            self.enc_settings[0] = enc_nums
        if enc_capitals is not None:
            self.enc_settings[1] = enc_capitals
        if enc_special is not None:
            self.enc_settings[2] = enc_special
        if enc_whitesp is not None:
            self.enc_settings[3] = enc_whitesp
        pass

    def spawnRotorInstances(self, key: str, notch: tuple) -> Rotor:
        return Rotor(key, notch)

    def setRotor(self, r1: int | str, r2: int | str, r3: int | str) -> None:
        """
        Initializes the rotor instance
        """
        temp_rot = []
        rotors = (r1, r2, r3)
        for rot in rotors:
            rot = str(rot)
            if isroman(rot):
                temp_rot.append(str(roman2den(rot)))
            else:
                temp_rot.append(rot)
        temp_rot = tuple(temp_rot)
        self.rotors = []  # TODO could be array
        for i in temp_rot:
            rotkey = self.rotorkeys_store[i]["key"]
            rotnotch = self.rotorkeys_store[i]["notch"]
            self.rotors.append(self.spawnRotorInstances(rotkey, rotnotch))

    def setReflector(self, reflectr: str) -> None:
        """
        Setter for the reflector
        """
        self.reflector = reflectr

    def addCustomRotor(
        self, rotor_id: str, key: str, notch: tuple, allowdupes=False
    ) -> None:
        """
        Allows the user to add custom rotors with custom keys and notches
        """
        if isroman(rotor_id):
            rotor_id = str(roman2den(rotor_id))
        if rotor_id in self.rotorkeys_store:
            raise Exception(f"A rotor with the ID {rotor_id} already exists")
        if len(key) != 26:
            raise Exception("Rotor keys must be 26 characters long")
        if not allowdupes:
            tmpkey = []
            for k in key:
                if k in tmpkey:
                    raise Exception(
                        f"There letter {k} was found as dupelicatein the key provided"
                    )
                else:
                    tmpkey.append(k)
        if len(notch) < 1:
            raise Exception("There must be at least one Notch key")
        for n in notch:
            if n not in key:
                raise Exception(
                    f"The provided notch {notch} does not exist in the specified key {key}"
                )
        self.rotorkeys_store.update({rotor_id: {"key": key, "notch": notch}})

    def addCustomReflector(self, reflector_id: str, key: str, allowdupes=False) -> None:
        """
        Allows the user to add custom reflectors with custom keys
        """
        if isroman(reflector_id):
            reflector_id = str(roman2den(reflector_id))
        if reflector_id in self.reflectorkeys_store:
            raise Exception(f"A reflector with the ID {reflector_id} already exists")
        if len(key) != 26:
            raise Exception("Reflector keys must be 26 characters long")
        if not allowdupes:
            tmpkey = []
            for k in key:
                if k in tmpkey:
                    raise Exception(
                        f"There letter {k} was found as dupelicatein the key provided"
                    )
                else:
                    tmpkey.append(k)
        self.reflectorkeys_store.update({reflector_id: key})

    def advanceRotor(self) -> None:
        """
        Advances the rotors acording to the notch and their positions
        """
        if self.rotors[1].check_notch:
            self.rotors[1].shiftPosition(1)
            self.rotors[0].shiftPosition(1)

        if self.rotors[2].check_notch:
            self.rotors[1].shiftPosition(1)

        self.rotors[2].shiftPosition(1)

    def applySteckers(self, char: str) -> str:
        """
        Converts the letters according to the plugboard specification
        """
        for l1, l2 in self.steckers:
            if char == l1:
                char = l2
            elif char == l2:
                char = l1
        return char

    def encryptChar(self, char: str) -> str:
        """
        Loops the character on the selected rotors for encryption.
        Goes forward starting with the rightmost rotor then reflects the character on the selected reflector and then goes across the rotors in the reverse order starting with the leftmost rotor and then returns the result
        """
        self.advanceRotor()
        char = self.applySteckers(char)
        eChar: int = c2n(char)
        # NOTE forward encipher
        for i in range(2, -1, -1):
            convChar = c2n(str(self.rotors[i].tyre[eChar]))
            offset = self.rotors[i].abs_pos
            eChar = (convChar - offset) % 26
            # print(n2c(eChar), self.rotors[self.rotors[i]].abs_pos) DEV debuging character encoding
        # NOTE reflector encipher
        eChar = c2n(self.reflectorkeys_store[self.reflector][eChar])
        # print(n2c(eChar)) DEV debuging character encoding

        # NOTE backward encipher
        for i in range(3):
            if eChar == 23:
                pass
            offset = self.rotors[i].abs_pos
            eChar = int(self.rotors[i].tyre.index(n2c(eChar + offset)))
            # print(n2c(eChar), eChar % 26, self.rotors[self.rotors[i]].abs_pos) DEV debuging character encoding
        # print(repr(self)) DEV debuging character encoding
        # print("===========") DEV debuging character encoding
        char = n2c(eChar)
        char = self.applySteckers(char)
        return char

    def encipher(self, string: str, decipher=False) -> str:
        """
        Loops on the string and sends each character to the encryptChar function to be encrypted
        calls the sp2norm function if the character is a special character or num2word if the
        character is a number or small2cap if the character is not a capital letter before sending
        it to the encryptChar function
        """
        normalized_str = ""
        retstr = ""
        if not decipher:
            for char in string:
                normalized_str += transformsp(char, self.enc_settings)
        elif self.enc_settings == [0, 0, 0, 0]:
            normalized_str = string
        else:
            normalized_str = string
        for char in normalized_str:
            if self.enc_settings == [0, 0, 0, 0] and not char.isalpha():
                retstr += char
            else:
                char = char.upper()
                retstr += self.encryptChar(char)
        return retstr

    def decipher(self, string: str) -> str:
        """
        Calls the encipher function to decipherthe string
        """
        return rmspecial(self.encipher(string, True))


if __name__ == "__main__":
    enigma = Enigma(
        settings=("A", "F", "A"),
        rotors=(1, 2, 3),
        reflector="B",
        ringstellung=("A", "B", "A"),
        steckers=[],
        enc_nums=2,
        enc_capitals=1,
        enc_special=2,
        enc_whitesp=2,
    )
    x = enigma.encipher("Hello World 15 [")
    print(x)
    enigma.resetSettings()
    print(enigma.decipher(x))
