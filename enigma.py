from typing import Literal, MutableSequence, TypeAlias
from utils import *
from rotor import Rotor
import storage
from datastructs.array_struct import Array


class Enigma:
    """
    The main Enigma machine class

    :param start_pos: refers to the rotors start positions, which consists of 3 characters ex:('F','G','B')
    :param rotors: specifies the rotors used and their order. There are 8 possible rotors labeled from 1 through 8. More rotors can be added using the addCustRotor method
    :param reflector: specifies the reflector used More can be specified using the addCustReflect method
    :param ring_setting: refers to the ring settings and consists of 3 characters ex:('F','G','B')
    :param plugboard: specifies the plugboard settings, indicating which characters are mapped to eachother. Consists of max 10 tuples of 2-tuples
    :param enc_nums: specifies whether numbers should be ignored (0), encrypted (1) or removed (2)
    :param enc_capitals:specifies whether capitals should be ignored (0), encrypted (1)
    :param enc_special:specifies whether special characters should be ignored (0), encrypted (1) or removed (2)
    :param enc_whitesp:specifies whether spaces should be ignored (0), encrypted (1) or removed (2)
    """

    def __init__(
        self,
        start_pos: tuple[str, str, str] | list[str] = ("A", "A", "A"),
        rotors: tuple[int, int, int]
        | list[int]
        | tuple[str, str, str]
        | list[str] = ("I", "II", "III"),
        reflector: str = "B",
        ring_setting: tuple[str, str, str] | list[str] = ("A", "A", "A"),
        plugboard: list[tuple[str, str]] = None,
        enc_nums: int = 0,
        enc_capitals: int = 0,
        enc_special: int = 0,
        enc_whitesp: int = 0,
        reflect2rotor: bool = False,
        duperot_instance: bool = False,
    ) -> None:
        self.setReflect2rotor(reflect2rotor)
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
            reflect2rotor,
            duperot_instance,
        ]
        self.applySettings()

    def __repr__(self) -> str:
        retstr = ""
        return retstr

    def setDupeRot(self, duperot_instance):
        """
        Sets the duperot_instance setting which allows for rotors of the same instance to exist
        """
        if not isinstance(duperot_instance, bool):
            raise TypeError(
                f"duperot_instance Must be a bool type not {type(duperot_instance)}"
            )
        self.duperot_instance = duperot_instance

    def setReflect2rotor(self, reflect2rotor):
        """
        Sets the reflect2rotor setting which allows the reflector to be a 4th rotor
        """
        if not isinstance(reflect2rotor, bool):
            raise TypeError(
                f"reflect2rotor Must be a bool type not {type(reflect2rotor)}"
            )
        self.reflect2rotor = reflect2rotor

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

    def encsettingCheck(self, enc_nums, enc_capitals, enc_special, enc_whitesp):
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

    def plugboardCheck(self, plugboard):
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

    def ringsetCheck(self, ring_setting):
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

    def reflectorCheck(self, reflector):
        """
        Checks for the types of values in the reflector.
        """
        if not isinstance(reflector, str):
            raise TypeError("The reflector must be a string")
        if reflector not in storage.reflectors:
            raise KeyError(f"The reflector {reflector} is not a valid reflector id")

    def rotorsCheck(self, rotors):
        """
        Checks for the types of values in the rotors.
        """
        if not isinstance(rotors, (MutableSequence, tuple)):
            raise TypeError("The rotors must be a mutable sequence or a tuple")
        if len(rotors) != 3:
            raise ValueError("The rotors consists of 3 string or integer values")
        for rot in rotors:
            if rot not in storage.rotors and str(rot) not in storage.rotors:
                raise KeyError(f"The rotor {rot} is not a valid rotor id")

    def startposCheck(self, start_pos):
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

    def setRotor(self, r1: int | str, r2: int | str, r3: int | str) -> None:
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
        if self.reflect2rotor:
            self.reflector = self.spawnRotorInstances(
                storage.reflectors[reflectr], ("Z")
            )
        self.reflector = reflectr

    def spawnRotorInstances(self, key: str, notch: tuple | Literal["Z"]) -> Rotor:
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
    ):
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

    def addCustomRotor(
        self, rotor_id: str, key: str, notch: tuple, allowdupes=False
    ) -> None:
        """
        Allows the user to add custom rotors with custom keys and notches
        """
        if isroman(rotor_id):
            rotor_id = str(roman2den(rotor_id))
        if rotor_id in storage.rotors:
            raise Exception(f"A rotor with the ID {rotor_id} already exists")
        if len(key) != 26:
            raise Exception("Rotor keys must be 26 characters long")
        if not allowdupes:
            tmpkey = []
            for k in key:
                if k in tmpkey:
                    raise Exception(
                        f"There letter {k} was found as dupelicate the key provided"
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
        storage.rotors.update({rotor_id: {"key": key, "notch": notch}})

    def addCustomReflector(self, reflector_id: str, key: str, allowdupes=False) -> None:
        """
        Allows the user to add custom reflectors with custom keys
        """
        if isroman(reflector_id):
            reflector_id = str(roman2den(reflector_id))
        if reflector_id in storage.reflectors:
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
        storage.reflectors.update({reflector_id: key})

    def advanceRotor(self) -> None:
        """
        Advances the rotors acording to the notch and their positions
        """
        if (
            self.rotors[0].check_notch
            and isinstance(self.reflector, Rotor)
            and self.reflect2rotor
        ):
            self.rotors[0].shiftPosition(1)
            self.reflector.shiftPosition(1)

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
        Loops the character on the selected rotors for encryption.
        Goes forward starting with the rightmost rotor then reflects the character on the selected reflector and then goes across the rotors in the reverse order starting with the leftmost rotor and then returns the result
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
        if isinstance(self.reflector, Rotor) and self.reflect2rotor:
            eChar = c2n(self.reflector.tyre[eChar])
        else:
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
    pass
