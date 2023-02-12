# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-29 1:44 
# ide： PyCharm
from typing import List
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = collections.defaultdict(int)
        q = sorted(set(queries))
        R, C = len(grid), len(grid[0])
        vis = [[0] * C for _ in range(R)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(r, c):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= R or nc < 0 or nc >= C or vis[nr][nc]:
                    continue
                else:
                    return False
            return True

        def calc(lst, target):
            T = lst[:]
            res = []
            score = 0
            while 1:
                tree = []
                for r, c in T:
                    if grid[r][c] >= target:
                        res.append((r, c))
                    else:
                        score += 1
                        for dr, dc in dirs:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < R and 0 <= nc < C and not vis[nr][nc]:
                                tree.append((nr, nc))
                                vis[nr][nc] = 1
                if not tree:
                    break
                T = tree
            return score, res

        cur = 0
        vis[0][0] = 1
        nodes=[(0,0)]
        for target in q:
            score, nodes = calc(nodes, target)
            cur += score
            m[target] = cur
        ans = []
        for t in queries:
            ans.append(m[t])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().maxPoints(
        [[1, 2, 3], [2, 5, 7], [3, 5, 1]],
        [5, 6, 2]
    )
)

