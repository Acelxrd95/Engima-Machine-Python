from datastructs.map_struct import Map
from datastructs.array_struct import Array
import re

r_dict = Map({"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1})
nm_dict = {
    # "0": ("NULL", "ZERO"),
    "0": "NULL",
    "1": "ONE",
    "2": "TWO",
    "3": "THREE",
    "4": "FOUR",
    "5": "FIVE",
    "6": "SIX",
    "7": "SEVEN",
    "8": "EIGHT",
    "9": "NINE",
}
sp_dict = {
    ".": "YJY",
    ",": "ZZZ",
    "(": "KZK",
    ")": "KZK",
    "{": "KZK",
    "}": "KZK",
    "[": "KZK",
    "]": "KZK",
    "?": "UDU",
    "$": "JMJ",
    "^": "JX",
    "/": "XYX",
    "\\": "YZY",
    '"': "XX",
    "'": "XX",
}


def roman2den(roman: str) -> int:
    last, total = 0, 0
    for c in list(roman)[::-1]:
        if last == 0:
            total += r_dict[c]
        elif last > r_dict[c]:
            total -= r_dict[c]
        else:
            total += r_dict[c]
        last = r_dict[c]
    return total


def isroman(roman: str) -> bool:
    for char in roman:
        if char not in r_dict.keys():
            return False
    return True


def c2n(char: str) -> int:
    """
    Converts Number to a character
    """
    num = 0
    if char.isupper():
        num = ord(char) - 65
    elif char.islower():
        num = ord(char) - 97
    return num


def n2c(num: int, upper: bool = True) -> str:
    """
    Converts Number to a character
    """
    num %= 26
    if num < 0:
        num += 25
    if upper:
        char = chr(num + 65)
    else:
        char = chr(num + 97)
    return char


def isspecial(char: str) -> bool:
    if char in sp_dict.keys():
        return True
    else:
        return False


def sp2norm(char: str, sp_setting: int = 1, whitesp_setting: int = 1) -> str:
    if isspecial(char):
        if sp_setting == 1:
            char = sp_dict[char]
        elif sp_setting == 2:
            char = ""
    elif char.isspace():
        if whitesp_setting == 1:
            char = "QYQ"
        elif whitesp_setting == 2:
            char = ""
    return char


def num2word(number: str, setting: int) -> str:
    if setting == 1:
        retNum = ""
        for num in number:
            retNum += nm_dict[num]
            retNum += "$"
        number = f"${retNum}"
    elif setting == 2:
        number = ""
    return number


def up2low(char: str, setting: int) -> str:
    if setting == 1:
        char = f"^{char}"
    return char


def transformsp(char: str, settings=[1, 1, 1, 1]) -> str:
    if char.isalpha():
        if char.islower():
            char = char.upper()
        elif char.isupper():
            char = up2low(char, settings[1])
    elif char.isnumeric():
        char = num2word(char, settings[0])
    if char != "" and (isspecial(char[0]) or char.isspace()):
        if char[0] == "$":
            char = sp2norm(char[0]) + char[1:-1] + sp2norm(char[-1])
        else:
            char = sp2norm(char[0], settings[2], settings[3]) + char[1:]
    else:
        char = char
    return char


def rmspecial(word: str) -> str:
    word = re.sub(r"KZK(.*)KZK", r"(\g<1>)", word)
    for key, val in sp_dict.items():
        word = word.replace(val, key)
    word = word.replace("QYQ", " ")
    nextact = ""
    numvar = ""
    x = list(nm_dict.values())
    newstr = ""
    for i in range(len(word)):
        char = word[i]
        if char == "$" and nextact == "$":
            char = list(nm_dict.keys())[x.index(numvar)]
            newstr += char
            numvar = ""
            nextact = ""
        elif nextact == "$":
            numvar += char
        elif char == "$":
            nextact = char
        elif char == "^":
            nextact = char
        elif nextact == "^":
            newstr += char.upper()
            nextact = ""
        else:
            newstr += char.lower()
    return newstr


# def norm2sp(string: str) -> str:
#     x = re.sub(r"JX([A-Z])", r"^\g<1>", retstr)


if __name__ == "__main__":
    # for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    #     print(c2n(char))
    #     print(n2c(c2n(char)))
    print(transformsp("1"))
