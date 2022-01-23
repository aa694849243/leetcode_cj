# -*- coding: utf-8 -*-
import heapq
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，为避免
# 会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。
#
#
#
#  示例 1：
#
#
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：intervals = [[7,10],[2,4]]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= intervals.length <= 10⁴
#  0 <= starti < endi <= 10⁶
#
#  Related Topics 贪心 数组 双指针 排序 堆（优先队列） 👍 366 👎 0

# 1 堆
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort()
        hq = []
        for st, en in intervals:
            if hq and st > hq[0]:
                heapq.heappop(hq)
                heapq.heappush(hq, en)
            else:
                heapq.heappush(hq, en)
        return len(hq)


# 双指针
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        a, b = sorted(x[0] for x in intervals), sorted(x[1] for x in intervals)
        s, e = 0, 0
        usedroom = 0
        while s < len(a):
            if a[s] >= b[e]:
                usedroom -= 1
                e += 1
            usedroom += 1
            s += 1
        return usedroom