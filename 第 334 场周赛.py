# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-26 10:26 
# ide： PyCharm
import bisect
import collections
import itertools
import math
from typing import List
import heapq

"""
6369. 左右元素和的差值
给你一个下标从 0 开始的整数数组 nums ，请你找出一个下标从 0 开始的整数数组 answer ，其中：

answer.length == nums.length
answer[i] = |leftSum[i] - rightSum[i]|
其中：

leftSum[i] 是数组 nums 中下标 i 左侧元素之和。如果不存在对应的元素，leftSum[i] = 0 。
rightSum[i] 是数组 nums 中下标 i 右侧元素之和。如果不存在对应的元素，rightSum[i] = 0 。
返回数组 answer 。
"""


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_sum = [0] + [*itertools.accumulate(nums)]
        right_sum = [0] + [*itertools.accumulate(nums[::-1])][:-1]
        left_sum = left_sum[:-1]
        right_sum = right_sum[::-1]
        return [abs(left_sum[i] - right_sum[i]) for i in range(n)]


# print(
#     Solution().leftRigthDifference([1])
# )
"""
6368. 找出字符串的可整除数组
给你一个下标从 0 开始的字符串 word ，长度为 n ，由从 0 到 9 的数字组成。另给你一个正整数 m 。

word 的 可整除数组 div  是一个长度为 n 的整数数组，并满足：

如果 word[0,...,i] 所表示的 数值 能被 m 整除，div[i] = 1
否则，div[i] = 0
返回 word 的可整除数组。
"""


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        res = [0] * len(word)
        pre = 0
        for i, ch in enumerate(word):
            cur = (pre * 10 + int(ch)) % m
            res[i] = +(cur == 0)
            pre = cur
        return res


# print(
#     Solution().divisibilityArray(word = "1010", m = 10)
# )
"""
6367. 求出最多标记下标
给你一个下标从 0 开始的整数数组 nums 。

一开始，所有下标都没有被标记。你可以执行以下操作任意次：

选择两个 互不相同且未标记 的下标 i 和 j ，满足 2 * nums[i] <= nums[j] ，标记下标 i 和 j 。
请你执行上述操作任意次，返回 nums 中最多可以标记的下标数目。
"""


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        nums_l = nums[:n // 2]
        nums_r = nums[n // 2:]
        l, r = 0, 0
        while l < len(nums_l) and r < len(nums_r):
            if nums_l[l] * 2 <= nums_r[r]:
                res += 2
                l += 1
                r += 1
            else:
                r += 1
        return res


"""
6366. 在网格图中访问一个格子的最少时间
给你一个 m x n 的矩阵 grid ，每个元素都为 非负 整数，其中 grid[row][col] 表示可以访问格子 (row, col) 的 最早 时间。也就是说当你访问格子 (row, col) 时，最少已经经过的时间为 grid[row][col] 。

你从 最左上角 出发，出发时刻为 0 ，你必须一直移动到上下左右相邻四个格子中的 任意 一个格子（即不能停留在格子上）。每次移动都需要花费 1 单位时间。

请你返回 最早 到达右下角格子的时间，如果你无法到达右下角的格子，请你返回 -1 。
"""


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        if grid[1][0] > 1 and grid[0][1] > 1:
            return -1
        T = [(0, 0, 0)]
        visted = {(0, 0)}
        while T:
            t, r, c = heapq.heappop(T)
            if r == R - 1 and c == C - 1:
                return t
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] <= t + 1 and (nr, nc) not in visted:
                    visted.add((nr, nc))
                    heapq.heappush(T, (t + 1, nr, nc))
                elif 0 <= nr < R and 0 <= nc < C and grid[nr][nc] > t + 1 and (nr, nc) not in visted:
                    visted.add((nr, nc))
                    if (grid[nr][nc] - t) % 2:
                        heapq.heappush(T, (grid[nr][nc], nr, nc))
                    else:
                        heapq.heappush(T, (grid[nr][nc] + 1, nr, nc))
                # elif len(T) == 1:
                #     print(nr, nc)
        return -1


print(
    Solution().minimumTime([[0, 1, 216], [81323, 14773, 33222]])
)
