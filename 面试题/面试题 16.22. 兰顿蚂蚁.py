#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。
#
#  (1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。
# (2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。
#
#  编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。
#
#  网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 'X' 表示，白色方格由 '_' 表示，蚂蚁所在的位置由 'L', 'U', 'R',
#  'D' 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。
#
#  示例 1:
#
#  输入: 0
# 输出: ["R"]
#
#
#  示例 2:
#
#  输入: 2
# 输出:
# [
#   "_X",
#   "LX"
# ]
#
#
#  示例 3:
#
#  输入: 5
# 输出:
# [
#   "_U",
#   "X_",
#   "XX"
# ]
#
#
#  说明：
#
#
#  K <= 100000
#
#  Related Topics 数组 哈希表 字符串 矩阵 模拟
#  👍 20 👎 0


class Solution:
    def printKMoves(self, K: int) -> List[str]:
        black = set()
        dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        curdir = 2
        pos = (0, 0)
        for _ in range(K):
            if pos in black:
                curdir = (curdir - 1) % 4
                black.discard(pos)
            else:
                curdir = (curdir + 1) % 4
                black.add(pos)
            dx, dy = dirs[curdir][0], dirs[curdir][1]
            pos = pos[0] + dx, pos[1] + dy
        X = [a[0] for a in black] + [pos[0]]
        Y = [a[1] for a in black] + [pos[1]]
        mx, my = min(X), min(Y)
        matrix = [['_' for y in range(max(Y) - min(Y) + 1)] for x in range(max(X) - min(X) + 1)]
        for x, y in black:
            x -= mx
            y -= my
            matrix[x][y] = 'X'
        matrix[pos[0] - mx][pos[1] - my] = 'LURD'[curdir]

        for i in range(len(matrix)):
            matrix[i] = ''.join(matrix[i])
        return matrix


Solution().printKMoves(5)
