#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
from typing import List


# 给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差
#
#
#
#  示例：
#
#
# 输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# 输出：3，即数值对(11, 8)
#
#
#
#
#  提示：
#
#
#  1 <= a.length, b.length <= 100000
#  -2147483648 <= a[i], b[i] <= 2147483647
#  正确结果在区间 [0, 2147483647] 内
#
#  Related Topics 数组 双指针 二分查找 排序
#  👍 38 👎 0


class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        heapq.heapify(a)
        heapq.heapify(b)
        flaga = a[0]
        flagb = b[0]
        ans = float('inf')
        while a and b:
            while a and a[0] < b[0]:
                flaga = heapq.heappop(a)
            if a and a[0] == b[0]:
                return 0
            ans = min(ans, abs(flaga - b[0]))
            while a and b and b[0] < a[0]:
                flagb = heapq.heappop(b)
            if a and b and b[0] == a[0]:
                return 0
            if a:
                ans = min(ans, abs(flagb - a[0]))
        return ans
Solution().smallestDifference([0],[2147483647])