from typing import Literal, MutableSequence, Union
from utils import *
from rotor import Rotor
import storage
from datastructs.array_struct import Array


class Enigma:
    """
    The main Enigma machine class

    :param start_pos: refers to the rotors start positions, which consists of 3 characters ex:('F','G','B')
    :param rotors: specifies the rotors used and their order. There are 8 possible rotors labeled from 1 through 8. More rotors can be added using the `addCustRotor` method
    :param reflector: specifies the reflector used More can be specified using the `addCustReflect` method
    :param ring_setting: refers to the ring settings and consists of 3 characters ex:('F','G','B')
    :param plugboard: specifies the plugboard settings, indicating which characters are mapped to eachother. Consists of max 10 tuples of 2-tuples
    :param enc_nums: specifies whether numbers should be ignored (0), encrypted (1) or removed (2)
    :param enc_capitals:specifies whether capitals should be ignored (0), encrypted (1)
    :param enc_special:specifies whether special characters should be ignored (0), encrypted (1) or removed (2)
    :param enc_whitesp:specifies whether spaces should be ignored (0), encrypted (1) or removed (2)
    """

    def __init__(
        self,
        start_pos: Union[tuple[str, str, str], list[str]] = ("A", "A", "A"),
        rotors: Union[
            tuple[int, int, int], list[int], tuple[str, str, str], list[str]
        ] = ("I", "II", "III"),
        reflector: str = "B",
        ring_setting: Union[tuple[str, str, str], list[str]] = ("A", "A", "A"),
        plugboard: list[tuple[str, str]] = None,
        enc_nums: int = 0,
        enc_capitals: int = 0,
        enc_special: int = 0,
        enc_whitesp: int = 0,
        duperot_instance: bool = False,
    ) -> None:
        self.setDupeRot(duperot_instance)
        self.startposCheck(start_pos)

        self.ringsetCheck(ring_setting)

        self.encsettingCheck(enc_nums, enc_capitals, enc_special, enc_whitesp)

        self.start_pos: Array = Array(str, values=start_pos)
        self.setReflector(reflector)
        self.ring_setting: Array = Array(str, values=ring_setting)
        self.plugboard: Array = Array(tuple, 10)
        if plugboard != None:
            self.plugboardCheck(plugboard)
            x = []
            for c1, c2 in plugboard:
                if c1 in x or c2 in x or c1 == c2:
                    continue
                x.append(c1)
                x.append(c2)
                try:
                    self.plugboard.insert((c1, c2))
                except:
                    break
        self.setRotor(*rotors)
        self.enc_settings = Array(
            int, values=[enc_nums, enc_capitals, enc_special, enc_whitesp]
        )
        self.initsettings = [
            start_pos,
            rotors,
            reflector,
            ring_setting,
            plugboard,
            enc_nums,
            enc_capitals,
            enc_special,
            enc_whitesp,
            duperot_instance,
        ]
        self.applySettings()

    def __repr__(self) -> str:
        """
        Returns the current rotor position's string representation.
        """
        return f"{[n2c(rot.curr_pos) for rot in self.rotors]}"

    def setDupeRot(self, duperot_instance: bool) -> None:
        """
        Sets the duperot_instance setting which allows for rotors of the same instance to exist
        """
        if not isinstance(duperot_instance, bool):
            raise TypeError(
                f"duperot_instance Must be a bool type not {type(duperot_instance)}"
            )
        self.duperot_instance = duperot_instance

    def resetSettings(self) -> None:
        """
        Resets the settings for the enigma machine to the settings it was initialized with
        """
        self.initsettings
        self.__init__(*self.initsettings)

    def applySettings(self, reset=False) -> None:
        """
        Applies the settings to the individual components of the enigma
        """
        for i in range(3):
            currot = self.rotors[i]
            if reset:
                currot.shiftPosition(c2n(self.start_pos[i]), -1)
            else:
                currot.shiftPosition(c2n(self.start_pos[i]))
            currot.changeRingsett(c2n(self.ring_setting[i]))

    @staticmethod
    def encsettingCheck(
        enc_nums: int, enc_capitals: int, enc_special: int, enc_whitesp: int
    ) -> None:
        """
        Checks for the types of values in enc_nums, enc_capitals, enc_special and enc_whitesp
        """
        if not isinstance(enc_nums, int):
            raise TypeError("The enc_nums setting must be an integer")
        if enc_nums < 0 or enc_nums > 2:
            raise ValueError(
                "The enc_nums setting must be a value between 0 and 2 inclusive"
            )

        if not isinstance(enc_capitals, int):
            raise TypeError("The enc_capitals setting must be an integer")
        if not enc_capitals == 0 and not enc_capitals == 1:
            raise ValueError("The enc_capitals setting must be a either 0 or 1")

        if not isinstance(enc_special, int):
            raise TypeError("The enc_special setting must be an integer")
        if enc_special < 0 or enc_special > 2:
            raise ValueError(
                "The enc_special setting must be a value between 0 and 2 inclusive"
            )

        if not isinstance(enc_whitesp, int):
            raise TypeError("The enc_whitesp setting must be an integer")
        if enc_whitesp < 0 or enc_whitesp > 2:
            raise ValueError(
                "The enc_whitesp setting must be a value between 0 and 2 inclusive"
            )

    @staticmethod
    def plugboardCheck(plugboard: Union[MutableSequence, tuple]) -> None:
        """
        Checks for the types of values in the plugboard.
        """
        if not isinstance(plugboard, MutableSequence):
            raise TypeError("The plugboard setting must be a mutable sequence")
        for plug in plugboard:
            if not isinstance(plug, (MutableSequence, tuple)):
                raise TypeError(
                    "The plugboard setting must be mutable sequence or tuple"
                )
            if not isinstance(plug[0], str) or not isinstance(plug[1], str):
                raise TypeError("The plugboard items must be a string")
            if not plug[0].isalpha() or not plug[1].isalpha():
                raise ValueError("The plugboard items must a letter between A and Z")

    @staticmethod
    def ringsetCheck(ring_setting: Union[MutableSequence, tuple]) -> None:
        """
        Checks for the types of values in the ring settings.
        """
        if not isinstance(ring_setting, (MutableSequence, tuple)):
            raise TypeError("The start position must be a tuple or a mutable sequence")
        if len(ring_setting) != 3:
            raise ValueError(
                "The start position consists of 3 string or integer values"
            )
        for ring in ring_setting:
            if isinstance(ring, str):
                if ring.isdigit():
                    ring = int(ring)
                elif not ring.isalpha():
                    raise ValueError("The ring setting must a letter between A and Z")
            if isinstance(ring, int):
                if not ring > 0 and ring <= 26:
                    raise ValueError(
                        "The ring setting must be between 1 and 26 inclusive"
                    )
            elif not isinstance(ring, str):
                raise TypeError(
                    f"The ring setting must be between a string or an integer not {type(ring)}"
                )

    @staticmethod
    def reflectorCheck(reflector: str) -> None:
        """
        Checks for the types of values in the reflector.
        """
        if not isinstance(reflector, str):
            raise TypeError("The reflector must be a string")
        if reflector not in storage.reflectors:
            raise KeyError(f"The reflector {reflector} is not a valid reflector id")

    @staticmethod
    def rotorsCheck(rotors: Union[MutableSequence, tuple]) -> None:
        """
        Checks for the types of values in the rotors.
        """
        if not isinstance(rotors, (MutableSequence, tuple)):
            raise TypeError("The rotors must be a mutable sequence or a tuple")
        if len(rotors) != 3:
            raise ValueError("The rotors consists of 3 string or integer values")
        for rot in rotors:
            if (
                rot not in storage.rotors
                and str(rot) not in storage.rotors
                and str(roman2den(rot)) not in storage.rotors
            ):
                raise KeyError(f"The rotor {rot} is not a valid rotor id")

    @staticmethod
    def startposCheck(start_pos: Union[MutableSequence, tuple]) -> None:
        """
        Checks for the types of values in the start position.
        """
        if not isinstance(start_pos, (MutableSequence, tuple)):
            raise TypeError("The start position must be a tuple or a mutable sequence")
        if len(start_pos) != 3:
            raise ValueError(
                "The start position consists of 3 string or integer values"
            )
        for pos in start_pos:
            if isinstance(pos, str):
                if pos.isdigit():
                    pos = int(pos)
                elif not pos.isalpha():
                    raise ValueError("The start position must a letter between A and Z")
            if isinstance(pos, int):
                if not pos > 0 and pos <= 26:
                    raise ValueError(
                        "The start position must be between 1 and 26 inclusive"
                    )
            elif not isinstance(pos, str):
                raise TypeError(
                    f"The start position must be between a string or an integer not {type(pos)}"
                )

    def setRotor(
        self, r1: Union[int, str], r2: Union[int, str], r3: Union[int, str]
    ) -> None:
        """
        Initializes the rotor instance
        """
        temp_rot = []
        rotors = (r1, r2, r3)
        self.rotorsCheck(rotors)
        if not self.duperot_instance:
            for rot in rotors:
                if rotors.count(rot) > 1:
                    raise KeyError(
                        "There cannot be more than one instance of the same rotor."
                    )
        for rot in rotors:
            rot = str(rot)
            if isroman(rot):
                temp_rot.append(str(roman2den(rot)))
            else:
                temp_rot.append(rot)
        temp_rot = tuple(temp_rot)
        self.rotors: Array = Array(Rotor, 3)
        for i in temp_rot:
            rotkey = storage.rotors[i]["key"]
            rotnotch = storage.rotors[i]["notch"]
            self.rotors.insert(self.spawnRotorInstances(rotkey, rotnotch))

    def setReflector(self, reflectr: str) -> None:
        """
        Setter for the reflector
        """
        self.reflectorCheck(reflectr)
        self.reflector = reflectr

    def spawnRotorInstances(self, key: str, notch: Union[tuple, Literal["Z"]]) -> Rotor:
        """
        Spawns a rotor instance
        """
        return Rotor(key, notch)

    def changeEncSettings(
        self,
        enc_nums: int = None,
        enc_capitals: int = None,
        enc_special: int = None,
        enc_whitesp: int = None,
    ) -> None:
        """
        Allows the user to change the encryption settings for enc_nums, enc_capitals, enc_special and enc_whitesp.
        """
        if enc_nums is not None:
            self.enc_settings[0] = enc_nums
        if enc_capitals is not None:
            self.enc_settings[1] = enc_capitals
        if enc_special is not None:
            self.enc_settings[2] = enc_special
        if enc_whitesp is not None:
            self.enc_settings[3] = enc_whitesp
        pass

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

    def applyplugboard(self, char: str) -> str:
        """
        Converts the letters according to the plugboard specification
        """
        if not self.plugboard.isempty():
            for l1, l2 in self.plugboard:
                if char == l1:
                    return l2
                elif char == l2:
                    return l1
        return char

    def encryptChar(self, char: str) -> str:
        """
        Loops the character on the selected rotors for encryption. Goes forward starting with the rightmost rotor then reflects the character on the selected reflector and then goes across the rotors in the reverse order starting with the leftmost rotor and then returns the result
        """
        self.advanceRotor()
        char = self.applyplugboard(char)
        eChar: int = c2n(char)
        # NOTE forward encipher
        for i in range(2, -1, -1):
            convChar = c2n(str(self.rotors[i].tyre[eChar]))
            offset = self.rotors[i].abs_pos
            eChar = (convChar - offset) % 26
            # print(n2c(eChar), self.rotors[self.rotors[i]].abs_pos) DEV debuging character encoding
        # NOTE reflector encipher
        eChar = c2n(storage.reflectors[self.reflector][eChar])
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
        char = self.applyplugboard(char)
        return char

    def encipher(self, string: str, decipher: bool = False) -> str:
        """
        Loops on the string and if bool is false the string is sent to the `transformsp` function to transform the special characters to encryptable characters if bool is false then automatically skips past the transform special characters function and then loops on the string and the sends each character to the `encryptChar` method to be encrypted
        """
        normalized_str = ""
        retstr = ""
        # if not deciphering transform all special characters to encryptable characters
        if not decipher and self.enc_settings != [0, 0, 0, 0]:
            for char in string:
                normalized_str += transformsp(char, self.enc_settings)
        # if all settings are on ignore or is deciphering the string is not changed
        else:
            normalized_str = string
        for char in normalized_str:
            # if all settings are on ignore or and the character isn't an alphabet character the character is not changed else encrypt the character
            if self.enc_settings == [0, 0, 0, 0] and not char.isalpha():
                retstr += char
            else:
                char = char.upper()
                retstr += self.encryptChar(char)
        return retstr

    def decipher(self, string: str) -> str:
        """
        Calls the `encipher` method to decipher the string then `rmspecial` function to remove special characters before displaying to the user
        """
        return rmspecial(self.encipher(string, True))


if __name__ == "__main__":
    pass
