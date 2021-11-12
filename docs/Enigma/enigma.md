# Enigma

> Auto-generated documentation for [Enigma.enigma](blob/master/Enigma/enigma.py) module.

- [Enigma machine](..\README.md#enigma-machine-index) / [Modules](..\MODULES.md#enigma-machine-modules) / [Enigma](index.md#enigma) / Enigma
    - [Enigma](#enigma)
        - [Enigma().\_\_repr\_\_](#enigma__repr__)
        - [Enigma().advanceRotor](#enigmaadvancerotor)
        - [Enigma().applySettings](#enigmaapplysettings)
        - [Enigma().applyplugboard](#enigmaapplyplugboard)
        - [Enigma().changeEncSettings](#enigmachangeencsettings)
        - [Enigma().decipher](#enigmadecipher)
        - [Enigma().encipher](#enigmaencipher)
        - [Enigma().encryptChar](#enigmaencryptchar)
        - [Enigma.encsettingCheck](#enigmaencsettingcheck)
        - [Enigma.plugboardCheck](#enigmaplugboardcheck)
        - [Enigma.reflectorCheck](#enigmareflectorcheck)
        - [Enigma().resetSettings](#enigmaresetsettings)
        - [Enigma.ringsetCheck](#enigmaringsetcheck)
        - [Enigma.rotorsCheck](#enigmarotorscheck)
        - [Enigma().setDupeRot](#enigmasetduperot)
        - [Enigma().setReflector](#enigmasetreflector)
        - [Enigma().setRotor](#enigmasetrotor)
        - [Enigma().spawnRotorInstances](#enigmaspawnrotorinstances)
        - [Enigma.startposCheck](#enigmastartposcheck)

## Enigma

[[find in source code]](blob/master/Enigma/enigma.py#L8)

```python
class Enigma():
    def __init__(
        start_pos: Union[(tuple[(str, str, str)], list[str])] = ('A', 'A', 'A'),
        rotors: Union[(tuple[(int, int, int)], list[int], tuple[(str, str, str)], list[str])] = ('I', 'II', 'III'),
        reflector: str = 'B',
        ring_setting: Union[(tuple[(str, str, str)], list[str])] = ('A', 'A', 'A'),
        plugboard: list[tuple[(str, str)]] = None,
        enc_nums: int = 0,
        enc_capitals: int = 0,
        enc_special: int = 0,
        enc_whitesp: int = 0,
        duperot_instance: bool = False,
    ) -> None:
```

Enigma machine class.

This class is a software implementation for the Enigma encryption machine used by the German
military in World War II. The Enigma encryption is a type of substitution cipher where a
character is passed through a few parameters in order to encrypt it to another character, but
the power of the enigma as opposed to for example a Caesar cipher is that typing the same
letter results in a different output due to the encryption of the letters dependant on the
rotor’s chosen, their positions, their ring settings and the plugboard wiring. All these are
factors that would change the output cipher

#### Attributes

start_pos (Union[tuple[str, str, str], list[str]]):
    refers to the rotors start positions, which consists of 3 characters ex:('F','G','B').
rotors (Union[tuple[int, int, int], list[int], tuple[str, str, str], list[str]]):
    specifies the rotors used and their order. There are 8 possible rotors labeled from 1 through 8. More rotors can be added using the `addCustRotor` method
reflector (str):
    specifies the reflector used More can be specified using the `addCustReflect` method
ring_setting (Union[tuple[str, str, str], list[str]]):
    refers to the ring settings and consists of 3 characters ex:('F','G','B')
plugboard (list[tuple[str, str]]):
    specifies the plugboard settings, indicating which characters are mapped to eachother. Consists of max 10 tuples of 2-tuples
enc_nums (int):
    specifies whether numbers should be ignored (0), encrypted (1) or removed (2)
enc_capitals (int):
    specifies whether capitals should be ignored (0), encrypted (1)
enc_special (int):
    specifies whether special characters should be ignored (0), encrypted (1) or removed (2)
enc_whitesp (int):
    specifies whether spaces should be ignored (0), encrypted (1) or removed (2)

#### Examples

machine = Enigma(
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
    enc_nums= 0,
    enc_capitals= 0,
    enc_special= 0,
    enc_whitesp= 0,
    duperot_instance= Flase,
)

### Enigma().\_\_repr\_\_

[[find in source code]](blob/master/Enigma/enigma.py#L121)

```python
def __repr__() -> str:
```

Returns the current rotor position's string representation.

### Enigma().advanceRotor

[[find in source code]](blob/master/Enigma/enigma.py#L348)

```python
def advanceRotor() -> None:
```

Advances the rotors acording to the notch and their positions

### Enigma().applySettings

[[find in source code]](blob/master/Enigma/enigma.py#L144)

```python
def applySettings(reset: bool = False) -> None:
```

Applies the settings to the individual components of the enigma

### Enigma().applyplugboard

[[find in source code]](blob/master/Enigma/enigma.py#L361)

```python
def applyplugboard(char: str) -> str:
```

Converts the letters according to the plugboard specification

### Enigma().changeEncSettings

[[find in source code]](blob/master/Enigma/enigma.py#L328)

```python
def changeEncSettings(
    enc_nums: int = None,
    enc_capitals: int = None,
    enc_special: int = None,
    enc_whitesp: int = None,
) -> None:
```

Allows the user to change the encryption settings for enc_nums, enc_capitals, enc_special and enc_whitesp.

### Enigma().decipher

[[find in source code]](blob/master/Enigma/enigma.py#L425)

```python
def decipher(string: str) -> str:
```

Calls the [Enigma().encipher](#enigmaencipher) method to decipher the string then `rmspecial` function to remove special characters before displaying to the user

### Enigma().encipher

[[find in source code]](blob/master/Enigma/enigma.py#L403)

```python
def encipher(string: str, decipher: bool = False) -> str:
```

Loops on the string and if bool is false the string is sent to the `transformsp` function to transform the special characters to encryptable characters if bool is false then automatically skips past the transform special characters function and then loops on the string and the sends each character to the [Enigma().encryptChar](#enigmaencryptchar) method to be encrypted

### Enigma().encryptChar

[[find in source code]](blob/master/Enigma/enigma.py#L373)

```python
def encryptChar(char: str) -> str:
```

Loops the character on the selected rotors for encryption. Goes forward starting with the rightmost rotor then reflects the character on the selected reflector and then goes across the rotors in the reverse order starting with the leftmost rotor and then returns the result

### Enigma.encsettingCheck

[[find in source code]](blob/master/Enigma/enigma.py#L156)

```python
@staticmethod
def encsettingCheck(
    enc_nums: int,
    enc_capitals: int,
    enc_special: int,
    enc_whitesp: int,
) -> None:
```

Checks for the types of values in enc_nums, enc_capitals, enc_special and enc_whitesp

### Enigma.plugboardCheck

[[find in source code]](blob/master/Enigma/enigma.py#L189)

```python
@staticmethod
def plugboardCheck(plugboard: Union[(MutableSequence, tuple)]) -> None:
```

Checks for the types of values in the plugboard.

### Enigma.reflectorCheck

[[find in source code]](blob/master/Enigma/enigma.py#L233)

```python
@staticmethod
def reflectorCheck(reflector: str) -> None:
```

Checks for the types of values in the reflector.

### Enigma().resetSettings

[[find in source code]](blob/master/Enigma/enigma.py#L137)

```python
def resetSettings() -> None:
```

Resets the settings for the enigma machine to the settings it was initialized with

### Enigma.ringsetCheck

[[find in source code]](blob/master/Enigma/enigma.py#L206)

```python
@staticmethod
def ringsetCheck(ring_setting: Union[(MutableSequence, tuple)]) -> None:
```

Checks for the types of values in the ring settings.

### Enigma.rotorsCheck

[[find in source code]](blob/master/Enigma/enigma.py#L243)

```python
@staticmethod
def rotorsCheck(rotors: Union[(MutableSequence, tuple)]) -> None:
```

Checks for the types of values in the rotors.

### Enigma().setDupeRot

[[find in source code]](blob/master/Enigma/enigma.py#L127)

```python
def setDupeRot(duperot_instance: bool) -> None:
```

Sets the duperot_instance setting which allows for rotors of the same instance to exist

### Enigma().setReflector

[[find in source code]](blob/master/Enigma/enigma.py#L315)

```python
def setReflector(reflectr: str) -> None:
```

Setter for the reflector

### Enigma().setRotor

[[find in source code]](blob/master/Enigma/enigma.py#L287)

```python
def setRotor(
    r1: Union[(int, str)],
    r2: Union[(int, str)],
    r3: Union[(int, str)],
) -> None:
```

Initializes the rotor instance

### Enigma().spawnRotorInstances

[[find in source code]](blob/master/Enigma/enigma.py#L322)

```python
def spawnRotorInstances(
    key: str,
    notch: Union[(tuple, Literal['Z'])],
) -> Rotor:
```

Spawns a rotor instance

#### See also

- [Rotor](rotor.md#rotor)

### Enigma.startposCheck

[[find in source code]](blob/master/Enigma/enigma.py#L260)

```python
@staticmethod
def startposCheck(start_pos: Union[(MutableSequence, tuple)]) -> None:
```

Checks for the types of values in the start position.
