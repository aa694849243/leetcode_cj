# -*- coding: utf-8 -*-
# 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
#
#  输入为三个整数：day、month 和 year，分别表示日、月、年。
#
#  您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "F
# riday", "Saturday"}。
#
#
#
#  示例 1：
#
#  输入：day = 31, month = 8, year = 2019
# 输出："Saturday"
#
#
#  示例 2：
#
#  输入：day = 18, month = 7, year = 1999
# 输出："Sunday"
#
#
#  示例 3：
#
#  输入：day = 15, month = 8, year = 1993
# 输出："Sunday"
#
#
#
#
#  提示：
#
#
#  给出的日期一定是在 1971 到 2100 年之间的有效日期。
#
#  Related Topics 数组
#  👍 35 👎 0


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def isleapyear(year):
            if year % 400==0:
                return True
            if year % 4 == 0 and year % 100 != 0:
                return True
            return False

        # 1971年1月1日为星期五
        ans = 0
        for y in range(1971, year):
            if isleapyear(y):
                ans += 366
            else:
                ans += 365
        for m in range(1, month):
            if m == 2:
                if isleapyear(year):
                    ans += 29
                else:
                    ans += 28
            elif m in [1, 3, 5, 7, 8, 10, 12]:
                ans += 31
            else:
                ans += 30
        ans += day
        li = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return li[(ans - 3) % 7]
Solution().dayOfTheWeek(31, 3, 1971)