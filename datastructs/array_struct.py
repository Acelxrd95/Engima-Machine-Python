import ctypes


class Array:
    def __init__(
        self,
        type: type,
        size: int = 1,
        values=None,
        *morevals,
    ):
        assert size > 0, "array size must be greater than 0"
        if values:
            if size < len(values) and size != 1:
                raise ValueError(
                    "array size must be equal to or larger than values inserted"
                )
            elif size == 1:
                size = len(values)
        self.size = size
        self.type = type
        PyArrayType = ctypes.py_object * size
        self.elements = PyArrayType()
        self.itemcount = 0
        self.count = 0
        for val in values:
            self.insert(val)
        for val in morevals:
            self.insert(val)

    def __len__(self):
        return self.size

    def __str__(self):
        x = "["
        for i in range(self.itemcount):
            if self.elements[i] is not None:
                x += str(self.elements[i])
                if i != self.itemcount - 1:
                    x += ","
        return x + "]"

    def __iter__(self) -> object:
        return iter(self.elements)

    def __next__(self) -> object:
        if self.count > self.itemcount:
            raise StopIteration
        else:
            self.count += 1
            return self.count - 1

    def __getitem__(self, i: int | slice | str):
        if type(i) is str:
            return self.index(i)
        elif type(i) is int:
            return self.elements[i]
        elif type(i) is slice:
            return self.elements[i]
            # return Array(self.type,len(self.elements[i]),self.elements[i])
        else:
            raise Exception(
                f"Array indices must be integers or slices, not {type(i).__name__}"
            ) from TypeError

    def __contains__(self, key):
        return key in self.elements

    def insert(self, item, index=-1):
        if self.size > self.itemcount:
            assert (
                type(item) == self.type
            ), f"value inserted must be of type {self.type}"
            if index == -1 or index >= self.size:
                self.elements[self.itemcount] = item
            else:
                for i in range(self.itemcount, index, -1):
                    self.elements[i] = self.elements[i - 1]
                self.elements[index] = item
            self.itemcount += 1
            return 0
        else:
            print("list is full")
            return 1

    def index(self, val):
        for i in range(self.itemcount):
            if self.elements[i] == val:
                return i
        else:
            return f"Value {val} doesn't exist in this array"

    def pop(self, index=-1):
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
        if direction == 1 or direction == -1:
            oldLi = (
                self.elements[shift * direction :] + self.elements[: shift * direction]
            )
            for i in range(len(oldLi)):
                self.elements[i] = oldLi[i]
        else:
            raise Exception("Invalid shift direction") from ValueError

    def extend(self, size):
        try:
            self.size += size
            oldelems = self.elements
            PyArrayType = ctypes.py_object * self.size
            self.elements = PyArrayType()
            self.itemcount = 0
            for elem in oldelems:
                self.insert(elem)
        except Exception:
            print(Exception)
            return 1
        finally:
            return 0


if __name__ == "__main__":
    # array1 = Array(str, 5)
    # array1.insert("salem")
    # array1.insert("ahmed")
    # array1.insert("mohamed", 1)
    # array1.insert("ibrahim", 0)
    # array1.insert("1", 12312324)
    # array1.insert("2", 12312324)
    # array1.extend(3)
    # array1.insert("3", 12312324)
    # array1.insert("4", 12312324)
    # array1.insert("5", 12312324)
    # array1.insert("6", 12312324)
    # print(array1)
    # print(array1.pop())
    # print(array1.pop(0))
    # print(array1)
    # print(array1.elements[0])
    array1 = Array(int, values=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    print(array1)
    array1.shift(3, 1)
    print(array1)
    array1.shift(3, -1)
    print(array1)
    print(type(array1))
    # print(array1)
