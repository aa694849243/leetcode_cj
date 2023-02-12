# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-11 13:35 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        R, C = len(grid), len(grid[0])
        if R * C == 1:
            return False
        visted = [[0] * C for _ in range(R)]
        visted[0][0] = 1
        s = set()
        grid2 = [[0] * C for _ in range(R)]

        # visted[R - 1][C - 1] = 1
        @lru_cache(None)
        def dfs(r, c):
            if r == R - 1 and c == C - 1:
                return True
            flag = False
            for nr, nc in [(r + 1, c), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C and not visted[nr][nc] and grid[nr][nc] == 1:
                    visted[nr][nc] = 1
                    if dfs(nr, nc):
                        flag = True
                    visted[nr][nc] = 0
            if flag:
                grid2[r][c] = 1
            return flag

        a = dfs(0, 0)
        if not a:
            return True
        T = {(0, 0)}
        while 1:
            tree = set()
            for r, c in T:
                for nr, nc in [(r + 1, c), (r, c + 1)]:
                    if 0 <= nr < R and 0 <= nc < C and grid2[nr][nc] == 1:
                        tree.add((nr, nc))
            if len(tree) == 1:
                return True
            if not tree:
                break
            T = tree
        return False



# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().isPossibleToCutPath([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
)

