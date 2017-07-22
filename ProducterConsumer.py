import queue
import random
import threading
import time

"""
运行代码
Utils.printmulti("生产者消费者")
pc = ProducterConsumer()
pc.start(500, 200)
"""


class ProducterConsumer:
    def __init__(self):
        self.s = Storage()

    def addProducter(self):
        Producter(self.s, "线程0").start()

    def addConsumer(self):
        Consumer(self.s, "线程0").start()

    def start(self, pCount=1, cCount=1):
        for i in range(pCount):
            Producter("生产线程" + str(i), self.s).start()
        time.sleep(3)
        for j in range(cCount):
            Consumer("消费线程" + str(j), self.s).start()


class Producter:
    def __init__(self, name, s):
        # self.speed = 2  # 2秒产出一个商品
        self.speed = random.randrange(3)
        self.s = s
        self.name = name

    def start(self):
        thread = MyThread(self.name, self.s, 0, self.speed)
        thread.start()


class Consumer:
    def __init__(self, name, s):
        self.s = s
        # self.speed = 1  # 1秒消费一个产品
        self.speed = random.randrange(2)
        self.name = name

    def start(self):
        thread = MyThread(self.name, self.s, 1, self.speed)
        thread.start()


class Storage:
    def __init__(self):
        self.q = queue.Queue(1000)

    def add(self, p):
        self.q.put(p)

    def remove(self):
        return self.q.get()

    def size(self):
        return self.q.qsize()


class Product:
    id = 0

    def __init__(self, id):
        self.id = id

    def print(self):
        print("产品:", self.id)


class MyThread(threading.Thread):
    def __init__(self, name, s, types, times):
        # super(MyThread, self).__init__()
        # 也可以写成
        # threading.Thread.__init__(self)
        threading.Thread.__init__(self)
        self.s = s
        self.types = types
        self.times = times
        self.name = name

    def run(self):
        while 1:
            if self.types:  # 0:producter 1:consumer
                time.sleep(self.times)
                p = self.s.remove()
                print(self.name, "消費一個产品", "產品數量：" + str(self.s.size()))
            else:
                time.sleep(self.times)
                p = Product(1)
                self.s.add(p)
                print(self.name, "生产一个产品", "產品數量：" + str(self.s.size()))
