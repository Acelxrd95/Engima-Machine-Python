import unittest
import pycipher
import old_enigma as en
import enigma as en2
from faker import Faker
import random

fake = Faker()

alphastr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphali = list(alphastr)


class EnsureCipher(unittest.TestCase):
    def test_encryption_decryption(self):
        enigma = en2.Enigma(
            settings=("A", "F", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("A", "B", "A"),
            steckers=[],
        )
        string = fake.paragraph()
        enc_string = enigma.encipher(string)
        enigma.resetSettings()
        self.assertEqual(enigma.decipher(enc_string), string.upper())

    def test_cipher(self):
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
            enigma.encipher(alphastr),
            mach1.encipher(alphastr),
        )
        pass

    def test_random_settings_cipher(self):
        settin_test = []
        rot_test = []
        reflect_test = random.choice(["A", "B", "C"])
        ring_test = []
        stckr_test = []
        for i in range(3):
            settin_test.append(random.choice(alphali))
            rot_test.append(random.randint(1, 8))
            ring_test.append(random.choice(alphali))
        print(settin_test, rot_test, reflect_test, ring_test, stckr_test)

        enigma = pycipher.Enigma(
            settings=settin_test,
            rotors=rot_test,
            reflector=reflect_test,
            ringstellung=ring_test,
            steckers=stckr_test,
        )
        mach1 = en2.Enigma(
            settings=settin_test,
            rotors=rot_test,
            reflector=reflect_test,
            ringstellung=ring_test,
            steckers=stckr_test,
        )
        self.assertEqual(
            enigma.encipher(alphastr),
            mach1.encipher(alphastr),
            f"{settin_test}\n{rot_test}\n{reflect_test}\n{ring_test}\n{stckr_test}\n",
        )
        pass


if __name__ == "__main__":
    unittest.main()
