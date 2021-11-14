<!-- @format -->

# Utils

> Auto-generated documentation for [Enigma.utils](blob/master/Enigma/utils.py) module.

-   [Enigma machine](..\README.md#enigma-machine-python) / [Modules](..\MODULES.md#enigma-machine-modules) / [Enigma](index.md#enigma) / Utils
    -   [c2n](#c2n)
    -   [isroman](#isroman)
    -   [isspecial](#isspecial)
    -   [n2c](#n2c)
    -   [num2word](#num2word)
    -   [rmspecial](#rmspecial)
    -   [roman2den](#roman2den)
    -   [sp2norm](#sp2norm)
    -   [transformsp](#transformsp)
    -   [up2low](#up2low)
    -   [whsp2norm](#whsp2norm)

## c2n

[[find in source code]](blob/master/Enigma/utils.py#L68)

```python
def c2n(char: str) -> int:
```

Converts Number to a character

## isroman

[[find in source code]](blob/master/Enigma/utils.py#L58)

```python
def isroman(roman: str) -> bool:
```

Checks whether the given string is a valid Roman number.

## isspecial

[[find in source code]](blob/master/Enigma/utils.py#L94)

```python
def isspecial(char: str) -> bool:
```

Checks whether the given character is an allowed special characters

## n2c

[[find in source code]](blob/master/Enigma/utils.py#L80)

```python
def n2c(num: int, upper: bool = True) -> str:
```

Converts Number to a character

## num2word

[[find in source code]](blob/master/Enigma/utils.py#L125)

```python
def num2word(number: str, setting: int) -> str:
```

Converts a number to its word representation

## rmspecial

[[find in source code]](blob/master/Enigma/utils.py#L178)

```python
def rmspecial(word: str) -> str:
```

Parses a word and replaces special character representation with their corresponding symbol

## roman2den

[[find in source code]](blob/master/Enigma/utils.py#L42)

```python
def roman2den(roman: str) -> int:
```

Convers roman numbers to denary numbers.

## sp2norm

[[find in source code]](blob/master/Enigma/utils.py#L101)

```python
def sp2norm(char: str, sp_setting: int) -> str:
```

Replaces special characters with normal characters to allow encryption

## transformsp

[[find in source code]](blob/master/Enigma/utils.py#L149)

```python
def transformsp(char: str, settings: Array) -> str:
```

Parses and transforms special characters to normal characters to allow encryption

#### See also

-   [Array](datastructs.md#array)

## up2low

[[find in source code]](blob/master/Enigma/utils.py#L140)

```python
def up2low(char: str, setting: int) -> str:
```

Adds a special character to the character string in order to allow encryption

## whsp2norm

[[find in source code]](blob/master/Enigma/utils.py#L113)

```python
def whsp2norm(char: str, whitesp_setting: int) -> str:
```

Replaces white spaces with normal characters to allow encryption
