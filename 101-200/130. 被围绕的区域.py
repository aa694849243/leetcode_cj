'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# dfs 深度优先遍历
class SolutiVon:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return []
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):  # 定义回溯策略
            if board[i][j] == 'O':
                board[i][j] = 'B'
            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + dir[0] < rows and 0 <= j + dir[1] < cols and board[i + dir[0]][j + dir[1]] == 'O':
                    dfs(i + dir[0], j + dir[1])

        for i in range(cols):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[rows - 1][i] == 'O':
                dfs(rows - 1, i)
        for i in range(rows):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][cols - 1] == 'O':
                dfs(i, cols - 1)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


# 宽度优先遍历 广度优先遍历 bfs
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        rows = len(board)
        cols = len(board[0])

        def bfs(i, j):
            qu = deque()
            qu.append([i, j])
            while qu:
                a = qu.popleft()
                if board[a[0]][a[1]] == 'O':
                    board[a[0]][a[1]] = 'B'
                    for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if 0 <= a[0] + dir[0] < rows and 0 <= a[1] + dir[1] < cols and board[a[0] + dir[0]][
                            a[1] + dir[1]] == 'O':
                            qu.append([a[0] + dir[0], a[1] + dir[1]])

        for i in range(rows):
            if board[i][0] == 'O':
                bfs(i, 0)
            if board[i][cols - 1] == 'O':
                bfs(i, cols - 1)
        for i in range(cols):
            if board[0][i] == "O":
                bfs(0, i)
            if board[rows - 1][i] == 'O':
                bfs(rows - 1, i)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


# 并查集
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        f = {}
        if not board or not board[0]:
            return []
        cols = len(board[0])
        rows = len(board)

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        origin = cols * rows
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and board[i][j] == 'O':
                    union(origin, i * cols + j)
                else:
                    if board[i][j] == 'O':
                        for dir in ([0, 1], [0, -1], [1, 0], [-1, 0]):
                            if board[i + dir[0]][j + dir[1]] == 'O':
                                union(i * cols + j, (i + dir[0]) * cols + j + dir[1])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O' and find(i * cols + j) != find(origin):
                    board[i][j] = 'X'


a = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
     ["O", "X", "O", "X", "O", "X"]]
Solution().solve(a)
