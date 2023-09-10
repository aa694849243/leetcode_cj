# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-05-08 1:39 
# ide： PyCharm
import collections
from typing import List
from collections import deque


# leetcode submit region begin(Prohibit modification and deletion)
# 拓扑排序
# 从边缘向中心靠拢
class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        g = collections.defaultdict(list)
        deg = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
            deg[u] += 1
            deg[v] += 1
        q = collections.deque()
        for i in range(n):  # 删掉无金币的叶子节点
            if deg[i] == 1 and coins[i] == 0:
                q.append(i)
        while q:
            u = q.popleft()
            deg[u] -= 1
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 1 and coins[v] == 0:
                    q.append(v)

        times = [0] * n  # 记录遍历到的时间点
        for i in range(n):
            if deg[i] == 1:
                q.append(i)
        while q:
            u = q.popleft()
            deg[u] -= 1
            for v in g[u]:
                deg[v] -= 1
                if deg[v] == 1:
                    q.append(v)
                    times[v] = times[u] + 1
        return sum(times[x] >= 2 and times[y] >= 2 for x, y in edges) * 2


print(
    Solution().collectTheCoins([1, 0, 0, 0, 0, 1, 0, 0, 1], [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6],[6,7],[7,8]])
)
