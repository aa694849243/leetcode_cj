# -*- coding: utf-8 -*-
# 你有一个 n x 3 的网格图 grid ，你需要用 红，黄，绿 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜
# 色不同）。
#
#  给你网格图的行数 n 。
#
#  请你返回给 grid 涂色的方案数。由于答案可能会非常大，请你返回答案对 10^9 + 7 取余的结果。
#
#
#
#  示例 1：
#
#  输入：n = 1
# 输出：12
# 解释：总共有 12 种可行的方法：
#
#
#
#  示例 2：
#
#  输入：n = 2
# 输出：54
#
#
#  示例 3：
#
#  输入：n = 3
# 输出：246
#
#
#  示例 4：
#
#  输入：n = 7
# 输出：106494
#
#
#  示例 5：
#
#  输入：n = 5000
# 输出：30228214
#
#
#
#
#  提示：
#
#
#  n == grid.length
#  grid[i].length == 3
#  1 <= n <= 5000
#
#  Related Topics 动态规划
#  👍 87 👎 0

#1递推
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        types = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if i != j and j != k:
                        types.append(i * 9 + j * 3 + k)  # 每一行不同的数目
        ntype = [[0] * len(types) for _ in range(len(types))]
        for i, c1 in enumerate(types):
            for j, c2 in enumerate(types):
                x1, y1, z1 = c1 // 9, c1 // 3 % 3, c1 % 3
                x2, y2, z2 = c2 // 9, c2 // 3 % 3, c2 % 3
                if x1 != x2 and y1 != y2 and z1 != z2:
                    ntype[i][j] = 1
        f = [[0] * len(types) for _ in range(n)]
        f[0] = [1] * len(types)
        for i in range(1, n):
            for j in range(len(types)):
                for k in range(len(types)):
                    if ntype[j][k]:
                        f[i][k] += f[i - 1][j]
                        f[i][k] %= mod
        return sum(f[-1]) % mod
#2 数学 https://leetcode-cn.com/problems/number-of-ways-to-paint-n-3-grid/solution/gei-n-x-3-wang-ge-tu-tu-se-de-fang-an-shu-by-leetc/
class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10 ** 9 + 7
        f1,f2=6,6
        for _ in range(1,n):
            nf1,nf2=2*f1+2*f2,2*f1+3*f2
            f1,f2=nf1%mod,nf2%mod
        return (f1+f2)%mod



Solution().numOfWays(2)
