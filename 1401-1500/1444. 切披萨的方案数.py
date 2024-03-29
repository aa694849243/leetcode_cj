#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个 rows x cols 大小的矩形披萨和一个整数 k ，矩形包含两种字符： 'A' （表示苹果）和 '.' （表示空白格子）。你需要切披萨 k-1
#  次，得到 k 块披萨并送给别人。
#
#  切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平
# 地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。
#
#  请你返回确保每一块披萨包含 至少 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。
#
#
#
#  示例 1：
#
#
#
#  输入：pizza = ["A..","AAA","..."], k = 3
# 输出：3
# 解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。
#
#
#  示例 2：
#
#  输入：pizza = ["A..","AA.","..."], k = 3
# 输出：1
#
#
#  示例 3：
#
#  输入：pizza = ["A..","A..","..."], k = 1
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= rows, cols <= 50
#  rows == pizza.length
#  cols == pizza[i].length
#  1 <= k <= 10
#  pizza 只包含字符 'A' 和 '.' 。
#
#  Related Topics 记忆化搜索 数组 动态规划 矩阵
#  👍 47 👎 0

# 二维前缀和
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10 ** 9 + 7
        R, C = len(pizza), len(pizza[0])
        cnt_apple = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R - 1, -1, -1):
            for c in range(C - 1, -1, -1):
                cnt_apple[r][c] = cnt_apple[r + 1][c] + cnt_apple[r][c + 1] - cnt_apple[r + 1][c + 1] + int(pizza[r][c] == 'A')
        dp = [[[-1] * (k + 1) for _ in range(C)] for _ in range(R)]

        def dfs(i, j, z):
            if dp[i][j][z] != -1:
                return dp[i][j][z]
            if z > cnt_apple[i][j]:
                return 0
            if z == 1:
                return 1
            dp[i][j][z] = 0
            for x in range(i + 1, R):
                if cnt_apple[i][j] > cnt_apple[x][j]:  # 需要切下来有苹果
                    dp[i][j][z] += dfs(x, j, z - 1)
            for y in range(j + 1, C):
                if cnt_apple[i][j] > cnt_apple[i][y]:
                    dp[i][j][z] += dfs(i, y, z - 1)
            return dp[i][j][z] % mod

        return dfs(0, 0, k)


Solution().ways(["A..", "AAA", "..."], k=3)
