#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。
#
#  以下是井字游戏的规则：
#
#
#  玩家轮流将字符放入空位（" "）中。
#  第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。
#  "X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。
#  当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。
#  当所有位置非空时，也算为游戏结束。
#  如果游戏结束，玩家不允许再放置字符。
#
#
#  如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "P
# ending"。
#
#  示例 1：
#
#  输入： board = ["O X"," XO","X O"]
# 输出： "X"
#
#
#  示例 2：
#
#  输入： board = ["OOX","XXO","OXO"]
# 输出： "Draw"
# 解释： 没有玩家获胜且不存在空位
#
#
#  示例 3：
#
#  输入： board = ["OOX","XXO","OX "]
# 输出： "Pending"
# 解释： 没有玩家获胜且仍存在空位
#
#
#  提示：
#
#
#  1 <= board.length == board[i].length <= 100
#  输入一定遵循井字棋规则
#
#  Related Topics 数组 计数 矩阵
#  👍 22 👎 0


class Solution:
    def tictactoe(self, board: List[str]) -> str:
        mr = collections.defaultdict(lambda: collections.defaultdict(int))
        mc = collections.defaultdict(lambda: collections.defaultdict(int))
        mr_add_c = collections.defaultdict(int)
        mr_c = collections.defaultdict(int)
        N = len(board)
        flagcnt = False
        for r in range(N):
            for c in range(N):
                s = board[r][c]
                if s==' ':
                    flagcnt = True
                    continue
                mr[r][s] += 1
                mc[c][s] += 1
                if r == c:
                    mr_c[s] += 1
                if r + c == N-1:
                    mr_add_c[s] += 1
                if mr[r][s] == N or mc[c][s] == N or mr_c[s] == N or mr_add_c[s] == N:
                    return s
        return 'Draw' if not flagcnt else 'Pending'


Solution().tictactoe(["O X"," XO","X O"])
