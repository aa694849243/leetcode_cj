#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
#
#
#
#  示例 1:
#
#  输入: [7,5,6,4]
# 输出: 5
#
#
#
#  限制：
#
#  0 <= 数组长度 <= 50000
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序
#  👍 466 👎 0

class ftree:
    def __init__(self, n):
        self.n = n
        self.li = [0] * (n + 1)

    @staticmethod
    def lowbit(num):
        return num & -num

    def update(self, num, dt):  # dt为增加幅度，此题为1
        while num <= self.n:
            self.li[num] += dt
            num += self.lowbit(num)

    def quiry(self, num):
        ans = 0
        while num > 0:
            ans += self.li[num]
            num -= self.lowbit(num)
        return ans


import bisect


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)

        def discretization(nums):  # 离散化
            a = sorted(list(set(nums)))
            return [bisect.bisect_left(a, num) + 1 for num in nums]

        li = discretization(nums)
        t = ftree(n)
        ans = 0
        for i in range(n - 1, -1, -1):
            num = li[i]
            ans += t.quiry(num - 1)
            t.update(num, 1)
        return ans