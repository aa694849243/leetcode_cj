#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 设想有个机器人坐在一个网格的左上角，网格 r 行 c 列。机器人只能向下或向右移动，但不能走到一些被禁止的网格（有障碍物）。设计一种算法，寻找机器人从左上角
# 移动到右下角的路径。
#
#
#
#  网格中的障碍物和空位置分别用 1 和 0 来表示。
#
#  返回一条可行的路径，路径由经过的网格的行号和列号组成。左上角为 0 行 0 列。如果没有可行的路径，返回空数组。
#
#  示例 1:
#
#  输入:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# 输出: [[0,0],[0,1],[0,2],[1,2],[2,2]]
# 解释:
# 输入中标粗的位置即为输出表示的路径，即
# 0行0列（左上角） -> 0行1列 -> 0行2列 -> 1行2列 -> 2行2列（右下角）
#
#  说明：r 和 c 的值均不超过 100。
#  Related Topics 数组 动态规划 回溯 矩阵
#  👍 66 👎 0


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if not obstacleGrid:
            return []
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[R - 1][C - 1] == 1 or obstacleGrid[0][0]==1:
            return []
        if (R, C) == (1, 1):
            return [[0, 0]]
        self.ans = []
        visted = {(0, 0)}

        def dfs(r, c, path):
            for (nr, nc) in [(r + 1, c), (r, c + 1)]:
                if (nr, nc) == (R - 1, C - 1):
                    self.ans = path + [[nr, nc]]
                    return
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in visted and obstacleGrid[nr][nc]!=1:
                    visted.add((nr, nc))
                    dfs(nr, nc, path + [[nr, nc]])

        dfs(0, 0, [[0, 0]])
        return self.ans
