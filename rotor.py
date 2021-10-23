from datastructs.array_struct import Array
from utils import *

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
        self.invtyre = self.invertRotorTyre()
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
        Changes the ring offset setting
        """
        if self.ring_offset != 0:
            self.shiftPosition(self.ring_offset)
        self.shiftPosition(pos, -1)
        self.ring_offset = pos

    def shiftPosition(self, pos: int, dirct: int = 1) -> None:
        """
        Shift the rotor position according :param pos for number of steps and the :param dirct for
        the direction of the shift
        """
        self.tyre.shift(pos, dirct)
        if dirct == 1:
            self.curr_pos += pos * dirct
        if self.abs_pos == 26:
            self.curr_pos = self.ring_offset

    def invertRotorTyre(self) -> Array:
        invrt = Array(str, self.tyre.size)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for char in alphabet:
            invr_char = alphabet[int(self.tyre.index(char))]
            invrt.insert(invr_char)
        return invrt


if __name__ == "__main__":
    x = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "Q")
    print(x.tyre)
    print(x.invtyre)

"""
BDFHJLCPRTXVZNYEIWGAKMUSQO
ABCDEFGHIJKLMNOPQRSTUVWXYZ
TAGBPCSDQEUFVNZHYIXJWLRKOM
"""
