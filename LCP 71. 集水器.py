# -*- coding: utf-8 -*-
# datetime： 2023-02-04 16:47
# ide： PyCharm
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.f[b] = a

    def connect(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def reservoir(self, shape: List[str]) -> int:
        R, C = len(shape), len(shape[0])
        ufind = UnionFind()
        root = (R * C, '-')

        def merge(r, c):
            if shape[r][c] == '.':
                node = (r * C + c, 'd')
                ufind.union(node, (r * C + c, 'u'))
                ufind.union(node, (r * C + c, 'r'))
                ufind.union(node, (r * C + c, 'l'))
                nr, nc = r + 1, c  # 下方
                if nr >= R:
                    ufind.union(root, node)
                elif shape[nr][nc] == 'l':
                    ufind.union((nr * C + nc, 'r'), node)
                elif shape[nr][nc] == 'r':
                    ufind.union((nr * C + nc, 'l'), node)
                elif shape[nr][nc] == '.':
                    ufind.union((nr * C + nc, 'd'), node)
                nr, nc = r, c - 1  # 左边
                if nc < 0:
                    ufind.union(root, node)
                elif shape[nr][nc] == 'l':
                    ufind.union((nr * C + nc, 'r'), node)
                elif shape[nr][nc] == 'r':
                    ufind.union((nr * C + nc, 'd'), node)
                elif shape[nr][nc] == '.':
                    ufind.union((nr * C + nc, 'd'), node)
                nr, nc = r, c + 1  # 右边
                if nc >= C:
                    ufind.union(root, node)
            elif shape[r][c] == 'l':
                node_u = (r * C + c, 'r')
                ufind.union(node_u, (r * C + c, 'u'))
                node_d = (r * C + c, 'd')
                ufind.union(node_d, (r * C + c, 'l'))
                nr, nc = r + 1, c  # 下方
                if nr >= R:
                    ufind.union(root, node_d)
                elif shape[nr][nc] == 'l':
                    ufind.union((nr * C + nc, 'r'), node_d)
                elif shape[nr][nc] == 'r':
                    ufind.union((nr * C + nc, 'l'), node_d)
                elif shape[nr][nc] == '.':
                    ufind.union((nr * C + nc, 'd'), node_d)
                nr, nc = r, c - 1  # 左边
                if nc < 0:
                    ufind.union(root, node_d)
                elif shape[nr][nc] == 'l':
                    ufind.union((nr * C + nc, 'r'), node_d)
                elif shape[nr][nc] == 'r':
                    ufind.union((nr * C + nc, 'd'), node_d)
                elif shape[nr][nc] == '.':
                    ufind.union((nr * C + nc, 'd'), node_d)
                nr, nc = r, c + 1  # 右边
                if nc >= C:
                    ufind.union(root, node_u)
            elif shape[r][c] == 'r':
                node_u = (r * C + c, 'l')
                ufind.union(node_u, (r * C + c, 'u'))
                node_d = (r * C + c, 'd')
                ufind.union(node_d, (r * C + c, 'r'))
                nr, nc = r + 1, c  # 下方
                if nr >= R:
                    ufind.union(root, node_d)
                elif shape[nr][nc] == 'l':
                    ufind.union((nr * C + nc, 'r'), node_d)
                elif shape[nr][nc] == 'r':
                    ufind.union((nr * C + nc, 'l'), node_d)
                elif shape[nr][nc] == '.':
                    ufind.union((nr * C + nc, 'd'), node_d)
                nr, nc = r, c - 1  # 左边
                if nc < 0:
                    ufind.union(root, node_u)
                elif shape[nr][nc] == 'l':
                    ufind.union((nr * C + nc, 'r'), node_u)
                elif shape[nr][nc] == 'r':
                    ufind.union((nr * C + nc, 'd'), node_u)
                elif shape[nr][nc] == '.':
                    ufind.union((nr * C + nc, 'd'), node_u)
                nr, nc = r, c + 1  # 右边
                if nc >= C:
                    ufind.union(root, node_d)

        ans = 0
        for r in range(R - 1, -1, -1):
            for c in range(C):
                merge(r, c)
            for c in range(C):
                for dir in ['u', 'd', 'l', 'r']:
                    if not ufind.connect(root, (r * C + c, dir)):
                        ans += 1 / 2
        for c in range(C):  # 第一行合并上层超级节点
            if shape[0][c] == '.':
                node = (c, 'd')
                ufind.union(node, (c, 'u'))
                ufind.union(node, (c, 'r'))
                ufind.union(node, (c, 'l'))
                ufind.union(root, node)
            elif shape[0][c] == 'l':
                node = (c, 'r')
                ufind.union(node, (c, 'u'))
                ufind.union(root, node)
            elif shape[0][c] == 'r':
                node = (c, 'l')
                ufind.union(node, (c, 'u'))
                ufind.union(root, node)

        for r in range(R):
            for c in range(C):
                for dir in ['u', 'd', 'l', 'r']:
                    if not ufind.connect(root, (r * C + c, dir)):
                        ans -= 1 / 2
        return int(ans)


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().reservoir(
        [".rlrlrlrl", "ll..rl..r", ".llrrllrr", "..lr..lr."]
    )
)
