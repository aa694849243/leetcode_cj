# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 20:17 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        visted = [[False] * C for _ in range(R)]
        T = []
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    T.append((r, c))
                    visted[r][c] = True
        res = [[0] * C for _ in range(R)]
        step = 0
        while 1:
            tree = []
            for r, c in T:
                res[r][c] = step
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < R and 0 <= nc < C and not visted[nr][nc]:
                        visted[nr][nc] = True
                        tree.append((nr, nc))
            if not tree:
                break
            T = tree
            step += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)

