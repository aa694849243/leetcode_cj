#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整
# 个棋盘的那两条对角线。
#
#  注意：本题相对原题做了扩展
#
#  示例:
#
#   输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#
#  Related Topics 数组 回溯
#  👍 90 👎 0


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(y, banx, ban_x_y, ban_x_add_y, path):
            if y == n:
                res.append(path.copy())
                return
            row = ['.'] * n
            for x in range(n):
                if x not in banx and x - y not in ban_x_y and x + y not in ban_x_add_y:
                    row[x] = 'Q'
                    dfs(y + 1, banx | {x}, ban_x_y | {x - y}, ban_x_add_y | {x + y}, path + [''.join(row)])
                    row[x] = '.'
        dfs(0,set(),set(),set(),[])
        return res
Solution().solveNQueens(4)