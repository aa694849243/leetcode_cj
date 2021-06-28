# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import functools


# 你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。
#
#  房子的客厅大小为 n x m，为保持极简的风格，需要使用尽可能少的 正方形 瓷砖来铺盖地面。
#
#  假设正方形瓷砖的规格不限，边长都是整数。
#
#  请你帮设计师计算一下，最少需要用到多少块方形瓷砖？
#
#
#
#  示例 1：
#
#
#
#  输入：n = 2, m = 3
# 输出：3
# 解释：3 块地砖就可以铺满卧室。
#      2 块 1x1 地砖
#      1 块 2x2 地砖
#
#  示例 2：
#
#
#
#  输入：n = 5, m = 8
# 输出：5
#
#
#  示例 3：
#
#
#
#  输入：n = 11, m = 13
# 输出：6
#
#
#
#
#  提示：
#
#
#  1 <= n <= 13
#  1 <= m <= 13
#
#  Related Topics 动态规划 回溯算法
#  👍 65 👎 0


class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:
        min_steps = max(n, m)
        arr = [[False for _ in range(m)] for _ in range(n)]

        @functools.lru_cache(None)
        def astar(remain):
            if remain == 0:
                return 0
            res = remain
            i = 1
            while i ** 2 <= remain:
                res = min(res, astar(remain - i ** 2) + 1)
                i += 1
            return res

        def dfs(steps, i, j, remain):
            nonlocal min_steps
            if steps + astar(remain) >= min_steps:
                return
            if i >= n:
                min_steps = min(min_steps, steps)
                return
            if j >= m:
                dfs(steps, i + 1, 0, remain)
                return
            if arr[i][j]:
                dfs(steps, i, j + 1, remain)
                return
            for length in range(min(n - i, m - j)):  # 找最大方块
                if arr[i][j + length]:
                    break
                u = length
            for x in range(i, i + u + 1):
                for y in range(j, j + u + 1):
                    arr[x][y] = True
            for l in range(u, -1, -1):  # 逐步缩小方块
                dfs(steps + 1, i, j + l + 1, remain - (l + 1) ** 2)
                for x in range(i, i + l + 1):  # 消掉外层方块
                    arr[x][j + l] = False
                for y in range(j, j + l + 1):  # 消掉外层方块
                    arr[i + l][y] = False

        dfs(0, 0, 0, n * m)
        return min_steps


Solution().tilingRectangle(5, 8)
