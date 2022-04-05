# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 整数数组 stations 表示 水平数轴 上各个加油站的位置。给你一个整数 k 。
#
#  请你在数轴上增设 k 个加油站，新增加油站可以位于 水平数轴 上的任意位置，而不必放在整数位置上。
#
#  设 penalty() 是：增设 k 个新加油站后，相邻 两个加油站间的最大距离。
# 请你返回 penalty() 可能的最小值。与实际答案误差在 10⁻⁶ 范围内的答案将被视作正确答案。
#
#
#
#  示例 1：
#
#
# 输入：stations = [1,2,3,4,5,6,7,8,9,10], k = 9
# 输出：0.50000
#
#
#  示例 2：
#
#
# 输入：stations = [23,24,36,39,46,56,57,65,84,98], k = 1
# 输出：14.00000
#
#
#
#
#  提示：
#
#
#  10 <= stations.length <= 2000
#  0 <= stations[i] <= 10⁸
#  stations 按 严格递增 顺序排列
#  1 <= k <= 10⁶
#
#  Related Topics 数组 二分查找 👍 48 👎 0

# https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station/solution/cpython3-huan-ge-jiao-du-er-fen-cha-zhao-yjoc/
class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        stations.sort()
        dist = [stations[i + 1] - stations[i] for i in range(len(stations) - 1)]

        def check(d):
            res = 0
            for dd in dist:
                res += (dd // d)
            return res <= k  # 说明达到这个距离，需要res个，如果res少于k个说明d还可以收窄

        l, r = 0, 10 ** 9
        eps = 10 ** -6
        while r - l > eps:
            mid = (l + r) / 2
            if check(mid):
                r = mid
            else:
                l = mid + eps
        return l
