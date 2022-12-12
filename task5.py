import csv
import os


class Iterator:
    def __init__(self, base: str, name: str, path: str):
        self.path = ""
        self.name = ""
        self.names = []
        self.limit = 0
        self.counter = 0
        self.base = ""
        self.init(base, name, path)

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            self.counter = 0
            return self.names[self.counter]

    def init(self, base: str, name: str, path: str) -> None:
        if not "dataset" in path:
            raise ("error")
        self.path = path
        self.name = name
        self.names = os.listdir(os.path.join(base, self.path, self.name))

        for i in self.names:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def clear(self) -> None:
        self.counter = 0

    def setName(self, name: str) -> None:
        self.init(self.base, name, self.path)

    def getName(self) -> None:
        print(self.name)

    def setPath(self, path: str) -> None:
        self.init(self.base, self.name, path)
