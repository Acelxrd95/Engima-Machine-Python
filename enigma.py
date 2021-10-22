from datastructs.array_struct import Array
from utils import *
import f


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


class Enigma:
    def __init__(
        self,
        settings: tuple[str, str, str] = ("A", "A", "A"),
        rotors: tuple[int, int, int] | tuple[str, str, str] = ("I", "II", "III"),
        reflector: str = "B",
        ringstellung: tuple[str, str, str] = ("A", "A", "A"),
        steckers: list[tuple[str, str]] = [],
    ) -> None:
        self.settings = settings
        temp_rot = []
        for rot in rotors:
            if type(rot) is str:
                temp_rot.append(str(roman2den(rot)))
            else:
                temp_rot.append(str(rot))
        self.rotors = tuple(temp_rot)
        self.selec_reflector = reflector
        self.ringstellung = ringstellung
        self.steckers = steckers
        self.rotorkeys = {
            "1": Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
            "2": Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
            "3": Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
            "4": Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
            "5": Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
            "6": Rotor("JPGVOUMFYQBENHZRDKASXLICTW", ("Z", "M")),
            "7": Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT", ("Z", "M")),
            "8": Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", ("Z", "M")),
        }
        self.invrotors = {
            "1": "UWYGADFPVZBECKMTHXSLRINQOJ",  # inverse rotor keys
            "2": "AJPCZWRLFBDKOTYUQGENHXMIVS",
            "3": "TAGBPCSDQEUFVNZHYIXJWLRKOM",
            "4": "HZWVARTNLGUPXQCEJMBSKDYOIF",
            "5": "QCYLXWENFTZOSMVJUDKGIARPHB",
            "6": "SKXQLHCNWARVGMEBJPTYFDZUIO",
            "7": "QMGYVPEDRCWTIANUXFKZOSLHJB",
            "8": "QJINSAYDVKBFRUHMCPLEWZTGXO",
        }
        self.reflectorkeys = {
            "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
            "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
        }
        self.initsettings = [
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

    def encipherChar(self, char: str) -> str:
        """
        docstring
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
        docstring
        """
        retstr = ""
        for char in string.upper():
            if char.isalpha():
                retstr += self.encipherChar(char)
            else:
                retstr += char
        return retstr

    def decipher(self, string):
        """
        docstring
        """
        raise NotImplementedError


"""
The Enigma rotors consist of a couple of settings and properties

:param tyre: refers to the alphabet tyre used to encrypt the letter entered

:param notch: refers to the notch at which the next rotor in order turns

:prop curr_pos: refers to the current position of the rotor

:prop ring_offset: refers to the offset of the ring wiring

:prop abs_pos: refers to the original absolute position of the rotor without the offset

:prop check_notch: checks whether the rotor is currently on the notch or not
"""


class Rotor:
    def __init__(self, tyre: str, notch: str | tuple[str, ...]) -> None:
        assert 26 == len(tyre), "Rotor Tyre must be equal to Alphabets entered"
        self.tyre = Array(str, values=tyre)
        self.notch = Array(str, values=notch)
        self.curr_pos = 0
        self.ring_offset = 0

    @property
    def abs_pos(self):
        return self.curr_pos - self.ring_offset

    @property
    def check_notch(self) -> bool:
        if n2c(self.curr_pos) in self.notch:
            return True
        else:
            return False

    def __repr__(self) -> str:
        x = {
            "tyre": str(self.tyre),
            "notch": str(self.notch),
            "curr_pos": self.curr_pos,
            "ring_offset": self.ring_offset,
            "abs_pos": self.abs_pos,
        }
        return f"{x}"

    def reset(self):
        """Reset the rotor"""
        self.shiftPosition(self.abs_pos)
        pass

    def changeRingsett(self, pos: int) -> None:
        """
        docstring
        """
        if self.ring_offset != 0:
            self.shiftPosition(self.ring_offset)
        self.shiftPosition(pos, -1)
        self.ring_offset = pos

    def shiftPosition(self, pos: int, dirct: int = 1) -> None:
        self.tyre.shift(pos, dirct)
        if dirct == 1:
            self.curr_pos += pos * dirct
        if self.abs_pos == 26:
            self.curr_pos = self.ring_offset


if __name__ == "__main__":
    x = Enigma(
        settings=("A", "A", "A"),
        rotors=(1, 2, 3),
        reflector="B",
        ringstellung=("A", "A", "A"),
        steckers=[],
    )
    for i in range(3):
        rotid = x.rotors[i]
        currot = x.rotorkeys[rotid]
        print(currot)
    print(x.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    print("================================================================")
    y = f.Enigma(
        settings=("A", "A", "A"),
        rotors=(1, 2, 3),
        reflector="B",
        ringstellung=("A", "A", "A"),
        steckers=[],
    )
    print(y.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    for i in range(3):
        rotid = x.rotors[i]
        currot = x.rotorkeys[rotid]
        print(currot)
    print("================================================================")
