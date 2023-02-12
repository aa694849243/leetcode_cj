# -*- coding: utf-8 -*-
# datetime： 2023-02-01 23:04
# ide： PyCharm
import collections


# leetcode submit region begin(Prohibit modification and deletion)
# 树形dfs 树形dp
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = 0

        def dfs(node, fa) -> (int, int):
            nonlocal ans
            s0, s1 = 0, price[node]  # s0为当前节点不带叶子节点的最大值，s1为当前节点带叶子节点的最大值
            p = price[node]
            for nxt in g[node]:
                if nxt == fa: continue
                t0, t1 = dfs(nxt, node)  # t0:不带叶子节点的最大值 t1:带叶子节点的最大值
                ans = max(ans, s0 + t1, s1 + t0)
                s0 = max(s0, t0 + p)
                s1 = max(s1, t1 + p)
            return s0, s1

        dfs(0, -1)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
