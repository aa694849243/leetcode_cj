# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 对于某些固定的 N，如果数组 A 是整数 1, 2, ..., N 组成的排列，使得：
#
#  对于每个 i < j，都不存在 k 满足 i < k < j 使得 A[k] * 2 = A[i] + A[j]。
#
#  那么数组 A 是漂亮数组。
#
#
#
#  给定 N，返回任意漂亮数组 A（保证存在一个）。
#
#
#
#  示例 1：
#
#  输入：4
# 输出：[2,1,4,3]
#
#
#  示例 2：
#
#  输入：5
# 输出：[3,1,2,5,4]
#
#
#
#  提示：
#
#
#  1 <= N <= 1000
#
#
#
#  Related Topics 分治算法
#  👍 125 👎 0

# 分治+仿射变换
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        m = {1: [1]}

        def dfs(n):
            if n in m: return m[n]
            left = dfs((n + 1) // 2)  # 如果size为奇数，左边多一个
            right = dfs(n // 2)
            ans = [x * 2 - 1 for x in left] + [y * 2 for y in right]  # 左侧仿射方程y=num/2+1/2,右侧仿射方程y=num/2
            m[n] = ans
            return ans

        return dfs(n)


Solution().beautifulArray(4)
