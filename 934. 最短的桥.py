# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。）
#
#  现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。
#
#  返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。）
#
#
#
#  示例 1：
#
#
# 输入：A = [[0,1],[1,0]]
# 输出：1
#
#
#  示例 2：
#
#
# 输入：A = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#
#
#  示例 3：
#
#
# 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1
#
#
#
#  提示：
#
#
#  2 <= A.length == A[0].length <= 100
#  A[i][j] == 0 或 A[i][j] == 1
#
#  Related Topics 深度优先搜索 广度优先搜索
#  👍 156 👎 0

# dfs找岛 bfs找桥
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        seen = set()

        def dfs(i, j, island):
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in seen and A[ni][nj] == 1:
                    island.add((ni, nj))
                    seen.add((ni, nj))
                    dfs(ni, nj, island)
            return island

        island1 = set()
        for i in range(R):
            for j in range(C):
                if A[i][j]:
                    island1.add((i, j))
                    seen.add((i,j))
                    island1 = dfs(i, j, island1)
                    break
            if len(seen)>=1:
                break


        q = collections.deque([])
        for r, c in island1:
            q.append((r, c, 0))
        while q:
            r, c, level = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in seen and 0 <= nr < R and 0 <= nc < C:
                    if A[nr][nc] == 1:
                        return level
                    else:
                        if not A[nr][nc]:
                            seen.add((nr,nc))
                            q.append((nr, nc, level + 1))


Solution().shortestBridge([[0,0,0,0,0,0],[0,1,0,0,0,0],[1,1,0,0,0,0],[1,1,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,0,0]])

