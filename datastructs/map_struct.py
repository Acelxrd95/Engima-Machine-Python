class Map:
    def __init__(self, values: dict = {}) -> None:
        self._keys: list = []
        self._values: list = []
        for key, val in values.items():
            if key in self._keys:
                """
                Replace key if it exists in the map
                """
                self.update({key: val})
            else:
                self._keys.append(key)
                self._values.append(val)

    def __len__(self) -> int:
        return len(self._keys)

    def __repr__(self) -> str:
        retstr: str = ""
        for i in range(len(self)):
            if i + 1 == len(self):
                retstr += f"{self._keys[i]}|{type(self._keys[i]).__name__} : {self._values[i]}|{type(self._values[i]).__name__}"
            else:
                retstr += f"{self._keys[i]}|{type(self._keys[i]).__name__} : {self._values[i]}|{type(self._values[i]).__name__} , "
        return "{" + retstr + "}"

    def __str__(self) -> str:
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

    def __getitem__(self, key):
        try:
            key_i: int = self._keys.index(key)
            return self._values[key_i]
        except:
            raise KeyError(key) from None

    def __contains__(self, key):
        return key in self._keys

    def update(self, item: dict = {}) -> None:
        for key, val in item.items():
            if key in self._keys:
                key_i: int = self._keys.index(key)
                self._values[key_i] = val
            else:
                self._keys.append(key)
                self._values.append(val)

    def pop(self, key):
        key_i: int = self._keys.index(key)
        self._keys.pop(key_i)
        return self._values.pop(key_i)

    def items(self) -> list[tuple]:
        retlist: list = []
        for key in self._keys:
            retlist.append((key, self[key]))
        return retlist

    def values(self) -> list:
        return self._values

    def keys(self) -> list:
        return self._keys


if __name__ == "__main__":
    fs = Map({"f": "aaa", 3: 3, "fs": "aaaaaa", 1: 54})
    fs.update({3: "55"})
    print(fs)
    print(repr(fs))
    print(fs[3])
    f = {"3": "afa", "fs": "aaaa"}
    print(fs.pop("f"))
    print(fs)
    # print(fs.items())
    print(fs[344])
