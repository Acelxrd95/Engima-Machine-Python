def roman2den(roman: str) -> int:
    r_dict = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

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


def c2n(char: str) -> int:
    """
    Converts Number to a character
    """
    num = 0
    if char.isupper():
        num = ord(char) - 65
        cap = True
    elif char.islower():
        num = ord(char) - 97
        cap = False

    return num


def n2c(num: int, upper: bool = True) -> str:
    """
    Converts Number to a character
    """
    if num > 25:
        num %= 26
    if upper:
        char = chr(num + 65)
    else:
        char = chr(num + 97)
    return char
