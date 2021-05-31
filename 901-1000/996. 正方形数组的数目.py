# -*- coding: utf-8 -*-
import collections
import functools
from typing import List


# 给定一个非负整数数组 A，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为正方形数组。
#
#  返回 A 的正方形排列的数目。两个排列 A1 和 A2 不同的充要条件是存在某个索引 i，使得 A1[i] != A2[i]。
#
#
#
#  示例 1：
#
#  输入：[1,17,8]
# 输出：2
# 解释：
# [1,8,17] 和 [17,8,1] 都是有效的排列。
#
#
#  示例 2：
#
#  输入：[2,2,2]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 12
#  0 <= A[i] <= 1e9
#
#  Related Topics 图 数学 回溯算法
#  👍 65 👎 0

# 记忆化+动态规划
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def check(a, b):
            if (a + b) ** 0.5 == int((a + b) ** 0.5):
                return True
            return False

        n = len(nums)

        @functools.lru_cache(None)
        def dp(pre, status):
            if status == (1 << n) - 1:
                return 1
            seen = set()
            ans = 0
            for i in range(n):
                if status & (1 << i) == 0 and check(pre, nums[i]) and nums[i] not in seen:
                    seen.add(nums[i])
                    ans += dp(nums[i], status | (1 << i))
            return ans

        m = set()
        res = 0
        for i, num in enumerate(nums):
            if num in m:
                continue
            m.add(num)
            res += dp(num, 1 << i)
        return res


# 2哈密顿路径+图
# 按值做节点
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def check(a, b):
            if (a + b) ** 0.5 == int((a + b) ** 0.5):
                return True
            return False

        count = collections.Counter(nums)
        graph = collections.defaultdict(list)
        for i in count:
            for j in count:
                if check(i, j):
                    graph[i].append(j)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                ans += sum(dfs(y, todo - 1) for y in graph[x] if count[y]>0)
            count[x] += 1
            return ans
        return sum(dfs(x,len(nums)-1) for x in count)
