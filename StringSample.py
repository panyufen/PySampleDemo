from DataTypeSample import DataTypeSample


class StringSample:
    dataType = DataTypeSample()

    def reprSample(self):
        print("=========== ")
        print("repr(string):", repr(self.dataType.string))
        print("repr(number):", repr(self.dataType.number))
        print("repr(tup):", repr(self.dataType.tup))
        print("repr(array):", repr(self.dataType.array))
        print("repr(dict):", repr(self.dataType.dict))

    def strSample(self):
        print("")
        print("str(string):", str(self.dataType.string))
        print("str(number):", str(self.dataType.number))
        print("str(tup):", str(self.dataType.tup))
        print("str(array):", str(self.dataType.array))
        print("str(dict):", str(self.dataType.dict))

    def formatSample(self):
        print("")
        print("A:{0} B:{1} C:{2} D:{3} ".format("a", "b", "c", "d"))
        print("A:{a} B:{b} C:{c} D:{d}".format(a=1, b=2, c=3, d=4))
        print("A:{0[0]} B:{0[1]} C:{0[2]} D:{0[3]} ".format(self.dataType.tup))
        print('A:{0[A]:d} B:{0[B]:d} C:{0[C]:d} E:{0[E]:s}'.format(self.dataType.dict))
        print('A:{A:d} B:{B:d} C:{C:d} E:{E:s}'.format(**self.dataType.dict))

        print("A={0} B={1} C={2} a={3} b={4} c={5}".format("A", "B", "C", "a", "b", "c"))

        # 旧版本格式化字符串 新版本str.format代替之
        print('常量 PI 的值近似为：%5.3f abc\n' % 3.1234567)

    def defaultSample(self):
        print("")
        multiStr = """这里是一个多行的字符串
        这里是一个多行的字符串
        这里是一个多行的字符串
        这里是一个多行的字符串"""
        print(multiStr)

        print("a".ljust(5), end="===\n")
        print("a".ljust(5, "-"), end="===\n")
        print("a".rjust(5), end="===\n")
        print("a".rjust(5, "-"), end="===\n")
        print("a".center(5, ), end="===\n")
        print("a".center(5, "-"), end="===\n")

        print("")
        print("====================    orign str:", self.dataType.string, end="   ==========================\n")
        print("split str[0:6]:", self.dataType.string[0:6] + "aaa")
        print("split str[:6]:", self.dataType.string[:6] + "aaa")
        print("DC in str:", "DC" in self.dataType.string)
        print("capitalize str:", self.dataType.string.capitalize())
        print("count str:", self.dataType.string.count("a", 0, 10))
        print("encode str:", self.dataType.string.encode("utf-8"))
        print("endwith str:", self.dataType.string.endswith("g"), self.dataType.string.endswith("g", 0, 7))
        print("find str:", self.dataType.string.find("A"), self.dataType.string.find("Z"))
        # 如果字符串至少有一个字符并且所有字符都是字母则返回 True, 否则返回 False
        print("isalpha str:", "aaa".isalpha(), "222".isalpha(), ",".isalpha(), "".isalpha())
        # 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True,否则返回 False
        print("isalnum str:", "aaa".isalnum(), "222".isalnum(), ",".isalnum(), "".isalpha())
        print("isdigit str:", self.dataType.string.isdigit())
        # 必须字符串序列
        print("join str:", "-".join(self.dataType.array[0:4]))
        print("strip str:", self.dataType.string.strip("a"))
        print("split str:", self.dataType.string.split("d"))
        print("translate str:", self.dataType.string.translate(str.maketrans({"A": "1", "B": "2", "C": "3"})))
