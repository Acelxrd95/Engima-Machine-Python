from typing import Union
from Enigma.utils import n2c
from Enigma.datastructs import Array


class Rotor:
    """
    The Enigma rotors consist of a couple of settings and properties.

        Attributes:
            tyre (str): refers to the alphabet tyre used to encrypt the letter entered.
            notch (Union[str, tuple[str, ...]]): refers to the notch at which the next rotor in order turns.
            curr_pos (int): refers to the current position of the rotor.
            ring_offset (int): refers to the offset of the ring wiring.
            abs_pos (int): refers to the original absolute position of the rotor without the offset.
            check_notch (bool): checks whether the rotor is currently on the notch or not.
    """

    def __init__(self, tyre: str, notch: Union[str, tuple[str, ...]]) -> None:
        if 26 != len(tyre):
            print("Rotor Tyre must be equal to Alphabets entered")
        self.tyre = Array(str, values=tyre)
        self.notch = Array(str, values=notch)
        self.curr_pos = 0
        self.ring_offset = 0

    @property
    def abs_pos(self) -> int:
        return self.curr_pos - self.ring_offset

    @property
    def check_notch(self) -> bool:
        if n2c(self.curr_pos) in self.notch:
            return True
        else:
            return False

    def __repr__(self) -> str:
        """
        Returns the object's string representation.
        """
        x = {
            "tyre": str(self.tyre),
            "notch": str(self.notch),
            "curr_pos": self.curr_pos,
            "ring_offset": self.ring_offset,
            "abs_pos": self.abs_pos,
        }
        return f"{x}"

    def reset(self):
        """
        Reset the rotor to its initial position.
        """
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
        Shift the rotor position according `pos` for number of steps and the `dirct` for
        the direction of the shift
        """
        self.tyre.shift(pos, dirct)
        if dirct == 1:
            self.curr_pos += pos * dirct
        if self.abs_pos == 26:
            self.curr_pos = self.ring_offset
