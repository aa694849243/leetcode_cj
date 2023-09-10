# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-18 22:16 
# ide： PyCharm
import collections
import heapq
import bisect
import math

# 6359. 替换一个数字后的最大差值
'''
给你一个整数 num 。你知道 Danny Mittal 会偷偷将 0 到 9 中的一个数字 替换 成另一个数字。

请你返回将 num 中 恰好一个 数字进行替换后，得到的最大值和最小值的差位多少。

注意：

当 Danny 将一个数字 d1 替换成另一个数字 d2 时，Danny 需要将 nums 中所有 d1 都替换成 d2 。
Danny 可以将一个数字替换成它自己，也就是说 num 可以不变。
Danny 可以将数字分别替换成两个不同的数字分别得到最大值和最小值。
替换后得到的数字可以包含前导 0 。
Danny Mittal 获得周赛 326 前 10 名，让我们恭喜他。

输入：num = 11891
输出：99009
解释：
为了得到最大值，我们将数字 1 替换成数字 9 ，得到 99899 。
为了得到最小值，我们将数字 1 替换成数字 0 ，得到 890 。
两个数字的差值为 99009 。
'''


class Solution:
    def minMaxDifference(self, num: int) -> int:
        if num == 0:
            return 8
        num = str(num)
        max_num = num
        min_num = num
        for i, ch in enumerate(num):
            if ch != '9':
                max_num = max_num.replace(ch, '9')
                break
        for i, ch in enumerate(num):
            if ch != '0':
                min_num = min_num.replace(ch, '0')
                break
        return int(max_num) - int(min_num)


# print(Solution().minMaxDifference(num = 11891))
'''
6361. 修改两个元素的最小分数
给你一个下标从 0 开始的整数数组 nums 。

nums 的 最小 得分是满足 0 <= i < j < nums.length 的 |nums[i] - nums[j]| 的最小值。
nums的 最大 得分是满足 0 <= i < j < nums.length 的 |nums[i] - nums[j]| 的最大值。
nums 的分数是 最大 得分与 最小 得分的和。
我们的目标是最小化 nums 的分数。你 最多 可以修改 nums 中 2 个元素的值。

请你返回修改 nums 中 至多两个 元素的值后，可以得到的 最小分数 。

|x| 表示 x 的绝对值。

 

示例 1：

输入：nums = [1,4,3]
输出：0
解释：将 nums[1] 和 nums[2] 的值改为 1 ，nums 变为 [1,1,1] 。|nums[i] - nums[j]| 的值永远为 0 ，所以我们返回 0 + 0 = 0 。
示例 2：

输入：nums = [1,4,7,8,5]
输出：3
解释：
将 nums[0] 和 nums[1] 的值变为 6 ，nums 变为 [6,6,7,8,5] 。
最小得分是 i = 0 且 j = 1 时得到的 |nums[i] - nums[j]| = |6 - 6| = 0 。
最大得分是 i = 3 且 j = 4 时得到的 |nums[i] - nums[j]| = |8 - 5| = 3 。
最大得分与最小得分之和为 3 。这是最优答案。
'''
from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3:
            return 0
        return min(nums[-1] - nums[2], nums[-2] - nums[1], nums[-3] - nums[0])


"""
6360. 最小无法得到的或值
给你一个下标从 0 开始的整数数组 nums 。

如果存在一些整数满足 0 <= index1 < index2 < ... < indexk < nums.length ，得到 nums[index1] | nums[index2] | ... | nums[indexk] = x ，那么我们说 x 是 可表达的 。换言之，如果一个整数能由 nums 的某个子序列的或运算得到，那么它就是可表达的。

请你返回 nums 不可表达的 最小非零整数 。

 

示例 1：

输入：nums = [2,1]
输出：4
解释：1 和 2 已经在数组中，因为 nums[0] | nums[1] = 2 | 1 = 3 ，所以 3 是可表达的。由于 4 是不可表达的，所以我们返回 4 。
示例 2：

输入：nums = [5,3,2]
输出：1
解释：1 是最小不可表达的数字。
 

"""


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 1:
            return 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > res + 1:
                return res + 1
            res |= nums[i]
        return res + 1


# print(Solution().minImpossibleOR(nums = [5,3,2]))
"""
6358. 更新数组后处理求和查询
给你两个下标从 0 开始的数组 nums1 和 nums2 ，和一个二维数组 queries 表示一些操作。总共有 3 种类型的操作：

操作类型 1 为 queries[i] = [1, l, r] 。你需要将 nums1 从下标 l 到下标 r 的所有 0 反转成 1 或将 1 反转成 0 。l 和 r 下标都从 0 开始。
操作类型 2 为 queries[i] = [2, p, 0] 。对于 0 <= i < n 中的所有下标，令 nums2[i] = nums2[i] + nums1[i] * p 。
操作类型 3 为 queries[i] = [3, 0, 0] 。求 nums2 中所有元素的和。
请你返回一个数组，包含所有第三种操作类型的答案。
示例 1：

输入：nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]
输出：[3]
解释：第一个操作后 nums1 变为 [1,1,1] 。第二个操作后，nums2 变成 [1,1,1] ，所以第三个操作的答案为 3 。所以返回 [3] 。
示例 2：

输入：nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]
输出：[5]
解释：第一个操作后，nums2 保持不变为 [5] ，所以第二个操作的答案是 5 。所以返回 [5] 。
"""


