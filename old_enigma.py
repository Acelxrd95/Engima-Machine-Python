from datastructs.array_struct import Array

# ---------------------------------- Classes --------------------------------- #
class Rotor:
    def __init__(
        self, wiring: str, notch: str, alphabet_tyre: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ) -> None:
        assert len(alphabet_tyre) == len(
            wiring
        ), "Wiring must be equal to Alphabets entered"

        self.alphabet_tyre = Array(str, values=alphabet_tyre)
        self.wiring = Array(str, values=wiring)
        self.notch = notch
        self.curr_pos = 0
        self.ring_offset = 0

    @property
    def checkrot(self) -> bool:
        if self.alphabet_tyre[-1] == self.notch:
            return True
        else:
            return False

    @property
    def rot_pos(self):
        return self.curr_pos - self.ring_offset

    def __repr__(self) -> str:
        return f"Wiring:\n{self.alphabet_tyre}\n{self.wiring}\nNotch: {self.notch}\nPositions:\nCurrent:{self.curr_pos}\tRing offset:{self.ring_offset}\tRotor:{self.rot_pos}"

    def __iter__(self) -> None:
        pass

    def setpos(self, pos: int | str, setring: bool = False) -> None:
        if setring:
            dirct = -1
        else:
            dirct = 1
        if type(pos) is int:
            self.alphabet_tyre.shift(pos, dirct)
            self.curr_pos += pos * dirct
            if setring:
                self.ring_offset = dirct * pos
        elif type(pos) is str:
            index = self.alphabet_tyre.index(pos)
            if type(index) is int:
                if setring:
                    self.ring_offset = dirct * index
                self.alphabet_tyre.shift(index, dirct)
                self.curr_pos += index * dirct
            else:
                raise KeyError(index)
        if self.rot_pos == 26:
            self.curr_pos = self.ring_offset

    def reset(self):
        self.setpos(self.curr_pos, True)

    def encrypt(
        self, data: str, reverse: bool = False, step: bool = False
    ) -> tuple[str, bool]:
        if reverse:
            data_pos = self.wiring.index(data)
            rtdata = self.alphabet_tyre[data_pos]
        else:
            data_pos = self.alphabet_tyre.index(data)
            rtdata = self.wiring[data_pos]
        if step:
            self.setpos(1, False)

        return (f"{rtdata}", self.checkrot)


class Steckers:
    def __init__(self) -> None:
        pass


class Reflector:
    def __init__(
        self, wiring: str, alphabet_tyre: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ) -> None:
        self.wiring = wiring
        self.alphabet_tyre = alphabet_tyre

    def encrypt(self, data: str) -> str:
        data_pos = self.alphabet_tyre.index(data)
        rtdata = self.wiring[data_pos]
        return rtdata


class Enigma:
    # T1 = tuple[str, str, str]
    # T1 = tuple[str | int, str | int, str | int]

    def __init__(
        self,
        settings: tuple[str, str, str] = ("A", "A", "A"),
        rotors: tuple[int, int, int] = (1, 2, 3),
        reflector: str = "B",
        ringstellung: tuple[str, str, str] = ("A", "A", "A"),
        steckers: list[tuple[str, str]] = [],
    ) -> None:
        self.settings = settings
        self.rotors = tuple([q - 1 for q in rotors])
        self.ringstellung = ringstellung
        self.steckers = steckers
        self.reflector = reflector
        self.reflector_storage = {
            "A": Reflector("EJMZALYXVBWFCRQUONTSPIKHGD"),
            "B": Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT"),
            "C": Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL"),
        }
        self.rotor_storage = [
            Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
            Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
            Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
            Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
            Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z"),
        ]
        self.apply_settings()

    def apply_settings(self):
        for i in range(3):
            rotid = self.rotors[i]
            currot = self.rotor_storage[rotid]
            currot.setpos(self.settings[i])
            currot.setpos(self.ringstellung[i], True)

    def encipher(self, string: str) -> str:
        rtstring = ""
        for char in string:
            tmpchar, chtrn = self.rotor_storage[self.rotors[0]].encrypt(
                char, False, True
            )
            tmpchar, chtrn = self.rotor_storage[self.rotors[1]].encrypt(
                tmpchar, False, chtrn
            )
            tmpchar, _ = self.rotor_storage[self.rotors[2]].encrypt(
                tmpchar, False, chtrn
            )
            # -------------------------------- Reflector ------------------------------- #
            tmpchar = self.reflector_storage[self.reflector].encrypt(tmpchar)
            # ---------------------------- Backwards encrypt --------------------------- #
            tmpchar, _ = self.rotor_storage[self.rotors[2]].encrypt(tmpchar, True)
            tmpchar, _ = self.rotor_storage[self.rotors[1]].encrypt(tmpchar, True)
            tmpchar, _ = self.rotor_storage[self.rotors[0]].encrypt(tmpchar, True)
            rtstring += tmpchar
        return f"{rtstring}"

    def decypher(self, string: str) -> str:
        return ""


# ----------------------------------- Code ----------------------------------- #

if __name__ == "__main__":
    # r1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
    # r2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
    # r3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    # r4 = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
    # r5 = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
    mach1 = Enigma(
        settings=("A", "A", "A"),
        rotors=(1, 2, 3),
        reflector="B",
        ringstellung=("A", "A", "A"),
        steckers=[
            ("P", "O"),
            ("M", "L"),
            ("I", "U"),
            ("K", "J"),
            ("N", "H"),
            ("Y", "T"),
            ("G", "B"),
            ("V", "F"),
            ("R", "E"),
            ("D", "C"),
        ],
    )
    x = mach1.encipher("A")
    print(x)
    print(mach1.rotor_storage[0])
    print(mach1.rotor_storage[1])
    print(mach1.rotor_storage[2])
    pass
