# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 请在 n × n 的棋盘上，实现一个判定井字棋（Tic-Tac-Toe）胜负的神器，判断每一次玩家落子后，是否有胜出的玩家。
#
#  在这个井字棋游戏中，会有 2 名玩家，他们将轮流在棋盘上放置自己的棋子。
#
#  在实现这个判定器的过程中，你可以假设以下这些规则一定成立：
#
#  1. 每一步棋都是在棋盘内的，并且只能被放置在一个空的格子里；
#
#  2. 一旦游戏中有一名玩家胜出的话，游戏将不能再继续；
#
#  3. 一个玩家如果在同一行、同一列或者同一斜对角线上都放置了自己的棋子，那么他便获得胜利。
#
#  示例:
#
#  给定棋盘边长 n = 3, 玩家 1 的棋子符号是 "X"，玩家 2 的棋子符号是 "O"。
#
# TicTacToe toe = new TicTacToe(3);
#
# toe.move(0, 0, 1); -> 函数返回 0 (此时，暂时没有玩家赢得这场对决)
# |X| | |
# | | | |    // 玩家 1 在 (0, 0) 落子。
# | | | |
#
# toe.move(0, 2, 2); -> 函数返回 0 (暂时没有玩家赢得本场比赛)
# |X| |O|
# | | | |    // 玩家 2 在 (0, 2) 落子。
# | | | |
#
# toe.move(2, 2, 1); -> 函数返回 0 (暂时没有玩家赢得比赛)
# |X| |O|
# | | | |    // 玩家 1 在 (2, 2) 落子。
# | | |X|
#
# toe.move(1, 1, 2); -> 函数返回 0 (暂没有玩家赢得比赛)
# |X| |O|
# | |O| |    // 玩家 2 在 (1, 1) 落子。
# | | |X|
#
# toe.move(2, 0, 1); -> 函数返回 0 (暂无玩家赢得比赛)
# |X| |O|
# | |O| |    // 玩家 1 在 (2, 0) 落子。
# |X| |X|
#
# toe.move(1, 0, 2); -> 函数返回 0 (没有玩家赢得比赛)
# |X| |O|
# |O|O| |    // 玩家 2 在 (1, 0) 落子.
# |X| |X|
#
# toe.move(2, 1, 1); -> 函数返回 1 (此时，玩家 1 赢得了该场比赛)
# |X| |O|
# |O|O| |    // 玩家 1 在 (2, 1) 落子。
# |X|X|X|
#
#
#
#
#  进阶:
# 您有没有可能将每一步的 move() 操作优化到比 O(n²) 更快吗?
#  Related Topics 设计 数组 哈希表 矩阵 👍 100 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class TicTacToe:

    def __init__(self, n: int):
        self.Rx = [0] * n
        self.Ro = [0] * n
        self.Cx = [0] * n
        self.Co = [0] * n
        self.posx = 0
        self.negx = 0
        self.poso = 0
        self.nego = 0
        self.msk = (1 << n) - 1
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.Rx[row] |= (1 << col)
            self.Cx[col] |= (1 << row)
            if row == col:
                self.posx |= (1 << col)
            if row + col == self.n - 1:
                self.negx |= (1 << col)
            if self.msk in (self.Rx[row], self.Cx[col], self.posx, self.negx):
                return player
        else:
            self.Ro[row] |= (1 << col)
            self.Co[col] |= (1 << row)
            if row == col:
                self.poso |= (1 << col)
            if row + col == self.n - 1:
                self.nego |= (1 << col)
            if self.msk in (self.Ro[row], self.Co[col], self.poso, self.nego):
                return player
        return 0