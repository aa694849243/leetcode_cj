# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个整数 n 表示某所大学里课程的数目，编号为 1 到 n ，数组 dependencies 中， dependencies[i] = [xi, yi]
#  表示一个先修课的关系，也就是课程 xi 必须在课程 yi 之前上。同时你还有一个整数 k 。
#
#  在一个学期中，你 最多 可以同时上 k 门课，前提是这些课的先修课在之前的学期里已经上过了。
#
#  请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。
#
#
#
#  示例 1：
#
#
#
#  输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
# 输出：3
# 解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。
#
#
#  示例 2：
#
#
#
#  输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
# 输出：4
# 解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。
#
#
#  示例 3：
#
#  输入：n = 11, dependencies = [], k = 2
# 输出：6
#
#
#
#
#  提示：
#
#
#  1 <= n <= 15
#  1 <= k <= n
#  0 <= dependencies.length <= n * (n-1) / 2
#  dependencies[i].length == 2
#  1 <= xi, yi <= n
#  xi != yi
#  所有先修关系都是不同的，也就是说 dependencies[i] != dependencies[j] 。
#  题目输入的图是个有向无环图。
#
#  Related Topics 位运算 图 动态规划 状态压缩 👍 77 👎 0

# https://leetcode-cn.com/problems/parallel-courses-ii/solution/bing-xing-ke-cheng-ii-ya-suo-zhuang-tai-vzihz/
class Solution:
    def minNumberOfSemesters(self, n: int, relations: List[List[int]], k: int) -> int:
        if not relations:
            return (n - 1) // k + 1
        if len(relations) == 1:
            a = (n - 1) // k + 1
            return a if a != 1 else 2

        relations = [[relations[i][0] - 1, relations[i][1] - 1] for i in range(len(relations))]
        pre = [0] * n
        for a, b in relations:
            pre[b] |= (1 << a)

        def getafter(status):
            res = 0
            for i in range(n):
                prestatus = pre[i]
                if prestatus & status == prestatus and not ((1 << i) & status):
                    res |= (1 << i)
            return res

        # 求二进制的子序列 二进制的子数组
        def getsubset(status):
            res = set()
            tmp = status
            while tmp:
                res.add(tmp)
                tmp = (tmp - 1) & status
            return res

        dp = [float('inf')] * (2 ** n)
        dp[0] = 0
        for i in range(2 ** n):
            nxt = getafter(i)
            subs = getsubset(nxt)
            for sub in subs:
                if bin(sub)[2:].count('1') <= k:
                    dp[i | sub] = min(dp[i | sub], dp[i] + 1)
        return dp[-1]