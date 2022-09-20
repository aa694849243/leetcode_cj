# -*- coding: utf-8 -*-
# 在 `n*m` 大小的棋盘中，有黑白两种棋子，黑棋记作字母 `"X"`, 白棋记作字母 `"O"`，空余位置记作 `"."`。当落下的棋子与其他相同颜色的棋
# 子在行、列或对角线完全包围（中间不存在空白位置）另一种颜色的棋子，则可以翻转这些棋子的颜色。
#
# ![1.gif](https://pic.leetcode-cn.com/1630396029-eTgzpN-6da662e67368466a96d203
# f67bb6e793.gif){:height=170px}![2.gif](https://pic.leetcode-cn.com/1630396240-
# nMvdcc-8e4261afe9f60e05a4f740694b439b6b.gif){:height=170px}![3.gif](https://pic.
# leetcode-cn.com/1630396291-kEtzLL-6fcb682daeecb5c3f56eb88b23c81d33.gif){:height=170
# px}
#
# 「力扣挑战赛」黑白翻转棋项目中，将提供给选手一个未形成可翻转棋子的棋盘残局，其状态记作 `chessboard`。若下一步可放置一枚黑棋，请问选手最多能翻转
# 多少枚白棋。
#
# **注意：**
# - 若翻转白棋成黑棋后，棋盘上仍存在可以翻转的白棋，将可以 **继续** 翻转白棋
# - 输入数据保证初始棋盘状态无可以翻转的棋子且存在空余位置
#
# **示例 1：**
#
# > 输入：`chessboard = ["....X.","....X.","XOOO..","......","......"]`
# >
# > 输出：`3`
# >
# > 解释：
# > 可以选择下在 `[2,4]` 处，能够翻转白方三枚棋子。
#
# **示例 2：**
#
# > 输入：`chessboard = [".X.",".O.","XO."]`
# >
# > 输出：`2`
# >
# > 解释：
# > 可以选择下在 `[2,2]` 处，能够翻转白方两枚棋子。
# > ![2126c1d21b1b9a9924c639d449cc6e65.gif](https://pic.leetcode-cn.com/16266832
# 55-OBtBud-2126c1d21b1b9a9924c639d449cc6e65.gif)
#
# **示例 3：**
#
# > 输入：`chessboard = [".......",".......",".......","X......",".O.....","..O....
# ","....OOX"]`
# >
# > 输出：`4`
# >
# > 解释：
# > 可以选择下在 `[6,3]` 处，能够翻转白方四枚棋子。
# > ![803f2f04098b6174397d6c696f54d709.gif](https://pic.leetcode-cn.com/16303937
# 70-Puyked-803f2f04098b6174397d6c696f54d709.gif)
#
# **提示：**
# - `1 <= chessboard.length, chessboard[i].length <= 8`
# - `chessboard[i]` 仅包含 `"."、"O"` 和 `"X"`
#
#  Related Topics 广度优先搜索 数组 矩阵 👍 6 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from copy import deepcopy


class Solution:
    def flipChess(self, chessboard: List[str]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        R, C = len(chessboard), len(chessboard[0])
        chessboard = [list(row) for row in chessboard]

        def dfs(board):
            board_backup = deepcopy(board)
            res = 0
            for r in range(R):
                for c in range(C):
                    if board[r][c] == '.':
                        tmp = 0
                        board[r][c] = 'X'
                        tmp += get_white_count(board, r, c)
                        if tmp != 0:
                            # tmp += dfs(board)
                            res = max(res, tmp)
                        board = deepcopy(board_backup)
            return res

        def get_white_count(board, r, c):
            count = 0
            candidates = []
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                tmp_cnt = 0
                tmp_cnadidates = []
                while 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'O':
                    tmp_cnt += 1
                    tmp_cnadidates.append((nr, nc))
                    nr += dr
                    nc += dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == 'X':
                    count += tmp_cnt
                    candidates.extend(tmp_cnadidates)
            for r, c in candidates:
                board[r][c] = 'X'
            for r, c in candidates:
                count += get_white_count(board, r, c)
            return count

        return dfs(chessboard)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().flipChess([".O..","XOO.",".XO."]))
# author： caoji
# datetime： 2022-08-26 1:00 
# ide： PyCharm
