# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-12 10:10 
# ide： PyCharm
import bisect
import collections
import math
from typing import List
import heapq


# 6354.
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            ans += (nums[l] * 10 ** len(str(nums[r]))) + nums[r]
            l += 1
            r -= 1
        if l == r:
            ans += nums[l]
        return ans


# 6355. 统计公平数对的数目
# 给你一个下标从 0 开始、长度为 n 的整数数组 nums ，和两个整数 lower 和 upper ，返回 公平数对的数目 。
# 如果 (i, j) 数对满足以下情况，则认为它是一个 公平数对 ：
# 0 <= i < j < n，且
# lower <= nums[i] + nums[j] <= upper
from sortedcontainers import SortedList


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def calc_greater_than(target):
            lst = SortedList()
            ans = 0
            for i, num in enumerate(nums):
                if i == 0:
                    lst.add(num)
                else:
                    x = target - num
                    ans += i - lst.bisect_left(x)
                    lst.add(num)
            return ans

        return calc_greater_than(lower) - calc_greater_than(upper + 1)


# 6356. 子字符串异或查询
# 给你一个 二进制字符串 s 和一个整数数组 queries ，其中 queries[i] = [firsti, secondi] 。
#
# 对于第 i 个查询，找到 s 的 最短子字符串 ，它对应的 十进制值 val 与 firsti 按位异或 得到 secondi ，换言之，val ^ firsti == secondi 。
#
# 第 i 个查询的答案是子字符串 [lefti, righti] 的两个端点（下标从 0 开始），如果不存在这样的子字符串，则答案为 [-1, -1] 。如果有多个答案，请你选择 lefti 最小的一个。
#
# 请你返回一个数组 ans ，其中 ans[i] = [lefti, righti] 是第 i 个查询的答案。
#
# 子字符串 是一个字符串中一段连续非空的字符序列。
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        queries = [a ^ b for a, b in queries]
        ans = [[-1, -1]] * len(queries)
        for i, querie in enumerate(queries):
            q = str(bin(querie))[2:]
            if q in s:
                ans[i] = [s.index(q), s.index(q) + len(q) - 1]
        return ans


# 6357. 最少得分子序列
# 给你两个字符串 s 和 t 。
#
# 你可以从字符串 t 中删除任意数目的字符。
#
# 如果没有从字符串 t 中删除字符，那么得分为 0 ，否则：
#
# 令 left 为删除字符中的最小下标。
# 令 right 为删除字符中的最大下标。
# 字符串的得分为 right - left + 1 。
#
# 请你返回使 t 成为 s 子序列的最小得分。
#
# 一个字符串的 子序列 是从原字符串中删除一些字符后（也可以一个也不删除），剩余字符不改变顺序得到的字符串。（比方说 "ace" 是 "abcde" 的子序列，但是 "aec" 不是）。
class Solution:
    def minimumScore(self, s: str, t: str) -> int:
        p = 0
        ans = math.inf
        left = [len(s)] * len(t)
        for i, ch in enumerate(s):
            if t[p] == ch:
                left[p] = i
                p += 1
                if p == len(t):
                    return 0
        ans = min(ans, len(t) - p)
        right = [-1] * len(t)
        p = len(t) - 1
        for i in range(len(s) - 1, -1, -1):
            if t[p] == s[i]:
                right[p] = i
                p -= 1
                if p == -1:
                    return 0
        ans = min(ans, p + 1)
        if s[0] == len(t):
            return ans
        r = 0
        for l in range(len(left)):
            r = max(r, l + 1)
            while r < len(right) and right[r] <= left[l]:
                r += 1
            if r == len(right) or left[l] == len(s):
                break
            ans = min(ans, r - l - 1)
        return ans


print(
    Solution().minimumScore(
        "abecdebe",
        "eaebceae"
    )
)
