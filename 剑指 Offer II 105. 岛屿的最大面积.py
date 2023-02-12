# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 19:53 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.f = {}
        self.sizes = collections.defaultdict(lambda: 1)

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.f[b] = a
            self.sizes[a] += self.sizes[b]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        uf = UnionFind()
        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    ans = max(ans, 1)
                    for nr, nc in [(r - 1, c), (r, c - 1)]:
                        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                            uf.union((nr, nc), (r, c))
                            ans = max(ans, uf.sizes[uf.find((r, c))])
        return ans

# leetcode submit region end(Prohibit modification and deletion)

