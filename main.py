# import unittest
# import pycipher
# import old_enigma as en
# import enigma as en2
# from faker import Faker
# import random
# from utils import *

# fake = Faker()

# alphastr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# allstr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,(){}[]?/\\'"
# alphali = list(alphastr)

# string = "Decide large year manage. Order forget resource size commercial leave senior control. Discuss wear scientist no really. Me teach man ok price whose."
# encoded_str = ""
# for char in string:
#     encoded_str += transformsp(char)
# decoded_str = rmspecial(encoded_str)
# print(decoded_str)
# print(string)
# from enigma import Enigma

# mach = Enigma(
#     start_pos=("A", "A", "A"),
#     rotors=(1, 2, 3),
#     reflector="B",
#     ring_setting=("A", "A", "A"),
#     plugboard=[
#         ("P", "O"),
#         ("M", "L"),
#         ("I", "U"),
#         ("K", "J"),
#         ("N", "H"),
#         ("Y", "T"),
#         ("G", "B"),
#         ("V", "F"),
#         ("R", "E"),
#         ("D", "C"),
#     ],
# )
# x = mach.encipher("Hello world")
# print(x)
# mach.resetSettings()
# print(mach.encipher(x))
import pycipher

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
print(enigma.encipher("hello"))
