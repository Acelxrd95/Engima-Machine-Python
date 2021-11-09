import ctypes
from typing import Any, Iterable, MutableSequence, NoReturn, Optional, Union


class Array:
    """
    Custom array data structure

    Args:
        artype (:obj:`type`): refers to the type of the elements in the array
        size (:obj:`int`): the number of elements in the array. Defaults to 1
        values (:obj:`MutableSequence`): values passed to the array. Defaults to None.
    """

    def __init__(
        self,
        artype: type,
        size: int = 1,
        values: Optional[Union[MutableSequence, tuple, str]] = None,
        *morevals,
    ):

        if not isinstance(artype, type):
            raise TypeError("Array type must be type object")
        if not isinstance(size, int):
            raise TypeError("Array size must be an integer")
        if not size > 0:
            raise ValueError("Array size must be greater than 0")

        if values:
            if not hasattr(values, "__iter__"):
                raise TypeError(f"Array values of type {type(values)} is not iterable")
            if size < len(values) and size != 1:
                raise ValueError(
                    "array size must be equal to or larger than values inserted"
                )
            elif size == 1:
                size = len(values)

        self.size: int = size
        self.type: type = artype
        PyArrayType = ctypes.py_object * size
        self.elements = PyArrayType()
        self.itemcount: int = 0
        self.count: int = 0
        if values == None:
            values = []
        for val in values:
            self.insert(val)
        for val in morevals:
            self.insert(val)

    def __len__(self) -> int:
        """
        Returns the length of the array.
        """
        return self.size

    def __str__(self) -> str:
        """
        Returns the object's string representation.
        """
        x = "["
        for i in range(self.itemcount):
            if self.elements[i] is not None:
                x += str(self.elements[i])
                if i != self.itemcount - 1:
                    x += ","
        return x + "]"

    def __next__(self) -> Any:
        """
        Returns object next iterator item
        """
        self.count += 1
        if self.count > self.itemcount:
            self.count = 0
            raise StopIteration
        else:
            return self.count - 1

    def __eq__(self, other: Any) -> bool:
        """
        Returns a boolean indicating whether two objects are equivalent or not
        """
        if isinstance(other, list):
            return list(self.elements) == other
        return self.elements == other

    def __getitem__(self, i: Union[int, slice]) -> Any:
        """
        Returns object at given position
        """
        if type(i) is int:
            return self.elements[i]
        elif type(i) is slice:
            return self.elements[i]
            # return Array(self.type,len(self.elements[i]),self.elements[i])
        else:
            raise TypeError(
                f"Array indices must be integers or slices, not {type(i).__name__}"
            )

    def __setitem__(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if type(value) != self.type:
            raise TypeError(
                f"Value inserted must be of type {self.type} not {type(value)}"
            )
        self.elements[index] = value

    def __contains__(self, key: Any) -> bool:
        """
        Returns whether the specified element exists in the array.
        """
        return key in self.elements

    def insert(self, item: Any, index: int = -1) -> None:
        """
        Inserts an item into the array at given position. Position defaults to the end of the array.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if self.size > self.itemcount:
            if type(item) != self.type:
                raise TypeError(
                    f"Value inserted must be of type {self.type} not {type(item)}"
                )
            if index == -1 or index >= self.size:
                self.elements[self.itemcount] = item
            else:
                for i in range(self.itemcount, index, -1):
                    self.elements[i] = self.elements[i - 1]
                self.elements[index] = item
            self.itemcount += 1
        else:
            raise Exception("Array is full")

    def index(self, val: Any) -> int:
        """
        Return the index of value in the array.
        """
        if val in self.elements:
            for i in range(self.itemcount):
                if self.elements[i] == val:
                    return i
        raise KeyError(f"Value {val} doesn't exist in this array")

    def pop(self, index: int = -1) -> Any:
        """
        Removes and returns an element from the array at the specified index. Defaults to the last element
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")
        if index == -1 or index >= self.size:
            returnval = self.elements[self.itemcount - 1]
        else:
            returnval = self.elements[index]
            for i in range(index, self.itemcount):
                self.elements[i] = self.elements[i + 1]
                pass
        self.itemcount -= 1
        self.elements[self.itemcount] = None
        return returnval

    def shift(self, shift: int, direction: int = 1) -> None:
        """
        Shift the elements in the array according to given shift and direction. Direction defaults to forward
        """
        if not isinstance(shift, int):
            raise TypeError("Shift value must be an integer")
        if direction in (1, -1):
            oldLi = (
                self.elements[shift * direction :] + self.elements[: shift * direction]
            )
            for i in range(len(oldLi)):
                self.elements[i] = oldLi[i]
        else:
            raise ValueError("Invalid shift direction")

    def extend(self, size: int) -> None:
        """
        Increase the size of the array with the given size.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        try:
            self.size += size
            oldelems = self.elements
            PyArrayType = ctypes.py_object * self.size
            self.elements = PyArrayType()
            self.itemcount = 0
            for elem in oldelems:
                self.insert(elem)
        except Exception as e:
            raise e

    def isempty(self) -> bool:
        """
        Checks if the array is empty
        """
        if self.itemcount == 0:
            return True
        return False
