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
"""

Tup3Str = tuple[str, str, str] | list[str]
Tup3Int = tuple[int, int, int] | list[int]
LiTup2Str = list[tuple[str, str]]


class Enigma:
    def __init__(
        self,
        settings: Tup3Str = ("A", "A", "A"),
        rotors: Tup3Int | Tup3Str = ("I", "II", "III"),
        reflector: str = "B",
        ringstellung: Tup3Str = ("A", "A", "A"),
        steckers: LiTup2Str = None,
    ) -> None:

        self.settings: Tup3Str = settings  # TODO could be array

        temp_rot = []
        for rot in rotors:
            rot = str(rot)
            if isroman(rot):
                temp_rot.append(str(roman2den(rot)))
            else:
                temp_rot.append(rot)

        self.rotors: tuple = tuple(temp_rot)  # TODO could be array

        self.selec_reflector: str = reflector

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
        self.rotorkeys = []  # TODO could be array
        for i in self.rotors:
            rotkey = self.rotorkeys_store[i]["key"]
            rotnotch = self.rotorkeys_store[i]["notch"]
            self.rotorkeys.append(self.spawnRotorInstances(rotkey, rotnotch))

        self.reflectorkeys = {  # TODO could be map
            "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
            "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
        }

        self.initsettings = [  # TODO could be Array
            settings,
            tuple(temp_rot),
            reflector,
            ringstellung,
            steckers,
            self.rotorkeys_store,
            self.reflectorkeys,
        ]

        self.applySettings()

    def resetSettings(self) -> None:
        """
        Resets the settings for the enigma machine to the settings it was initialized with
        """
        iniset = self.initsettings
        self.__init__(iniset[0], iniset[1], iniset[2], iniset[3], iniset[4])
        self.rotorkeys_store = iniset[5]
        self.reflectorkeys = iniset[6]

    def applySettings(self, reset=False) -> None:
        """
        Applies the settings to the individual components of the enigma
        """
        for i in range(3):
            currot = self.rotorkeys[i]
            if reset:
                currot.shiftPosition(c2n(self.settings[i]), -1)
            else:
                currot.shiftPosition(c2n(self.settings[i]))
            currot.changeRingsett(c2n(self.ringstellung[i]))
        # self.applySteckers()

    def spawnRotorInstances(self, key: str, notch: tuple) -> Rotor:
        return Rotor(key, notch)

    def advanceRotor(self) -> None:
        """
        Advances the rotors acording to the notch and their positions
        """
        if self.rotorkeys[1].check_notch:
            self.rotorkeys[1].shiftPosition(1)
            self.rotorkeys[0].shiftPosition(1)

        if self.rotorkeys[2].check_notch:
            self.rotorkeys[1].shiftPosition(1)

        self.rotorkeys[2].shiftPosition(1)

    def applySteckers(self):
        """
        docstring
        """
        raise NotImplementedError

    def encryptChar(self, char: str) -> str:
        """
        Loops the character on the selected rotors for encryption.
        Goes forward starting with the rightmost rotor then reflects the character on the selected reflector and then goes across the rotors in the reverse order starting with the leftmost rotor and then returns the result
        """
        self.advanceRotor()
        eChar: int = c2n(char)
        # NOTE forward encipher
        for i in range(2, -1, -1):
            convChar = c2n(str(self.rotorkeys[i].tyre[eChar]))
            offset = self.rotorkeys[i].abs_pos
            eChar = (convChar - offset) % 26
            # print(n2c(eChar), self.rotorkeys[self.rotors[i]].abs_pos) DEV debuging character encoding
        # NOTE reflector encipher
        eChar = c2n(self.reflectorkeys[self.selec_reflector][eChar])
        # print(n2c(eChar)) DEV debuging character encoding

        # NOTE backward encipher
        for i in range(3):
            if eChar == 23:
                pass
            offset = self.rotorkeys[i].abs_pos
            eChar = int(self.rotorkeys[i].tyre.index(n2c(eChar + offset)))
            # print(n2c(eChar), eChar % 26, self.rotorkeys[self.rotors[i]].abs_pos) DEV debuging character encoding
        # print(repr(self)) DEV debuging character encoding
        # print("===========") DEV debuging character encoding
        return n2c(eChar)

    def encipher(self, string: str, decipher=False) -> str:
        """
        Loops on the string and sends each character to the encryptChar function to be encrypted
        calls the sp2norm function if the character is a special character or num2word if the
        character is a number or small2cap if the character is not a capital letter before sending
        it to the encryptChar function
        """
        string = string.replace(" ", "")
        normalized_str = ""
        retstr = ""
        if not decipher:
            for char in string:
                normalized_str += transformsp(char)
        else:
            normalized_str = string
        for char in normalized_str:
            retstr += self.encryptChar(char)
        return retstr

    def decipher(self, string: str) -> str:
        """
        Calls the encipher function to decipherthe string
        """
        return rmspecial(self.encipher(string, True))


if __name__ == "__main__":
    x = Enigma(
        settings=("A", "A", "B"),
        rotors=(1, 2, 3),
        reflector="B",
        ringstellung=("A", "A", "B"),
        steckers=[],
    )
    print(x.encipher("Ahmed"))
    x.resetSettings()
    print(x.decipher("SSZKHNF"))
