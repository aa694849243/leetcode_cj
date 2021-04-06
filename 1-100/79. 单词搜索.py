'''
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
 

提示：

board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

#二维数组递归caojie——33%
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.visted = [[False] * cols for _ in range(rows)]

        def dfs(board, l1, i, j):
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == l1[0] and not self.visted[i][j]:
                if len(l1) == 1:
                    return True
                self.visted[i][j] = True
                for k in range(4):
                    newi = i + direction[k][0]
                    newj = j + direction[k][1]
                    if 0 <= newi < rows and 0 <= newj < cols and not self.visted[newi][newj] and dfs(board, l1[1:], newi, newj):
                        return True
                self.visted[i][j] = False

        for i in range(rows):
            for j in range(cols):
                if dfs(board, word, i, j):
                    return True
        return False


Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED')
