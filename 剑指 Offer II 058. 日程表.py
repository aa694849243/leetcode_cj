# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 21:47 
# ide： PyCharm
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.s = SortedList()


    def book(self, start: int, end: int) -> bool:
        idx = self.s.bisect_left((start,end))
        if idx > 0 and self.s[idx - 1][1] > start:
            return False
        if idx < len(self.s) and self.s[idx][0] < end:
            return False
        self.s.add((start,end))
        return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
# leetcode submit region end(Prohibit modification and deletion)

