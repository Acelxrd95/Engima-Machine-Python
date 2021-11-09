<!-- @format -->

# Engima-Machine-Python

This project is a software implementation for the Enigma encryption machine used by the German military in World War II. The Enigma encryption is a type of substitution cipher where a character is passed through a few parameters in order to encrypt it to another character, but the power of the enigma as opposed to for example a Caesar cipher is that typing the same letter results in a different output due to the encryption of the letters dependant on the rotor’s chosen, their positions, their ring settings and the plugboard wiring. All these are factors that would change the output cipher

# Table-of-Contents

-   [Demo-Preview](#Demo-Preview)
-   [Features](#Features)
-   [Prerequisite](#Prerequisite)
-   [Installation](#Installation)
-   [Usage](#Usage)
-   [Running-the-tests](#Running-the-tests)
-   [Todo](#Todo)

# Demo-Preview

# Features

-   Set the starting positions for the rotors
-   Select 3 from a list of rotors
-   Add and use custom made rotors
-   Select a reflector from a list of reflectors
-   Add and use custom made reflectors
-   Set the ring settings for each of the rotors
-   Set the wiring for the plugboard
-   Choose whether to ignore, encrypt or remove special characters. capitals, whitespace and numbers

# Prerequisite

-   Python 3.9+

# Installation

1. clone repository from github using \
   `git clone https://github.com/Acelxrd95/Engima-Machine-Python.git`
2. run `python setup.py`
3. run tests with `python test_enigma.py` to make sure that dependancies are up to date

# Usage

Can be used in the terminal by typing `python enigmaTerm.py [OPTIONS] STRING`
whereas options are the options passed to the enigma and string is the string to be enciphered/deciphered

help can be displayed using `python enigmaTerm.py --help`
the help message is

```powershell
Usage: enigmaTerm.py [OPTIONS] STRING

Options:
  -e, --encipher / -d, --decipher
                                  Whether to encrypt or decrypt the string
  -s, --start-position [A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z]...
                                  Rotors starting position  [default: A, A, A]
  -r, --rotors TEXT               Rotor to be used  [default: 1, 2, 3]
  -rf, --reflector TEXT           Reflector to be used  [default: B]
  -rs, --ring-setting [A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z]...
                                  Rotors ring setting  [default: A, A, A]
  -p, --plugboard [A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z]...
                                  Plugboard configuration  [default: ('P',
                                  'O'), ('M', 'L'), ('I', 'U'), ('K', 'J'),
                                  ('N', 'H'), ('Y', 'T'), ('G', 'B'), ('V',
                                  'F'), ('R', 'E'), ('D', 'C')]
  -n, --encrypt-num [0|1|2]       Ignore (0), Encrypted (1) or Remove (2)
                                  numbers  [default: 0]
  -c, --encrypt-capital [0|1]     Ignore (0), Encrypted (1) or Remove (2)
                                  capitals  [default: 0]
  -sp, --encrypt-special [0|1|2]  Ignore (0), Encrypted (1) or Remove (2)
                                  special  [default: 0]
  -w, --encrypt-whitespace [0|1|2]
                                  Ignore (0), Encrypted (1) or Remove (2)
                                  whitespace  [default: 0]
  --help                          Show this message and exit.
```

The enigma class can be imported into your python project and then called with some arguments

```python
from enigma import Enigma
machine = Enigma(
    start_pos=("A", "A", "A"),       #Choose rotors starting positions
    rotors=(1, 2, 3),                #Choose rotors to be used
    reflector=reflector_id,          #Choose reflector to be used
    ring_setting=("A", "A", "A"),    #Choose ring settings
    plugboard=[                      #Choose plugs to be used in plugboard
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
    enc_nums= 0,                     #toggles the encryption of numbers
    enc_capitals= 0,                 #toggles the encryption of capitals
    enc_special= 0,                  #toggles the encryption of special characters
    enc_whitesp= 0,                  #toggles the encryption of whitespace
    duperot_instance= Boolean,       #allows the usage of the same rotor in different positions
)
```

See [Developer documentation](#Dev-documentation) for more details.

# Dev-documentation

Main class for the enigma is `Enigma` which takes some parameters

`param start_pos`
: refers to the rotors start positions, which consists of 3 characters ex:('F','G' 'B')

`param rotors`
: specifies the rotors used and their order. There are 8 possible rotors labeled from 1 through 8. More rotors can be added using the `addCustRotor` method

`param reflector`
: specifies the reflector used More can be specified using the addCustReflect method

`param ring_setting`
: refers to the ring settings and consists of 3 characters ex:('F','G','B')

`param plugboard`
: specifies the plugboard settings, indicating which characters are mapped to eachother. Consists of max 10 tuples of 2-tuples

`param enc_nums`
: specifies whether numbers should be ignored (0), encrypted (1) or removed (2)

`param enc_capitals`
: specifies whether capitals should be ignored (0), encrypted (1)

`param enc_special`
: specifies whether special characters should be ignored (0), encrypted (1) or removed (2)

`param enc_whitesp`
: specifies whether spaces should be ignored (0), encrypted (1) or removed (2)

The enigma class has some methods like:

`encipher(string, bool)`
: Loops on the string and if bool is false the string is sent to the `transformsp` function to transform the special characters to encryptable characters if bool is false then automatically skips past the transform special characters function and then loops on the string and the sends each character to the `encryptChar` method to be encrypted

`decipher(string)`
: Calls the `encipher` method to decipher the string then `rmspecial` function to remove special characters before displaying to the user

# Running-the-tests

Tests can be run with `python test_enigma.py` to make sure that dependancies are up to date

# Todo

-   [x] Encryption of Capital Letters
-   [x] CHoose correct Data Structures
-   [x] Encryption of Numbers and Symbols
-   [x] Addition of custom reflectors
-   [x] Addition of Custom Rotors
-   [x] Add error messages
-   [x] Unit tests
-   [x] Toggle sp replacment
-   [x] Plugboard
-   [x] Argparser
-   [x] Multithreading tried but failed due to usage of cTypes
-   [ ] Complete Readme
-   [ ] save files + output
