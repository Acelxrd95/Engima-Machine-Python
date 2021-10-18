from datastructs.array_struct import Array

"""
The Enigma M3 cipher consists of a few parameters

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


class Rotor:
    def __init__(self, tyre: str, notch: str | tuple[str, ...]) -> None:
        assert 27 == len(tyre), "Rotor Tyre must be equal to Alphabets entered"
        self.tyre = Array(str, values=tyre)
        self.notch = Array(str, values=notch)
        self.curr_pos = 0
        self.ring_offset = 0

    def __repr__(self):
        pass


class Enigma:
    def __init__(
        self,
        settings: tuple[str, str, str] = ("A", "A", "A"),
        rotors: tuple[int, int, int] = (1, 2, 3),
        reflector: str = "B",
        ringstellung: tuple[str, str, str] = ("A", "A", "A"),
        steckers: list[tuple[str, str]] = [],
    ) -> None:
        self.settings = settings
        self.rotors = rotors
        self.selec_reflector = reflector
        self.ringstellung = ringstellung
        self.steckers = steckers
        self.rotorkeys = [
            Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
            Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
            Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
            Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
            Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
            Rotor("JPGVOUMFYQBENHZRDKASXLICTW", ("Z", "M")),
            Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT", ("Z", "M")),
            Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", ("Z", "M")),
        ]
        self.reflectorkeys = [
            "EJMZALYXVBWFCRQUONTSPIKHGD",
            "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            "FVPJIAOYEDRZXWGCTKUQSBNMHL",
        ]
        self.initsettings = [
            settings,
            rotors,
            reflector,
            ringstellung,
            steckers,
            self.rotorkeys,
            self.reflectorkeys,
        ]

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
        docstring
        """
        raise NotImplementedError

    def advanceRotor(self) -> None:
        """
        Advances the rotors acording to the notch and their positions
        """
        # if self.settings[1] in self.rotorkeys[self.rotors[1]]:
        raise NotImplementedError

    def substr(self, string: str) -> str:

        return ""

    def applySteckers(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def index2alpha(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def alpha2index(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def encipherChar(self, char: str) -> str:
        """
        docstring
        """
        self.advanceRotor()
        raise NotImplementedError

    def encipher(self, string: str) -> str:
        """
        docstring
        """
        retstr = ""
        for char in string.upper():
            if char.isalpha():
                retstr += self.encipherChar(char)
            else:
                retstr += char
        return retstr

    def decipher(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError
