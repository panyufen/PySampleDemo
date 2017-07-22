class Site:
    def __init__(self, name, url):
        self.name = name
        self.__url = url

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def foo(self):
        print('这是公共方法')
        self.__foo()

    @staticmethod
    def __foo():
        print("这个是私有方法")


# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


# 重载（__add__ 类专有方法重载）
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

class ClassSample:
    @staticmethod
    def print():
        x = Site('菜鸟教程', 'http://www.runoob.com')
        x.who()
        x.foo()
        print("")

        test = Sample("Tim", 25, 80, 4, "Python")
        test.speak()
        print("")

        v1 = Vector(2, 10)
        v2 = Vector(5, -2)
        print(v1)
        print(v2)
        print(v1 + v2)
