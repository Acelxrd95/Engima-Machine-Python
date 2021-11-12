from Enigma.datastructs import Map
from Enigma.utils import roman2den, isroman


"""
Storage for rotors and reflectors
"""

rotors = Map(
    {
        "1": {"key": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "notch": "Q"},
        "2": {"key": "AJDKSIRUXBLHWTMCQGZNPYFVOE", "notch": "E"},
        "3": {"key": "BDFHJLCPRTXVZNYEIWGAKMUSQO", "notch": "V"},
        "4": {"key": "ESOVPZJAYQUIRHXLNFTGKDCMWB", "notch": "J"},
        "5": {"key": "VZBRGITYUPSDNHLXAWMJQOFECK", "notch": "Z"},
        "6": {"key": "JPGVOUMFYQBENHZRDKASXLICTW", "notch": ("Z", "M")},
        "7": {"key": "NZJHGRCXMYSWBOUFAIVLPEKQDT", "notch": ("Z", "M")},
        "8": {"key": "FKQHTLXOCBJSPDZRAMEWNIUYGV", "notch": ("Z", "M")},
    }
)
reflectors = Map(
    {
        "A": "EJMZALYXVBWFCRQUONTSPIKHGD",
        "B": "YRUHQSLDPXNGOKMIEBFZCWVJAT",
        "C": "FVPJIAOYEDRZXWGCTKUQSBNMHL",
    }
)


def addCustomRotor(
    rotor_id: str, key: str, notch: tuple, allowdupes: bool = False
) -> None:
    """
    Allows the user to add custom rotors with custom keys and notches
    """
    if isroman(rotor_id):
        rotor_id = str(roman2den(rotor_id))
    if rotor_id in rotors:
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
    if isinstance(notch, str) and len(notch) >= 2:
        notch = tuple(notch.split(","))
    for n in notch:
        if n not in key:
            raise Exception(
                f"The provided notch {notch} does not exist in the specified key {key}"
            )
    rotors.update({rotor_id: {"key": key, "notch": notch}})


def addCustomReflector(reflector_id: str, key: str, allowdupes: bool = False) -> None:
    """
    Allows the user to add custom reflectors with custom keys
    """
    if isroman(reflector_id):
        reflector_id = str(roman2den(reflector_id))
    if reflector_id in reflectors:
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
    reflectors.update({reflector_id: key})
