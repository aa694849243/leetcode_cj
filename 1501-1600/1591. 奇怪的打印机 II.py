#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你一个奇怪的打印机，它有如下两个特殊的打印规则：
#
#
#  每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。
#  一旦矩形根据上面的规则使用了一种颜色，那么 相同的颜色不能再被使用 。
#
#
#  给你一个初始没有颜色的 m x n 的矩形 targetGrid ，其中 targetGrid[row][col] 是位置 (row, col) 的颜色。
#
#
#  如果你能按照上述规则打印出矩形 targetGrid ，请你返回 true ，否则返回 false 。
#
#
#
#  示例 1：
#
#
#
#  输入：targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
# 输出：true
#
#
#  示例 2：
#
#
#
#  输入：targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
# 输出：true
#
#
#  示例 3：
#
#  输入：targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
# 输出：false
# 解释：没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。
#
#  示例 4：
#
#  输入：targetGrid = [[1,1,1],[3,1,3]]
# 输出：false
#
#
#
#
#  提示：
#
#
#  m == targetGrid.length
#  n == targetGrid[i].length
#  1 <= m, n <= 60
#  1 <= targetGrid[row][col] <= 60
#
#  Related Topics 图 拓扑排序 数组 矩阵
#  👍 23 👎 0


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors = collections.defaultdict(set)
        R, C = len(targetGrid), len(targetGrid[0])
        for r in range(R):
            for c in range(C):
                colors[targetGrid[r][c]].add((r, c))
        m = {}
        for p in colors:
            mir, mic = R, C
            mar, mac = -1, -1
            for r, c in colors[p]:
                mir, mic = min(r, mir), min(c, mic)
                mar, mac = max(r, mar), max(c, mac)
            m[p] = [mir, mic, mar, mac]
        unfilled = collections.defaultdict(set)
        for p in m:
            mir, mic, mar, mac = m[p]
            for r in range(mir, mar + 1):
                for c in range(mic, mac + 1):
                    if targetGrid[r][c] != p:
                        unfilled[p].add((r, c))
        while unfilled:
            d = []
            for color in unfilled.keys():
                if not unfilled[color]:
                    unfilled.pop(color)
                    d.append(color)
            if not d:
                return False
            for color in d:
                unfilled[color] -= colors[color]
        return True


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        R, C = len(targetGrid), len(targetGrid[0])
        colors = collections.defaultdict(set)
        for r in range(R):
            for c in range(C):
                colors[targetGrid[r][c]].add((r, c))
        rects = collections.defaultdict(list)
        for color in colors:
            rects[color] = [min(r for r, c in colors[color]), max(r for r, c in colors[color]), min(c for r, c in colors[color]), max(c for r, c in colors[color])]
        unfilled = collections.defaultdict(set)
        for color in colors:
            mir, mar, mic, mac = rects[color]
            unfilled[color]
            for r in range(mir, mar + 1):
                for c in range(mic, mac + 1):
                    if targetGrid[r][c] != color:
                        unfilled[color].add((r, c))
        while unfilled:
            for color in unfilled:
                if not unfilled[color]:  # 只有完整矩形才能上色
                    break
            else:  # unfilled没有清空，但是没有可以上色的完整矩形
                return False
            unfilled.pop(color)
            for other in unfilled:
                unfilled[other] -= colors[color]
        return True

Solution().isPrintable([[1, 1, 1, 1], [1, 2, 2, 1], [1, 2, 2, 1], [1, 1, 1, 1]])
#线段树