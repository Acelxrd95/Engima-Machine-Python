# Utils

> Auto-generated documentation for [Enigma.utils](blob/master/Enigma/utils.py) module.

- [Enigma machine](..\README.md#enigma-machine-index) / [Modules](..\MODULES.md#enigma-machine-modules) / [Enigma](index.md#enigma) / Utils
    - [c2n](#c2n)
    - [isroman](#isroman)
    - [isspecial](#isspecial)
    - [n2c](#n2c)
    - [num2word](#num2word)
    - [rmspecial](#rmspecial)
    - [roman2den](#roman2den)
    - [sp2norm](#sp2norm)
    - [transformsp](#transformsp)
    - [up2low](#up2low)

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

[[find in source code]](blob/master/Enigma/utils.py#L121)

```python
def num2word(number: str, setting: int) -> str:
```

Converts a number to its word representation

## rmspecial

[[find in source code]](blob/master/Enigma/utils.py#L166)

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

[[find in source code]](blob/master/Enigma/utils.py#L104)

```python
def sp2norm(char: str, sp_setting: int = 1, whitesp_setting: int = 1) -> str:
```

Replaces special characters with normal characters to allow encryption

## transformsp

[[find in source code]](blob/master/Enigma/utils.py#L145)

```python
def transformsp(
    char: str,
    settings: Array = Array(int, values=[1, 1, 1, 1]),
) -> str:
```

Parses and transforms special characters to normal characters to allow encryption

#### See also

- [Array](datastructs.md#array)

## up2low

[[find in source code]](blob/master/Enigma/utils.py#L136)

```python
def up2low(char: str, setting: int) -> str:
```

Adds a special character to the character string in order to allow encryption
