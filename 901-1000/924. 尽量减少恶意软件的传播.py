# 在节点网络中，只有当 graph[i][j] = 1 时，每个节点 i 能够直接连接到另一个节点 j。
#
#  一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传
# 播将继续，直到没有更多的节点可以被这种方式感染。
#
#  假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。
#
#  我们可以从初始列表中删除一个节点。如果移除这一节点将最小化 M(initial)， 则返回该节点。如果有多个节点满足条件，就返回索引最小的节点。
#
#  请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后可能仍然因恶意软件传播而受到感染。
#
#
#
#
#
#
#  示例 1：
#
#  输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0
#
#
#  示例 2：
#
#  输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
# 输出：0
#
#
#  示例 3：
#
#  输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
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
#  graph[i][i] == 1
#  1 <= initial.length < graph.length
#  0 <= initial[i] < graph.length
#
#  Related Topics 深度优先搜索 并查集
#  👍 59 👎 0


from typing import List

import collections


class Solution:
    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        f = {}
        size = collections.defaultdict(lambda: 1)
        n = len(graph)

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

        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                if graph[node1][node2] == 1:
                    union(node1, node2)
        malcal = collections.Counter()
        for malnode in initial:
            malcal[find(malnode)] += 1
        flag = 0
        initial.sort()
        ans = initial[0]
        for node in initial:
            if malcal[find(node)] == 1:
                if size[find(node)] > flag:
                    ans = node
                    flag = size[find(node)]
        return ans


Solution().minMalwareSpread(graph=[[1, 1, 1], [1, 1, 1], [1, 1, 1]], initial=[1, 2])
