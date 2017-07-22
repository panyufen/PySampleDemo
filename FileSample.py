class FileSample:
    encoding = "utf-8"
    filePath = "./files/file.txt"
    fileContent = "今天天气真好\n做点什么事呢\n去外面走走吧"

    def __init__(self):
        fileW = open(self.filePath, "w", encoding=self.encoding)
        fileW.write(self.fileContent)
        fileW.close()

    def readByWhile(self):
        print("通过while逐行读取")
        fileR = open(self.filePath, "r", encoding=self.encoding)
        fileLine = fileR.readline()
        while fileLine:
            print(fileLine, end="")
            fileLine = fileR.readline()
        else:
            fileR.close()
            print("\n")

    def readByFor(self):
        print("通过for循环逐行输出")
        fileByFor = open(self.filePath, "r", encoding=self.encoding)
        for fl in fileByFor:
            print(fl, end="")
        else:
            fileByFor.close()
            print("\n")

    def readByContent(self):
        print("通过read 读取整个内容")
        fileRC = open(self.filePath, "r", encoding=self.encoding)
        fileContent = fileRC.read()
        print(fileContent + "\n")
        fileRC.close()

    def print(self):
        # 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
        fileRS = open(self.filePath, "rb+")
        fileRS.readline()
        print(fileRS.tell())
        if fileRS.seekable():
            fileRS.seek(-10, 1)
            print(fileRS.tell())

    def writeAdd(self):
        writeFile = open("./files/fileWrite.txt", "a+", encoding="utf-8")
        writeData = ['a', 'b', 'c', 'd']
        for wi in range(len(writeData)):
            writeData[wi] += " "
        writeData.append("\n")
        writeFile.writelines(writeData)
        writeFile.close()
