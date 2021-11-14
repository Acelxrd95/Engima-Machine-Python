<!-- @format -->

# Enigma-Machine-Python

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
   `git clone`https://github.com/Acelxrd95/Enigma-Machine-Python.git
2. cd into the directory by using `cd Enigma-Machine-Python`
3. run `pip install .`
4. run tests with `python tests/test_enigma.py` to make sure that dependancies are up to date

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
  -s, --starting-position [A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z]...
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
from Enigma.enigma import Enigma
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

Full Enigma machine project documentation can be found in [Modules](MODULES.md#enigma-machine-modules)

# Running-the-tests

Tests can be run with `python test_enigma.py` to make sure that dependancies are up to date
