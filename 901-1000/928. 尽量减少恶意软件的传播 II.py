# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# (这个问题与 尽量减少恶意软件的传播 是一样的，不同之处用粗体表示。)
#
#  在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。
#
#  一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传
# 播将继续，直到没有更多的节点可以被这种方式感染。
#
#  假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
#
#  我们可以从初始列表中删除一个节点，并完全移除该节点以及从该节点到任何其他节点的任何连接。如果移除这一节点将最小化 M(initial)， 则返回该节点。如
# 果有多个节点满足条件，就返回索引最小的节点。
#
#
#
#
#
#
#  示例 1：
#
#  输出：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输入：0
#
#
#  示例 2：
#
#  输入：graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
# 输出：1
#
#
#  示例 3：
#
#  输入：graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 < graph.length = graph[0].length <= 300
#  0 <= graph[i][j] == graph[j][i] <= 1
#  graph[i][i] = 1
#  1 <= initial.length < graph.length
#  0 <= initial[i] < graph.length
#
#  Related Topics 深度优先搜索 并查集 图
#  👍 38 👎 0

# dfs 找图里最近的未感染的点
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph)
        cleans = set(range(n)) - set(initial)
        indected_bynode = collections.defaultdict(set)

        def dfs(root, node, seen):
            for nxt in range(n):
                if graph[node][nxt] == 1 and nxt in cleans and nxt not in seen:
                    seen.add(nxt)
                    indected_bynode[nxt].add(root)
                    dfs(root, nxt, seen)

        for root in initial:
            dfs(root, root, set())
        count = [0] * n
        for cleannode, malnodes in indected_bynode.items():
            if len(malnodes) == 1:
                count[list(malnodes)[0]] += 1
        ans = min(initial)
        flag = -1
        for i in sorted(initial):
            if count[i] > flag:
                ans = i
                flag = count[i]
        return ans


# 2并查集
class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        f = {}
        n = len(graph)
        size = collections.defaultdict(lambda: 1)

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                f[b] = a
                size[a] += size[b]

        cleans = set(range(n)) - set(initial)
        for i in range(n):
            for j in range(n):
                if i != j and i in cleans and j in cleans and graph[i][j] == 1:
                    union(i, j)
        initial.sort()
        m = collections.defaultdict(set)
        for node in initial:
            for nxt in range(n):
                if nxt in cleans and graph[node][nxt]:
                    m[find(nxt)].add(node)
        count = [0] * n
        for clean_o, malnodes in m.items():
            if len(malnodes) == 1:
                count[malnodes.pop()] += size[clean_o]
        ans = initial[0]
        flag = 0
        for i in range(n):
            if count[i] > flag:
                ans = i
                flag = count[i]
        return ans


Solution().minMalwareSpread([[1,0,0,0,0,1,0],[0,1,1,0,0,0,0],[0,1,1,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[1,0,0,0,0,1,0],[0,0,0,0,0,0,1]], [4])
