# -*- coding: utf-8 -*-
import copy
from typing import List


# 给你一个 m x n 的二进制矩阵 mat。
#
#  每一步，你可以选择一个单元格并将它反转（反转表示 0 变 1 ，1 变 0 ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。（注：相邻的两个
# 单元格共享同一条边。）
#
#  请你返回将矩阵 mat 转化为全零矩阵的最少反转次数，如果无法转化为全零矩阵，请返回 -1 。
#
#  二进制矩阵的每一个格子要么是 0 要么是 1 。
#
#  全零矩阵是所有格子都为 0 的矩阵。
#
#
#
#  示例 1：
#
#
#
#  输入：mat = [[0,0],[0,1]]
# 输出：3
# 解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。
#
#
#  示例 2：
#
#  输入：mat = [[0]]
# 输出：0
# 解释：给出的矩阵是全零矩阵，所以你不需要改变它。
#
#
#  示例 3：
#
#  输入：mat = [[1,1,1],[1,0,1],[0,0,0]]
# 输出：6
#
#
#  示例 4：
#
#  输入：mat = [[1,0,0],[1,0,0]]
# 输出：-1
# 解释：该矩阵无法转变成全零矩阵
#
#
#
#
#  提示：
#
#
#  m == mat.length
#  n == mat[0].length
#  1 <= m <= 3
#  1 <= n <= 3
#  mat[i][j] 是 0 或 1 。
#
#  Related Topics 广度优先搜索
#  👍 40 👎 0

# 1Bfs
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])

        def encode(matrix):
            x = 0
            for r in range(R):
                for c in range(C):
                    x <<= 1
                    x += matrix[r][c]
            return x

        def decode(num):
            matrix = [[0] * C for _ in range(R)]
            for r in range(R - 1, -1, -1):
                for c in range(C - 1, -1, -1):
                    matrix[r][c] = num & 1
                    num >>= 1
            return matrix

        def covert(matrix, x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    matrix[nx][ny] ^= 1

        start = encode(mat)
        if start == 0:
            return 0
        t = [start]
        visted = {start}
        steps = 1
        while t:
            tree = []
            for status in t:
                for i in range(R):
                    for j in range(C):
                        matrix = decode(status)
                        covert(matrix, i, j)
                        num = encode(matrix)
                        if num == 0:
                            return steps
                        if num not in visted:
                            tree.append(num)
                            visted.add(num)
            if not tree:
                break
            t = tree
            steps += 1
        return -1


# 2dfs

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])

        def covert(matrix, x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    matrix[nx][ny] ^= 1

        self.ans = float('inf')

        def dfs(matrix, pos, steps):
            if pos == R * C:
                if all(matrix[i][j] == 0 for i in range(R) for j in range(C)):
                    self.ans = min(steps, self.ans)
                return
            dfs(matrix, pos + 1, steps)  # 不翻看情况
            x, y = pos // C, pos % C
            covert(matrix, x, y)
            dfs(matrix, pos + 1, steps + 1)
            covert(matrix, x, y)

        dfs(mat, 0, 0)
        return self.ans if self.ans != float('inf') else -1


# 优化版dfs
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])

        def covert(matrix, x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    matrix[nx][ny] ^= 1

        self.ans = float('inf')

        def dfs(matrix, pos, steps):
            if pos == R * C:
                if all(matrix[i][j] == 0 for i in range(R) for j in range(C)):
                    self.ans = min(steps, self.ans)
                return
            x, y = pos // C, pos % C
            if x == 0:
                dfs(matrix, pos + 1, steps)
                covert(matrix, x, y)
                dfs(matrix, pos + 1, steps + 1)
                covert(matrix, x, y)
            else:  # 除第一层外，其他层都要跟着上一层走，因为上一层能改变的唯一方法就在下一层
                if matrix[x - 1][y] == 0:
                    dfs(matrix, pos + 1, steps)
                else:
                    covert(matrix, x, y)
                    dfs(matrix, pos + 1, steps + 1)
                    covert(matrix, x, y)

        dfs(mat, 0, 0)
        return self.ans if self.ans != float('inf') else -1


# 状压
class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        ans=float('inf')
        def covert(matrix, x, y):
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    matrix[nx][ny] ^= 1

        for num in range(1 << C):
            matrix = copy.deepcopy(mat)
            steps = 0
            for i in range(C):
                if num & (1 << i):
                    steps += 1
                    covert(matrix, 0, i)
            for i in range(1, R):
                for j in range(C):
                    if matrix[i - 1][j] == 1:
                        covert(matrix, i, j)
                        steps += 1
            if all(matrix[i][j]==0 for i in range(R) for j in range(C)):
                ans=min(ans,steps)

        return ans if ans!=float('inf') else -1
Solution().minFlips([[1, 0, 0], [1, 0, 0]])
