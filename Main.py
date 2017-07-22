import os
import random

import time

import sys

import _thread

from ArraySample import ArraySample
from ClassSample import ClassSample
from CommonUtils import CommonUtils as Utils
from DateSample import DateSample
from FileSample import FileSample
from JsonSample import JsonSample
from PickleSample import PickleSample
from PrintSample import PrintSample
from ProducterConsumer import ProducterConsumer
from RegexpSample import RegexpSample
from SortSample import SortSample
from StringSample import StringSample

# Utils.printmulti("基本语法")
# StringSample.print()
#
# Utils.printmulti("文件操作")
# fileSample = FileSample()
# fileSample.readByWhile()
# fileSample.readByFor()
# fileSample.readByContent()
# fileSample.print()
# fileSample.writeAdd()
#
# Utils.printmulti("pickle 使用")
# PickleSample.print()
#
# Utils.printmulti("面向对象")
# ClassSample.print()
#
# Utils.printmulti("Date 使用")
# DateSample.print()
#
# Utils.printmulti("json 序列化 反序列化")
# jsonSample = JsonSample()
# jsonSample.printStr()
# print("")
# jsonSample.printObject()
#
# print("")
# jsonSample.writeJsonInFile()
# jsonSample.readJsonFromFile()
#
# Utils.printmulti("正则使用")
# regexpSample = RegexpSample()
# regexpSample.match()
# regexpSample.split()
# regexpSample.findall()

#################  排序测试  ###################
# sys.setrecursionlimit(10000000)
# startTime0 = time.time()
# sortSample = SortSample(5000)
# endtime0 = time.time()
# print("随机数组生成：",endtime0-startTime0)
# list1 = sortSample.getListData().copy()
# print(list1)
# # 冒泡排序
# sortSample.sortbubble(list1)
# print(list1)
# endTime1 = time.time()
# speedTime1 = endTime1 - endtime0
# print("冒泡排序:", speedTime1)
#
# list2 = sortSample.getListData().copy()
# print(list2)
# # 快速排序
# sortSample.sortquick(list2, 0, len(list2) - 1)
# print(list2)
# endTime2 = time.time()
# print("快速排序:", endTime2 - endTime1)
#
# list3 = sortSample.getListData().copy()
# print(list3)
# # 插入排序
# sortSample.sortinsert(list3)
# print(list3)
# endTime3 = time.time()
# print("插入排序:", endTime3 - endTime2)
#
# list4 = sortSample.getListData().copy()
# print(list4)
# # 简单选择排序
# sortSample.sortselect(list4)
# print(list4)
# endTime4 = time.time()
# print("选择排序", endTime4 - endTime3)


# Utils.printmulti("生产者消费者")
# pc = ProducterConsumer()
# pc.start(101, 100)


################### 模拟手机点击 #####################
# str = "adb shell input tap 270 670"
# str1 = "adb shell input tap 370 1250"
# print("start")
#
# for x in range(int(60 / 5)):
#     os.popen(str)
#     time.sleep(3)
#     os.popen(str1)
#     time.sleep(2)
#     print("print", x)

#####################  数组 元组 字典  ########################
# arraySample = ArraySample()
# arraySample.print()

####################### print输出 ##############################
# printSample = PrintSample()
# printSample.printSample()

####################### 字符串处理 格式化 ##############################
stringSample = StringSample()
# stringSample.reprSample()
# stringSample.strSample()
# stringSample.formatSample()
stringSample.defaultSample()



