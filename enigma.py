from datastructs.array_struct import Array
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

Tup3Str = tuple[str, str, str]
Tup3Int = tuple[int, int, int]
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
            if type(rot) is str:
                temp_rot.append(str(roman2den(rot)))
            else:
                temp_rot.append(str(rot))
        self.rotors: tuple = tuple(temp_rot)  # TODO could be array
        self.selec_reflector: str = reflector
        self.ringstellung: Tup3Str = ringstellung  # TODO could be array
        if steckers == None:
            steckers = []
        self.steckers: LiTup2Str = steckers  # TODO could be array
        self.rotorkeys = {  # TODO could be map
            "1": Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
            "2": Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
            "3": Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
            "4": Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
            "5": Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
            "6": Rotor("JPGVOUMFYQBENHZRDKASXLICTW", ("Z", "M")),
            "7": Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT", ("Z", "M")),
            "8": Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", ("Z", "M")),
        }
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
            self.rotorkeys,
            self.reflectorkeys,
        ]
        self.applySettings()

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def resetSettings(self) -> None:
        """
        Resets the settings for the enigma machine to the settings it was initialized with
        """
        self.settings = self.initsettings[0]
        self.rotors = self.initsettings[1]
        self.selec_reflector = self.initsettings[2]
        self.ringstellung = self.initsettings[3]
        self.steckers = self.initsettings[4]
        self.rotorkeys = self.initsettings[5]
        self.reflectorkeys = self.initsettings[6]
        self.applySettings()

    def applySettings(self) -> None:
        """
        Applies the settings to the individual components of the enigma
        """
        for i in range(3):
            rotid = self.rotors[i]
            currot = self.rotorkeys[rotid]
            currot.shiftPosition(c2n(self.settings[i]))
            currot.changeRingsett(c2n(self.ringstellung[i]))
        # self.applySteckers()

    def advanceRotor(self) -> None:
        """
        Advances the rotors acording to the notch and their positions
        """
        if self.rotorkeys[self.rotors[1]].check_notch:
            self.rotorkeys[self.rotors[1]].shiftPosition(1)
            self.rotorkeys[self.rotors[0]].shiftPosition(1)

        if self.rotorkeys[self.rotors[2]].check_notch:
            self.rotorkeys[self.rotors[1]].shiftPosition(1)

        self.rotorkeys[self.rotors[2]].shiftPosition(1)

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
        # forward encipher
        for i in range(2, -1, -1):
            eChar = (
                c2n(str(self.rotorkeys[self.rotors[i]].tyre[eChar]))
                - self.rotorkeys[self.rotors[i]].curr_pos
            )
            print(n2c(eChar))
        # reflector encipher
        eChar = c2n(self.reflectorkeys[self.selec_reflector][eChar])
        print(n2c(eChar))

        # backward encipher
        for i in range(3):
            eChar = int(
                self.rotorkeys[self.rotors[i]].tyre.index(
                    n2c(eChar + self.rotorkeys[self.rotors[i]].curr_pos)
                )
            )
            print(n2c(eChar))
        return n2c(eChar)

    def encipher(self, string: str) -> str:
        """
        Loops on the string and sends each character to the encryptChar function to be encrypted
        calls the sp2norm function if the character is a special character or num2word if the
        character is a number or small2cap if the character is not a capital letter before sending
        it to the encryptChar function
        """
        retstr = ""
        for char in string.upper():
            if char.isalpha():
                retstr += self.encryptChar(char)
            else:
                retstr += char
        return retstr

    def decipher(self, string: str) -> str:
        """
        Calls the encipher function to decipherthe string
        """
        return self.encipher(string)


if __name__ == "__main__":
    x = Enigma(
        settings=("A", "A", "A"),
        rotors=(1, 2, 3),
        reflector="B",
        ringstellung=("A", "A", "A"),
        steckers=[],
    )
