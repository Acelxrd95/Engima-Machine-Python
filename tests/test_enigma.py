import unittest
import pycipher
import Enigma.enigma as en
from faker import Faker
import random
from Enigma.utils import rmspecial, transformsp

fake = Faker()

alphastr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
allstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,(){}[]?/\\'"
alphali = list(alphastr)


class EnsureCipher(unittest.TestCase):
    def test_encryption_decryption(self):
        enigma = en.Enigma(
            start_pos=("A", "F", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ring_setting=("A", "A", "A"),
            plugboard=[],
            enc_nums=1,
            enc_capitals=1,
            enc_special=1,
            enc_whitesp=2,
        )
        string = fake.paragraph()
        enc_string = enigma.encipher(string)
        enigma.resetSettings()
        self.assertEqual(enigma.decipher(enc_string), string.replace(" ", ""))

    def test_cipher(self):
        enigma = pycipher.Enigma(
            settings=("A", "A", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ringstellung=("A", "A", "A"),
            steckers=[],
        )
        mach1 = en.Enigma(
            start_pos=("A", "A", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ring_setting=("A", "A", "A"),
            plugboard=[],
        )
        self.assertEqual(
            enigma.encipher(alphastr),
            mach1.encipher(alphastr.lower()).upper(),
        )

    def test_plugboard(self):
        enigma = pycipher.Enigma(
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
        mach1 = en.Enigma(
            start_pos=("A", "A", "A"),
            rotors=(1, 2, 3),
            reflector="B",
            ring_setting=("A", "A", "A"),
            plugboard=[
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
        self.assertEqual(
            enigma.encipher(alphastr),
            mach1.encipher(alphastr.lower()).upper(),
        )

    def test_random_settings_cipher(self):
        settin_test = []
        rot_test = []
        reflect_test = random.choice(["A", "B", "C"])
        ring_test = []
        stckr_test = []
        for _ in range(3):
            settin_test.append(random.choice(alphali))
            rot_test.append(random.randint(1, 8))
            ring_test.append(random.choice(alphali))
        enigma = pycipher.Enigma(
            settings=settin_test,
            rotors=rot_test,
            reflector=reflect_test,
            ringstellung=ring_test,
            steckers=stckr_test,
        )
        mach1 = en.Enigma(
            start_pos=settin_test,
            rotors=rot_test,
            reflector=reflect_test,
            ring_setting=ring_test,
            plugboard=stckr_test,
            duperot_instance=True,
        )
        self.assertEqual(
            enigma.encipher(alphastr),
            mach1.encipher(alphastr.lower()).upper(),
            f"{settin_test}\n{rot_test}\n{reflect_test}\n{ring_test}\n{stckr_test}\n",
        )


class UtilsTest(unittest.TestCase):
    def test_sp_encoding(self):
        string = 'ABC(defGHIj)kl123.,"/"\\"'
        encoded_str = ""
        for char in string:
            encoded_str += transformsp(char)
        self.assertEqual(
            encoded_str,
            "JXAJXBJXCKZKDEFJXGJXHJXIJKZKKLJMJONEJMJJMJTWOJMJJMJTHREEJMJYJYZZZXXXYXXXYZYXX",
        )

    def test_sp_decoding(self):
        encoded_str = "JXAJXBJXCKZKDEFJXGJXHJXIJKZKKLJMJONEJMJJMJTWOJMJJMJTHREEJMJYJYZZZXXXYXXXYZYXX"
        decoded_str = rmspecial(encoded_str)
        self.assertEqual(
            decoded_str,
            'ABC(defGHIj)kl123.,"/"\\"',
        )

    def test_sp_bothway(self):
        string = fake.paragraph()
        encoded_str = ""
        for char in string:
            encoded_str += transformsp(char)
        decoded_str = rmspecial(encoded_str)
        self.assertEqual(decoded_str, string)


if __name__ == "__main__":
    unittest.main()
