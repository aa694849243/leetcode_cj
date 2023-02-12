# -*- coding: utf-8 -*-
# datetime： 2023-01-28 1:56
# ide： PyCharm
class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v in edges:
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)
        color = [0] * n

        def is_bipart(x, c):
            nodes.append(x)
            color[x] = c
            for y in g[x]:
                if color[y] == c or color[y] == 0 and not is_bipart(y, -c): return False
            return True

        vis = [0] * n
        clock = 0

        def bfs(start):
            nonlocal clock
            clock += 1
            T = [start]
            vis[start] = clock
            step = 1
            while 1:
                tree = []
                for node in T:
                    for nxt in g[node]:
                        if vis[nxt] != clock:
                            vis[nxt] = clock
                            tree.append(nxt)
                if not tree: break
                T = tree
                step += 1
            return step

        ans = 0
        for i, c in enumerate(color):
            if c == 0:
                nodes = []
                if not is_bipart(i, 1): return -1
                ans += max(bfs(node) for node in nodes)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().magnificentSets(
    2,
    [[1, 2]]
))

