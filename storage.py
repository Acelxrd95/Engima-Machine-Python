from datastructs.map_struct import Map


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
