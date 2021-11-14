<!-- @format -->

# Datastructs

> Auto-generated documentation for [Enigma.datastructs](blob/master/Enigma/datastructs.py) module.

-   [Enigma machine](..\README.md#enigma-machine-python) / [Modules](..\MODULES.md#enigma-machine-modules) / [Enigma](index.md#enigma) / Datastructs
    -   [Array](#array)
        -   [Array().\_\_contains\_\_](#array__contains__)
        -   [Array().\_\_eq\_\_](#array__eq__)
        -   [Array().\_\_getitem\_\_](#array__getitem__)
        -   [Array().\_\_len\_\_](#array__len__)
        -   [Array().\_\_next\_\_](#array__next__)
        -   [Array().\_\_str\_\_](#array__str__)
        -   [Array().extend](#arrayextend)
        -   [Array().index](#arrayindex)
        -   [Array().insert](#arrayinsert)
        -   [Array().isempty](#arrayisempty)
        -   [Array().pop](#arraypop)
        -   [Array().shift](#arrayshift)
    -   [Map](#map)
        -   [Map().\_\_contains\_\_](#map__contains__)
        -   [Map().\_\_getitem\_\_](#map__getitem__)
        -   [Map().\_\_len\_\_](#map__len__)
        -   [Map().\_\_repr\_\_](#map__repr__)
        -   [Map().\_\_str\_\_](#map__str__)
        -   [Map().items](#mapitems)
        -   [Map().keys](#mapkeys)
        -   [Map().pop](#mappop)
        -   [Map().update](#mapupdate)
        -   [Map().values](#mapvalues)

## Array

[[find in source code]](blob/master/Enigma/datastructs.py#L5)

```python
class Array():
    def __init__(
        artype: type,
        size: int = 1,
        values: Optional[Union[(MutableSequence, tuple, str)]] = None,
        *morevals,
    ):
```

Custom array data structure

#### Arguments

-   `artype` _:obj:`type`_ - refers to the type of the elements in the array
-   `size` _:obj:`int`_ - the number of elements in the array. Defaults to 1
-   `values` _:obj:`MutableSequence`_ - values passed to the array. Defaults to None.

### Array().\_\_contains\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L110)

```python
def __contains__(key: Any) -> bool:
```

Returns whether the specified element exists in the array.

### Array().\_\_eq\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L81)

```python
def __eq__(other: Any) -> bool:
```

Returns a boolean indicating whether two objects are equivalent or not

### Array().\_\_getitem\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L89)

```python
def __getitem__(i: Union[(int, slice)]) -> Any:
```

Returns object at given position

### Array().\_\_len\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L53)

```python
def __len__() -> int:
```

Returns the length of the array.

### Array().\_\_next\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L71)

```python
def __next__() -> Any:
```

Returns object next iterator item

### Array().\_\_str\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L59)

```python
def __str__() -> str:
```

Returns the object's string representation.

### Array().extend

[[find in source code]](blob/master/Enigma/datastructs.py#L178)

```python
def extend(size: int) -> None:
```

Increase the size of the array with the given size.

### Array().index

[[find in source code]](blob/master/Enigma/datastructs.py#L137)

```python
def index(val: Any) -> int:
```

Return the index of value in the array.

### Array().insert

[[find in source code]](blob/master/Enigma/datastructs.py#L116)

```python
def insert(item: Any, index: int = -1) -> None:
```

Inserts an item into the array at given position. Position defaults to the end of the array.

### Array().isempty

[[find in source code]](blob/master/Enigma/datastructs.py#L195)

```python
def isempty() -> bool:
```

Checks if the array is empty

### Array().pop

[[find in source code]](blob/master/Enigma/datastructs.py#L147)

```python
def pop(index: int = -1) -> Any:
```

Removes and returns an element from the array at the specified index. Defaults to the last element

### Array().shift

[[find in source code]](blob/master/Enigma/datastructs.py#L163)

```python
def shift(shift: int, direction: int = 1) -> None:
```

Shift the elements in the array according to given shift and direction. Direction defaults to forward

## Map

[[find in source code]](blob/master/Enigma/datastructs.py#L204)

```python
class Map():
    def __init__(values: Mapping = None) -> None:
```

Custom map data structure

#### Arguments

-   `values` _:obj:`dict`_ - values passed to the map. Defaults to None.

### Map().\_\_contains\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L273)

```python
def __contains__(key):
```

Returns if the specified key is in the map

### Map().\_\_getitem\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L264)

```python
def __getitem__(key: Any) -> Any:
```

Returns value corresponding to the specified key.

### Map().\_\_len\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L227)

```python
def __len__() -> int:
```

Returns the length of the map

### Map().\_\_repr\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L233)

```python
def __repr__() -> str:
```

Returns the string representation of the map

### Map().\_\_str\_\_

[[find in source code]](blob/master/Enigma/datastructs.py#L245)

```python
def __str__() -> str:
```

Returns the string representation of the map

### Map().items

[[find in source code]](blob/master/Enigma/datastructs.py#L303)

```python
def items() -> list[tuple]:
```

Returns a list of all items in the map

### Map().keys

[[find in source code]](blob/master/Enigma/datastructs.py#L318)

```python
def keys() -> list:
```

Returns a list of all keys in the map

### Map().pop

[[find in source code]](blob/master/Enigma/datastructs.py#L295)

```python
def pop(key: Any) -> Any:
```

Removes and returns an element from the map with the specified key.

### Map().update

[[find in source code]](blob/master/Enigma/datastructs.py#L279)

```python
def update(item: Mapping = None) -> None:
```

Adds a new item to the map

### Map().values

[[find in source code]](blob/master/Enigma/datastructs.py#L312)

```python
def values() -> list:
```

Returns a list of all values in the map
