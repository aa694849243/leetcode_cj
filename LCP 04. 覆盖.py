# -*- coding: utf-8 -*-
import functools
from typing import List


# 你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块
# 骨牌？这些骨牌可以横着或者竖着放。
#
#
#
#  输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。
#
#  输出：一个整数，代表最多能在棋盘上放的骨牌数。
#
#
#
#  示例 1：
#
#  输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
# 输出：2
# 解释：我们最多可以放两块骨牌：[[0, 0], [0, 1]]以及[[0, 2], [1, 2]]。（见下图）
#
#
#
#
#
#  示例 2：
#
#  输入：n = 3, m = 3, broken = []
# 输出：4
# 解释：下图是其中一种可行的摆放方式
#
#
#
#
#
#
#  限制：
#
#
#  1 <= n <= 8
#  1 <= m <= 8
#  0 <= b <= n * m
#
#  Related Topics 位运算 图 数组 动态规划 状态压缩
#  👍 47 👎 0

# 1匈牙利算法
class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        R, C = n, m
        match = [[None for _ in range(C)] for _ in range(R)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, visted):
            visted.add(r, c)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    nxt = match[nr][nc]  # 观察是否名花有主
                    if nxt in visted:  # 如果名花有主且已经访问过,已经访问过说明访问过的这个节点就是之前需要增广路径的节点，跳过它避免重复或无限循环
                        continue
                    if not nxt or dfs(*nxt, visted):  # 如果名花无主或者之前的主人可以找其他花朵
                        match[r][c] = (nr, nc)
                        match[nr][nc] = (r, c)
                        return True
            return False

        ans = 0
        for r, c in broken:
            match[r][c] = '#'
        for r in range(R):
            for c in range(C):
                if (r + c) % 2 and match[r][c] != '#':  # 奇数为主，偶数为花
                    if dfs(r, c, {'#'}):  # 每次都是主去找，冲突的花也只会找之前访问过的主人
                        ans += 1
        return ans


# https://leetcode-cn.com/problems/broken-board-dominoes/solution/backtrace-hui-su-fa-jie-jue-by-hhxxxx/
class Solution:
    def domino(self, n: int, m: int, broken: List[List[int]]) -> int:
        R, C = n, m
        m = {}

        def cal(i, j):
            if (i, j) in m:
                return m[i, j]
            return i * C + j

        status = 0
        for i, j in broken:
            num = cal(i, j)
            status |= (1 << num)

        @functools.lru_cache(typed=False, maxsize=None)
        def dfs(num, status):
            if num >= R * C:
                return 0
            res = 0
            r, c = num // C, num % C
            if status & (1 << num) == 0:
                if r < R - 1 and status & (1 << cal(r + 1, c)) == 0:  # 向下
                    res = max(res, 1 + dfs(num + 1, status | (1 << num) | (1 << cal(r + 1, c))))
                if c < C - 1 and status & (1 << cal(r, c + 1)) == 0:  # 向右
                    res = max(res, 1 + dfs(num, status | (1 << num) | (1 << cal(r, c + 1))))
            res = max(res, dfs(num + 1, status | (1 << num)))
            return res

        return dfs(0,status)
Solution().domino(8, 8,[[1, 0], [1, 1]])