class SegmentTree:
    def __init__(self, arr):
        self.tree = [0] * (4 * len(arr))
        self.lazy = [0] * (4 * len(arr))
        self.build(arr, 1, 0, len(arr) - 1)

    def build(self, arr, idx, l, r):
        if l == r:
            self.tree[idx] = arr[l]
            return
        mid = (l + r) // 2
        self.build(arr, idx * 2, l, mid)
        self.build(arr, idx * 2 + 1, mid + 1, r)
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def push(self, idx, l, r):
        if self.lazy[idx] != 0:
            self.tree[idx] = (r - l + 1) - self.tree[idx]
            if l != r:
                self.lazy[idx * 2] ^= 1
                self.lazy[idx * 2 + 1] ^= 1
            self.lazy[idx] = 0

    def update(self, idx, l, r, ul, ur):
        self.push(idx, l, r)
        if l > ur or r < ul:
            return
        if ul <= l and r <= ur:
            self.tree[idx] = (r - l + 1) - self.tree[idx]
            if l != r:
                self.lazy[idx * 2] ^= 1
                self.lazy[idx * 2 + 1] ^= 1
            return
        mid = (l + r) // 2
        self.update(idx * 2, l, mid, ul, ur)
        self.update(idx * 2 + 1, mid + 1, r, ul, ur)
        self.tree[idx] = self.tree[idx * 2] + self.tree[idx * 2 + 1]

    def query(self, idx, l, r, ql, qr):
        self.push(idx, l, r)
        if l > qr or r < ql:
            return 0
        if ql <= l and r <= qr:
            return self.tree[idx]
        mid = (l + r) // 2
        return self.query(idx * 2, l, mid, ql, qr) + self.query(idx * 2 + 1, mid + 1, r, ql, qr)


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        tree = SegmentTree(nums1)
        total = sum(nums2)
        for query in queries:
            if query[0] == 1:
                tree.update(1, 0, len(nums1) - 1, query[1], query[2])
            elif query[0] == 2:
                total += query[1] * tree.query(1, 0, len(nums1) - 1, 0, len(nums1) - 1)
            else:
                res.append(total)
        return res


# a = ftree_range(5)
# a.range_add(1, 3, 1)
# # a.range_add(1, 2, 2)
# # a.range_ask(1,3)
# # print(a.ask(3))
# print(a.ask(1))
# print(a.range_ask(1, 2))
# print(Solution().handleQuery(nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]))
'''
6362. 合并两个二维数组 - 求和法
给你两个 二维 整数数组 nums1 和 nums2.

nums1[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
nums2[i] = [idi, vali] 表示编号为 idi 的数字对应的值等于 vali 。
每个数组都包含 互不相同 的 id ，并按 id 以 递增 顺序排列。

请你将两个数组合并为一个按 id 以递增顺序排列的数组，并符合下述条件：

只有在两个数组中至少出现过一次的 id 才能包含在结果数组内。
每个 id 在结果数组中 只能出现一次 ，并且其对应的值等于两个数组中该 id 所对应的值求和。如果某个数组中不存在该 id ，则认为其对应的值等于 0 。
返回结果数组。返回的数组需要按 id 以递增顺序排列。

 

示例 1：

输入：nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
输出：[[1,6],[2,3],[3,2],[4,6]]
解释：结果数组中包含以下元素：
- id = 1 ，对应的值等于 2 + 4 = 6 。
- id = 2 ，对应的值等于 3 。
- id = 3 ，对应的值等于 2 。
- id = 4 ，对应的值等于5 + 1 = 6 。
示例 2：

输入：nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
输出：[[1,3],[2,4],[3,6],[4,3],[5,5]]
解释：不存在共同 id ，在结果数组中只需要包含每个 id 和其对应的值。
'''


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        c = collections.defaultdict(int)
        for i in range(len(nums1)):
            c[nums1[i][0]] += nums1[i][1]
        for i in range(len(nums2)):
            c[nums2[i][0]] += nums2[i][1]
        return sorted(c.items(), key=lambda x: x[0])


"""
6365. 将整数减少到零需要的最少操作数
给你一个正整数 n ，你可以执行下述操作 任意 次：

n 加上或减去 2 的某个 幂
返回使 n 等于 0 需要执行的 最少 操作数。

如果 x == 2i 且其中 i >= 0 ，则数字 x 是 2 的幂。
示例 1：

输入：n = 39
输出：3
解释：我们可以执行下述操作：
- n 加上 20 = 1 ，得到 n = 40 。
- n 减去 23 = 8 ，得到 n = 32 。
- n 减去 25 = 32 ，得到 n = 0 。
可以证明使 n 等于 0 需要执行的最少操作数是 3 。
示例 2：

输入：n = 54
输出：3
解释：我们可以执行下述操作：
- n 加上 21 = 2 ，得到 n = 56 。
- n 加上 23 = 8 ，得到 n = 64 。
- n 减去 26 = 64 ，得到 n = 0 。
使 n 等于 0 需要执行的最少操作数是 3 。
"""

import functools

import math
import functools

import math
import functools

import functools
import math


class Solution:
    def minOperations(self, n: int) -> int:
        @functools.lru_cache(None)
        def dfs(x):
            if x & (x - 1) == 0:
                return 1
            nb = (x & -x)
            return min(dfs(x - nb), dfs(x + nb)) + 1

        return dfs(n)


print(Solution().minOperations(39))
