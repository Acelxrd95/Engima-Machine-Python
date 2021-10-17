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


class Enigma:
    def __init__(
        self,
        settings: tuple[str, str, str] = ("A", "A", "A"),
        rotors: tuple[int, int, int] = (1, 2, 3),
        reflector: str = "B",
        ringstellung: tuple[str, str, str] = ("A", "A", "A"),
        steckers: list[tuple[str, str]] = [],
    ) -> None:
        self.initsettings = [settings, rotors, reflector, ringstellung, steckers]
        self.settings = settings
        self.rotors = rotors
        self.selec_reflector = reflector
        self.ringstellung = ringstellung
        self.steckers = steckers
        self.rotorkeys = [
            ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
            ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
            ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
            ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
            ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
            ("JPGVOUMFYQBENHZRDKASXLICTW", ("Z", "M")),
            ("NZJHGRCXMYSWBOUFAIVLPEKQDT", ("Z", "M")),
            ("FKQHTLXOCBJSPDZRAMEWNIUYGV", ("Z", "M")),
        ]
        self.reflectorkeys = [
            "EJMZALYXVBWFCRQUONTSPIKHGD",
            "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            "FVPJIAOYEDRZXWGCTKUQSBNMHL",
        ]

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def resetSettings(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def applySettings(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def advanceRotor(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

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

    def encipherChar(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def encipher(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError

    def decipher(self, parameter_list):
        """
        docstring
        """
        raise NotImplementedError
