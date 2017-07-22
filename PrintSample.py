from DataTypeSample import DataTypeSample


class PrintSample:
    dataType = DataTypeSample()

    def printSample(self):
        print("")
        print("print(string):", self.dataType.string)
        print("print(number):", self.dataType.number)
        print("print(tup):", self.dataType.tup)
        print("print(array):", self.dataType.array)
        print("print(dict):", self.dataType.dict)

        print("%s %s %d %d" % self.dataType.tup)
