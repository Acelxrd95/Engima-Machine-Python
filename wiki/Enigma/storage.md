# Storage

> Auto-generated documentation for [Enigma.storage](blob/master/Enigma/storage.py) module.

- [Enigma machine](..\README.md#enigma-machine-index) / [Modules](..\MODULES.md#enigma-machine-modules) / [Enigma](index.md#enigma) / Storage
    - [addCustomReflector](#addcustomreflector)
    - [addCustomRotor](#addcustomrotor)

## addCustomReflector

[[find in source code]](blob/master/Enigma/storage.py#L63)

```python
def addCustomReflector(
    reflector_id: str,
    key: str,
    allowdupes: bool = False,
) -> None:
```

Allows the user to add custom reflectors with custom keys

## addCustomRotor

[[find in source code]](blob/master/Enigma/storage.py#L30)

```python
def addCustomRotor(
    rotor_id: str,
    key: str,
    notch: tuple,
    allowdupes: bool = False,
) -> None:
```

Allows the user to add custom rotors with custom keys and notches
