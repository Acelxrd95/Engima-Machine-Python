from typing import Any, Mapping


class Map:
    """
    Custom map data structure

    Args:
        values (:obj:`dict`): values passed to the map. Defaults to None.
    """

    def __init__(self, values: Mapping = {}) -> None:
        self._keys: list = []
        self._values: list = []
        if not isinstance(values, Mapping):
            raise TypeError("Values must be an instance of Mapping")
        for key, val in values.items():
            if key in self._keys:
                # Replace key if it exists in the map
                self.update({key: val})
            else:
                self._keys.append(key)
                self._values.append(val)

    def __len__(self) -> int:
        """
        Returns the length of the map
        """
        return len(self._keys)

    def __repr__(self) -> str:
        """
        Returns the string representation of the map
        """
        retstr: str = ""
        for i in range(len(self)):
            if i + 1 == len(self):
                retstr += f"{self._keys[i]}|{type(self._keys[i]).__name__} : {self._values[i]}|{type(self._values[i]).__name__}"
            else:
                retstr += f"{self._keys[i]}|{type(self._keys[i]).__name__} : {self._values[i]}|{type(self._values[i]).__name__} , "
        return "{" + retstr + "}"

    def __str__(self) -> str:
        """
        Returns the string representation of the map
        """
        retstr: str = "Keys\t|Values"
        retstr += "\n----------------"
        for i in range(len(self)):
            retstr += (
                "\n"
                + str(self._keys[i])
                + "  "
                + str(type(self._keys[i]).__name__)
                + "\t|"
                + str(self._values[i])
                + "  "
                + str(type(self._values[i]).__name__)
            )
        return retstr

    def __getitem__(self, key: Any) -> Any:
        """
        Returns value corresponding to the specified key.
        """
        if key not in self._keys:
            raise KeyError(f"{key} is not in the map")
        key_i: int = self._keys.index(key)
        return self._values[key_i]

    def __contains__(self, key):
        """
        Returns if the specified key is in the map
        """
        return key in self._keys

    def update(self, item: Mapping = {}) -> None:
        """
        Adds a new item to the map
        """
        if not isinstance(item, Mapping):
            raise TypeError("Item must be an instance of Mapping")
        for key, val in item.items():
            if key in self._keys:
                key_i: int = self._keys.index(key)
                self._values[key_i] = val
            else:
                self._keys.append(key)
                self._values.append(val)

    def pop(self, key: Any) -> Any:
        """
        Removes and returns an element from the map with the specified key.
        """
        key_i: int = self._keys.index(key)
        self._keys.pop(key_i)
        return self._values.pop(key_i)

    def items(self) -> list[tuple]:
        """
        Returns a list of all items in the map
        """
        retlist: list = []
        for key in self._keys:
            retlist.append((key, self[key]))
        return retlist

    def values(self) -> list:
        """
        Returns a list of all values in the map
        """
        return self._values

    def keys(self) -> list:
        """
        Returns a list of all keys in the map
        """
        return self._keys


if __name__ == "__main__":
    x = Map({3: 4})
    x[4]
