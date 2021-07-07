# -*- coding: utf-8 -*-
import collections
from typing import List


# 总共有 n 个人和 40 种不同的帽子，帽子编号从 1 到 40 。
#
#  给你一个整数列表的列表 hats ，其中 hats[i] 是第 i 个人所有喜欢帽子的列表。
#
#  请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。
#
#  由于答案可能很大，请返回它对 10^9 + 7 取余后的结果。
#
#
#
#  示例 1：
#
#
# 输入：hats = [[3,4],[4,5],[5]]
# 输出：1
# 解释：给定条件下只有一种方法选择帽子。
# 第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。
#
#  示例 2：
#
#
# 输入：hats = [[3,5,1],[3,5]]
# 输出：4
# 解释：总共有 4 种安排帽子的方法：
# (3,5)，(5,3)，(1,3) 和 (1,5)
#
#
#  示例 3：
#
#
# 输入：hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
# 输出：24
# 解释：每个人都可以从编号为 1 到 4 的帽子中选。
# (1,2,3,4) 4 个帽子的排列方案数为 24 。
#
#
#  示例 4：
#
#
# 输入：hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
# 输出：111
#
#
#
#
#  提示：
#
#
#  n == hats.length
#  1 <= n <= 10
#  1 <= hats[i].length <= 40
#  1 <= hats[i][j] <= 40
#  hats[i] 包含一个数字互不相同的整数列表。
#
#  Related Topics 位运算 数组 动态规划 状态压缩
#  👍 67 👎 0


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        maxhat = max(max(hats[i]) for i in range(len(hats)))
        n = len(hats)
        f = [[0] * (1 << n) for _ in range(maxhat + 1)]
        f[0][0] = 1  # f[i][j] i代表帽子号，j代表人
        m = collections.defaultdict(list)
        mod = 10 ** 9 + 7
        for i in range(n):
            for h in hats[i]:
                m[h].append(i)
        for h in range(1, maxhat + 1):
            for mask in range(1 << n):
                f[h][mask] = f[h - 1][mask]  # 不用h号帽子
                for j in m[h]:
                    if mask & (1 << j):
                        f[h][mask] += f[h - 1][mask ^ (1 << j)]  # h号帽子用在第j个人头上
                f[h][mask]%=mod
        return f[-1][(1<<n)-1]