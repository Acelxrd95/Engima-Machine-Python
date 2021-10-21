import unittest
import pycipher
import old_enigma as en
import enigma as en2


class EnsureCypher(unittest.TestCase):
    def test_cypher(self):
        enigma = pycipher.Enigma(
            settings=("A", "A", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("A", "A", "A"),
            steckers=[],
        )
        mach1 = en2.Enigma(
            settings=("A", "A", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("A", "A", "A"),
            steckers=[],
        )
        self.assertEqual(
            enigma.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            mach1.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        )
        pass

    def test_other_settings_cypher(self):
        enigma = pycipher.Enigma(
            settings=("A", "F", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("A", "Z", "A"),
            steckers=[],
        )
        mach1 = en2.Enigma(
            settings=("A", "F", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("A", "Z", "A"),
            steckers=[],
        )
        self.assertEqual(
            enigma.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
            mach1.encipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
        )
        pass


# if __name__ == "__main__":
#     unittest.main()
