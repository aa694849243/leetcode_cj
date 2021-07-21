#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
#
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
#
#
#  例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。
#
#
#
#
#
#  示例 1：
#
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "AB
# CCED"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= board.length <= 200
#  1 <= board[i].length <= 200
#  board 和 word 仅由大小写英文字母组成
#
#
#
#
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/
#  Related Topics 数组 回溯 矩阵
#  👍 362 👎 0


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0]),
        n = len(word)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visted, i):
            if i==n:
                return True
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] == word[i] and (nr,nc) not in visted:
                    if dfs(nr, nc, visted | {(nr, nc)}, i + 1):
                        return True
            return False
        for r in range(R):
            for c in range(C):
                if board[r][c]==word[0]:
                    if dfs(r,c,{(r,c)},1):
                        return True
        return False
Solution().exist([["a","a"]], "aaa")