#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 这个问题是实现一个简单的消除算法。
#
#  给定一个二维整数数组 board 代表糖果所在的方格，不同的正整数 board[i][j] 代表不同种类的糖果，如果 board[i][j] = 0 代表
#  (i, j) 这个位置是空的。给定的方格是玩家移动后的游戏状态，现在需要你根据以下规则粉碎糖果，使得整个方格处于稳定状态并最终输出。
#
#
#  如果有三个及以上水平或者垂直相连的同种糖果，同一时间将它们粉碎，即将这些位置变成空的。
#  在同时粉碎掉这些糖果之后，如果有一个空的位置上方还有糖果，那么上方的糖果就会下落直到碰到下方的糖果或者底部，这些糖果都是同时下落，也不会有新的糖果从顶部出
# 现并落下来。
#  通过前两步的操作，可能又会出现可以粉碎的糖果，请继续重复前面的操作。
#  当不存在可以粉碎的糖果，也就是状态稳定之后，请输出最终的状态。
#
#
#  你需要模拟上述规则并使整个方格达到稳定状态，并输出。
#
#
#
#  样例 :
#
#  输入:
# board =
# [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,41
# 4],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[
# 4,1,4,4,1014]]
#
# 输出:
# [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,
# 113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,
# 512,713,1014]]
#
# 解释:
#
#
#
#
#
#  注释 :
#
#
#  board 数组的行数区间是 [3, 50]。
#  board[i] 数组的长度区间（即 board 数组的列数区间）是 [3, 50]。
#  每个 board[i][j] 初始整数范围是 [1, 2000]。
#
#  Related Topics 数组 双指针 矩阵 模拟
#  👍 67 👎 0


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        R, C = len(board), len(board[0])
        todo = False
        for r in range(R):
            for c in range(C - 2):
                if abs(board[r][c]) == abs(board[r][c + 1]) == abs(board[r][c + 2]) != 0:
                    board[r][c] = board[r][c + 1] = board[r][c + 2] = -abs(board[r][c])
                    todo = True
        for c in range(C):
            for r in range(R - 2):
                if abs(board[r][c]) == abs(board[r + 1][c]) == abs(board[r + 2][c]) != 0:
                    board[r][c] = board[r + 1][c] = board[r + 2][c] = -abs(board[r][c])
                    todo = True
        for c in range(C):
            wr = R - 1
            for r in range(R - 1, -1, -1):
                if board[r][c] > 0:
                    board[wr][c] = board[r][c]
                    wr -= 1
            for r in range(wr,-1,-1):
                board[r][c]=0
        return self.candyCrush(board) if todo else board
