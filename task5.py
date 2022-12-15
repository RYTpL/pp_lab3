import os


class Iterator:
    def __init__(self, base: str, name: str, path: str) -> None:
        '''constructor'''
        self.path = path
        self.name = name
        self.names = []
        self.names = os.listdir(os.path.join(base, self.path, self.name))
        self.limit = 0
        self.counter = 0
        self.base = ""
        self.init(base, name, path)
        for i in self.names:
            if not ".jpg" in i:
                self.names.remove(i)
        self.limit = len(self.names)
        self.counter = 0

    def __next__(self) -> None:
        '''go to the next element of the list'''
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        else:
            self.counter = 0
            return self.names[self.counter]

    def clear(self) -> None:
        '''clears the pointer to the list of file names'''
        self.counter = 0

    def setName(self, name: str) -> None:
        '''changes the file name'''
        self.init(self.base, name, self.path)

    def getName(self) -> None:
        '''returns the file name'''
        print(self.name)

    def setPath(self, path: str) -> None:
        """sets the file path"""
        self.init(self.base, self.name, path)
