# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 一个坐标可以从 -infinity 延伸到 +infinity 的 无限大的 棋盘上，你的 骑士 驻扎在坐标为 [0, 0] 的方格里。
#
#  骑士的走法和中国象棋中的马相似，走 “日” 字：即先向左（或右）走 1 格，再向上（或下）走 2 格；或先向左（或右）走 2 格，再向上（或下）走 1 格
# 。
#
#  每次移动，他都可以按图示八个方向之一前进。
#
#
#
#  现在，骑士需要前去征服坐标为 [x, y] 的部落，请你为他规划路线。
#
#  最后返回所需的最小移动次数即可。本题确保答案是一定存在的。
#
#
#
#  示例 1：
#
#  输入：x = 2, y = 1
# 输出：1
# 解释：[0, 0] → [2, 1]
#
#
#  示例 2：
#
#  输入：x = 5, y = 5
# 输出：4
# 解释：[0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
#
#
#
#
#  提示：
#
#
#  |x| + |y| <= 300
#
#  Related Topics 广度优先搜索 👍 63 👎 0


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0
        sr, sc = 0, 0
        dirs = [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, 2)]
        t = [(sr, sc)]
        visted = {(sr, sc)}
        cnt = 0
        while 1:
            tree = []
            cnt += 1
            for r, c in t:
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (nr, nc) not in visted:
                        visted.add((nr,nc))
                        if (nr, nc) == (x, y):
                            return cnt
                        tree.append((nr, nc))
            t=tree

