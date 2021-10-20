class Map:
    def __init__(self, values: dict = {}) -> None:
        self.keys = [k for k in values.keys()]
        self.values = [val for val in values.values()]

    def __len__(self) -> int:
        return len(self.keys)

    def __repr__(self) -> str:
        retstr:str=""
        for i in range(len(self)):
            retstr += f"{}"
        return f"{}"


fk = Map({"f": "a7a", "fk": "aaaaaa"})
print(fk)
