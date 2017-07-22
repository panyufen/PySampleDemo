import random


class SortSample:
    listArr = []

    def __init__(self, num):
        if num > 1:
            while len(self.listArr) < num:
                ri = random.randrange(0, num)
                if not self.listArr.count(ri):
                    self.listArr.append(ri)
        print("count:", len(self.listArr))
        print("data:", self.listArr)

    def getListData(self):
        return self.listArr

    def sortbubble(self, lists):
        """
        冒泡排序法
        比较相邻的元素。如果第一个比第二个大，就交换他们两个。  
        对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。  
        针对所有的元素重复以上的步骤，除了最后一个。  
        持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。  
        """
        size = len(lists)
        for i in range(size):
            for j in range(i + 1, size):
                if lists[i] > lists[j]:
                    temp = lists[i]
                    lists[i] = lists[j]
                    lists[j] = temp

    def sortquick(self, lists, start=0, end=0):
        """
        快速排序法
        选择一个基准元素,通常选择第一个元素或者最后一个元素,通过一趟扫描，将待排序列分成两部分,一部分比基准元素小,
        一部分大于等于基准元素,此时基准元素在其排好序后的正确位置,然后再用同样的方法递归地排序划分的两部分。
        """
        if start < end:
            partition = lists[start]
            i, j = start, end
            while i < j:
                while lists[i] < partition and i < end:
                    i += 1
                while lists[j] > partition and j > start:
                    j -= 1

                if i <= j:
                    temp = lists[i]
                    lists[i] = lists[j]
                    lists[j] = temp

            if i + 1 < end:
                self.sortquick(lists, i + 1, end)
            if j - 1 > start:
                self.sortquick(lists, start, j - 1)
        else:
            print("start end is invalid start={0:2d},end={1:2d}".format(start, end))

    def sortinsert(self, lists):
        """
        插入排序
        就是每一步都将一个待排数据按其大小插入到已经排序的数据中的适当位置，直到全部插入完毕。 
        """
        for i in range(1, len(lists)):
            temp = lists[i]
            j = i
            while j > 0 and lists[j - 1] > temp:
                lists[j] = lists[j - 1]
                j -= 1
            lists[j] = temp

    def sortselect(self, lists):
        """
        选择排序
        基本思想：在要排序的一组数中，选出最小的一个数与第一个位置的数交换；
        然后在剩下的数当中再找最小的与第二个位置的数交换，如此循环到倒数第二个数和最后一个数比较为止。
        """
        size = len(lists)
        for i in range(size):
            pos = i
            temp = lists[i]
            for j in range(i + 1, size):
                if temp > lists[j]:
                    temp = lists[j]
                    pos = j
            if lists[i] > temp:
                lists[pos] = lists[i]
                lists[i] = temp

    def sortshell(self,lists):
        """
        希尔排序
        算法先将要排序的一组数按某个增量d（n/2,n为要排序数的个数）分成若干组，每组中记录的下标相差d.
        对每组中全部元素进行直接插入排序，然后再用一个较小的增量（d/2）对它进行分组，在每组中再进行直接插入排序。
        当增量减到1时，进行直接插入排序后，排序完成。
        """
