# -*- coding: utf-8 -*-
# 请你编写一个程序来计算两个日期之间隔了多少天。
#
#  日期以字符串形式给出，格式为 YYYY-MM-DD，如示例所示。
#
#
#
#  示例 1：
#
#  输入：date1 = "2019-06-29", date2 = "2019-06-30"
# 输出：1
#
#
#  示例 2：
#
#  输入：date1 = "2020-01-15", date2 = "2019-12-31"
# 输出：15
#
#
#
#
#  提示：
#
#
#  给定的日期是 1971 年到 2100 年之间的有效日期。
#
#  Related Topics 数学 字符串
#  👍 33 👎 0


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split('-')
        date2 = date2.split('-')
        date1, date2 = sorted([date1, date2])
        diff = 0

        def isleapyear(y):
            return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

        for y in range(int(date1[0]), int(date2[0])):
            if isleapyear(y):
                diff += 366
            else:
                diff += 365
        for month in range(1, int(date1[1])):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                diff -= 31
            elif month == 2:
                if isleapyear(int(date1[0])):
                    diff -= 29
                else:
                    diff -= 28
            else:
                diff -= 30
        for month in range(1, int(date2[1])):
            if month in [1, 3, 5, 7, 8, 10, 12]:
                diff += 31
            elif month == 2:
                if isleapyear(int(date2[0])):
                    diff += 29
                else:
                    diff += 28
            else:
                diff += 30
        diff+=int(date2[2])-int(date1[2])
        return diff
Solution().daysBetweenDates("2020-01-15", date2 = "2019-12-31")