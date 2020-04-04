class FPyCompare:
    def __readFile(self, fileName):
        with open(fileName) as f:
            lines = f.read().splitlines()
        return lines

    def __writeFile(self, resultList, fileName):
        with open(fileName, "w") as outfile:
            outfile.write("\n".join(resultList))
        print(fileName + " completed!")

    def initializeList(self):
        fileNameOne = input("First File Name: ")
        self.listOne = set(self.__readFile(fileNameOne))
        fileNameTwo = input("Second File Name: ")
        self.listTwo = set(self.__readFile(fileNameTwo))

    def interset(self, printResult=True):
        intersect = list(self.listOne.intersection(self.listTwo))
        print(intersect) if printResult else self.__writeFile(intersect, "result_intersect.txt")

    def union(self, printResult=True):
        union = list(self.listOne.union(self.listTwo))
        print(union) if printResult else self.__writeFile(union, "result_union.txt")

    def differenceListOne(self, printResult=True):
        subtract = list(self.listOne.difference(self.listTwo))
        print(subtract) if printResult else self.__writeFile(subtract, "result_DifferenceOne.txt")

    def differenceListTwo(self, printResult=True):
        subtract = list(self.listTwo.difference(self.listOne))
        print(subtract) if printResult else self.__writeFile(subtract, "result_DifferenceTwo.txt")


fCompare = FPyCompare()

fCompare.initializeList()
fCompare.interset(False)
fCompare.union(False)
fCompare.differenceListOne(False)
fCompare.differenceListTwo(False)
