<!-- @format -->

# Rotor

> Auto-generated documentation for [Enigma.rotor](blob/master/Enigma/rotor.py) module.

-   [Enigma machine](..\README.md#enigma-machine-index) / [Modules](..\MODULES.md#enigma-machine-modules) / [Enigma](index.md#enigma) / Rotor
    -   [Rotor](#rotor)
        -   [Rotor().\_\_repr\_\_](#rotor__repr__)
        -   [Rotor().abs_pos](#rotorabs_pos)
        -   [Rotor().changeRingsett](#rotorchangeringsett)
        -   [Rotor().check_notch](#rotorcheck_notch)
        -   [Rotor().reset](#rotorreset)
        -   [Rotor().shiftPosition](#rotorshiftposition)

## Rotor

[[find in source code]](blob/master/Enigma/rotor.py#L6)

```python
class Rotor():
    def __init__(tyre: str, notch: Union[(str, tuple[(str, ...)])]) -> None:
```

The Enigma rotors consist of a couple of settings and properties.

#### Attributes

-   `tyre` _str_: refers to the alphabet tyre used to encrypt the letter entered.
-   `notch` _Union[str, tuple[str, ...]]_: refers to the notch at which the next rotor in order turns.
-   `curr_pos` _int_: refers to the current position of the rotor.
-   `ring_offset` _int_: refers to the offset of the ring wiring.
-   `abs_pos` _int_: refers to the original absolute position of the rotor without the offset.
-   `check_notch` _bool_: checks whether the rotor is currently on the notch or not.

### Rotor().\_\_repr\_\_

[[find in source code]](blob/master/Enigma/rotor.py#L38)

```python
def __repr__() -> str:
```

Returns the object's string representation.

### Rotor().abs_pos

[[find in source code]](blob/master/Enigma/rotor.py#L27)

```python
@property
def abs_pos() -> int:
```

### Rotor().changeRingsett

[[find in source code]](blob/master/Enigma/rotor.py#L58)

```python
def changeRingsett(pos: int) -> None:
```

Changes the ring offset setting

### Rotor().check_notch

[[find in source code]](blob/master/Enigma/rotor.py#L31)

```python
@property
def check_notch() -> bool:
```

### Rotor().reset

[[find in source code]](blob/master/Enigma/rotor.py#L51)

```python
def reset():
```

Reset the rotor to its initial position.

### Rotor().shiftPosition

[[find in source code]](blob/master/Enigma/rotor.py#L67)

```python
def shiftPosition(pos: int, dirct: int = 1) -> None:
```

Shift the rotor position according `pos` for number of steps and the `dirct` for
the direction of the shift
