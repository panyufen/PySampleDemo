class ArraySample:
    def print(self):
        # 元组
        otm = ("a", 2, 3, "c")
        # 字典 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
        dict = {"a": 111, "234": 222, 234: 333, otm: 444}
        print("dict:", dict)
        print("dict[\"234\"]:", dict["234"])
        print('dict["234"]:', dict["234"])
        print("dict[234]:", dict[234])
        print("dict[otm]:", dict[otm])
        print("str(dict):", str(dict))
        print('"234" in dict:', "234" in dict)
        print("dict.items():", dict.items())
        print("dict.keys():", dict.keys())
        print("dict.values():", dict.values())

        arr = ["a", 1, "b", 2, "c", 3, "d", 4]
        it = iter(arr)
        print("arr value :", end=" ")
        for x in it:
            print(x, end=" ")

        table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
        for name, number in table.items():
            print('{0:10} ==> {1:10d}'.format(name, number))
        print("")
