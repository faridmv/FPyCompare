class FPyCompare:
    def __readFile(self, fileName):
        with open(fileName) as f:
            lines = f.read().splitlines()
        return lines

    def initializeList(self):
        fileNameOne = input("First File Name: ")
        self.listOne = set(self.__readFile(fileNameOne))
        fileNameTwo = input("Second File Name: ")
        self.listTwo = set(self.__readFile(fileNameTwo))

    def interset(self):
        intersect = list(self.listOne.intersection(self.listTwo))
        print(intersect)

    def union(self):
        union = list(self.listOne.union(self.listTwo))
        print(union)

    def differenceListOne(self):
        subtract = list(self.listOne.difference(self.listTwo))
        print(subtract)

    def differenceListTwo(self):
        subtract = list(self.listTwo.difference(self.listOne))
        print(subtract)


fCompare = FPyCompare()

fCompare.initializeList()
fCompare.interset()
fCompare.union()
fCompare.differenceListOne()
fCompare.differenceListTwo()
