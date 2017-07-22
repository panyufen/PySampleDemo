import calendar
import time


class DateSample:
    @staticmethod
    def print():
        timeNow = time.time()
        print("now " + str(timeNow))
        localTime = time.localtime()
        print(repr(localTime))

        print("有参数localtime(): \n" + str(time.localtime(1455508609.34375)) + "\n")

        print("无参数localtime(): \n" + str(localTime.tm_year) + " " +
              str(localTime.tm_mon) + " " +
              str(localTime.tm_mday) + " " +
              str(localTime.tm_hour) + " " +
              str(localTime.tm_min) + " " +
              str(localTime.tm_sec) + "\n")

        print("%Y-%m-%d %H:%M:%S" + " -> " + time.strftime("%Y-%m-%d %H:%M:%S", localTime))
        print("%a %b %d %H:%M:%S %Y" + " -> " + time.strftime("%a %b %d %H:%M:%S %Y", localTime))

        timestr = "Sat Mar 28 22:24:24 2016"
        print(time.mktime(time.strptime(timestr, "%a %b %d %H:%M:%S %Y")))
        print("")

        t = (2016, 2, 17, 17, 3, 38, 1, 48, 0)
        secs = time.mktime(t)
        print("time.mktime(t) : %f %d" % (secs, int(secs)))
        print("")

        print("以下输出2017年5月份的日历:")
        print(calendar.month(2017, 5) + "\n")

        # 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
        print(str(calendar.weekday(2017, 5, 12)) + "\n")

        # 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
        print(calendar.monthrange(2017, 5))

        # 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。
        # Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
        monthCalendar = calendar.monthcalendar(2017, 5);
        for weekI in monthCalendar:
            print(weekI, end="\n")

        # 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
        print(calendar.calendar(2017))
