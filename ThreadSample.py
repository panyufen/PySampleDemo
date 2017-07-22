import threading
import time


class ThreadSample:
    # 为线程定义一个函数
    @staticmethod
    def printTime( threadName, delay):
        count = 0
        while count < 5:
            time.sleep(delay)
            count += 1
            print("%s: %s" % (threadName, time.ctime(time.time())))


exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("开始线程：" + self.name)
        self.printTime(self.name, self.counter, 5)
        print("退出线程：" + self.name)

    def printTime(self, threadName, delay, counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1

# print("threading.Thread 使用==========================================================")
# # 创建新线程
# thread1 = MyThread(1, "Thread-10", 1)
# thread2 = MyThread(2, "Thread-20", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print("退出主线程")

# lock = _thread.allocate_lock()  # 创建一个琐对象
#
# count = 0
#
# def threadTest():
#     global count, lock
#     lock.acquire()  # 获取琐
#
#     for i in range(10000):
#         print(count)
#         count += 1
#
#     lock.release()  # 释放琐
#
# for i in range(10):
#     _thread.start_new_thread(threadTest, ())
#     print("index " + str(i))
# time.sleep(3)
# print(count)
