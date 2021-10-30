import click

# @click.command()
# def hehe

"""
Options:
    -s CHAR, CHAR, CHAR --start-pos=(CHAR, CHAR, CHAR)  Rotors starting position
    -r1 CHAR --rotor-1=CHAR Rotor to be used
    -r2 CHAR --rotor-2=CHAR Rotor to be used
    -r3 CHAR --rotor-3=CHAR Rotor to be used
    -rf CHAR --reflector=CHAR Reflector to be used
    -rs CHAR, CHAR, CHAR --ring-setting=(CHAR, CHAR, CHAR)  Rotors ring setting
    -p [(CHAR,CHAR),...]

Encryption Settings
    -n INT --encrypt-num=INT   Ignore (0), Encrypted (1) or Remove (2) numbers (default 0)
    -N  Encrypt numbers
    -c INT --encrypt-capital=INT   Ignore (0), Encrypted (1) or Remove (2) capitals (default 0)
    -C  Encrypt capitals
    -sp INT --encrypt-special=INT   Ignore (0), Encrypted (1) or Remove (2) special characters (default 0)
    -SP Encrypt special characters
    -w INT --encrypt-num=INT   Ignore (0), Encrypted (1) or Remove (2) whitespace (default 0)
    -W  Encrypt whitespace
    -0  Ignore all numbers, capitals, special characters and whitespace
    -1  Encrypt all numbers, capitals, special characters and whitespace
    -2  Remove all numbers, special characters and whitespace

Customization
    --custom-rotor
    --custom-reflector
"""
