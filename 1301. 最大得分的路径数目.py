# -*- coding: utf-8 -*-
from typing import List


# 给你一个正方形字符数组 board ，你从数组最右下方的字符 'S' 出发。
#
#  你的目标是到达数组最左上角的字符 'E' ，数组剩余的部分为数字字符 1, 2, ..., 9 或者障碍 'X'。在每一步移动中，你可以向上、向左或者左上
# 方移动，可以移动的前提是到达的格子没有障碍。
#
#  一条路径的 「得分」 定义为：路径上所有数字的和。
#
#  请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 10^9 + 7 取余。
#
#  如果没有任何路径可以到达终点，请返回 [0, 0] 。
#
#
#
#  示例 1：
#
#
# 输入：board = ["E23","2X2","12S"]
# 输出：[7,1]
#
#
#  示例 2：
#
#
# 输入：board = ["E12","1X1","21S"]
# 输出：[4,2]
#
#
#  示例 3：
#
#
# 输入：board = ["E11","XXX","11S"]
# 输出：[0,0]
#
#
#
#
#  提示：
#
#
#  2 <= board.length == board[i].length <= 100
#
#  Related Topics 数组 动态规划 Matrix
#  👍 32 👎 0


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        dp = [[[-1, 0]] * n for _ in range(n)]
        dp[-1][-1] = [0, 1]
        mod = 10**9+7

        def update(x, y, i, j):
            if i>=n or j>=n or  dp[i][j][0] == -1:
                return
            if dp[i][j][0] == dp[x][y][0]:
                dp[x][y][1] += dp[i][j][1]
            elif dp[i][j][0] > dp[x][y][0]:
                dp[x][y] = dp[i][j][:]

        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if (r, c) == (n - 1, n - 1):
                    continue
                if board[r][c] != 'X':
                    update(r, c, r + 1, c + 1)
                    update(r, c, r + 1, c)
                    update(r, c, r, c + 1)
                    if board[r][c] != 'E' and dp[r][c][0] != -1:
                        dp[r][c][0] += int(board[r][c])
                    dp[r][c][1] %= mod
        return dp[0][0] if dp[0][0][0] != -1 else [0, 0]


Solution().pathsWithMaxScore(["E23", "2X2", "12S"])
