# -*- coding: utf-8 -*-
import collections
from typing import List


# 力扣数据中心有 n 台服务器，分别按从 0 到 n-1 的方式进行了编号。
#
#  它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 connections 是无向的。
#
#  从形式上讲，connections[i] = [a, b] 表示服务器 a 和 b 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器
# 。
#
#  「关键连接」是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。
#
#  请你以任意顺序返回该集群内的所有 「关键连接」。
#
#
#
#  示例 1：
#
#
#
#  输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# 输出：[[1,3]]
# 解释：[[3,1]] 也是正确的。
#
#
#
#  提示：
#
#
#  1 <= n <= 10^5
#  n-1 <= connections.length <= 10^5
#  connections[i][0] != connections[i][1]
#  不存在重复的连接
#
#  Related Topics 深度优先搜索
#  👍 138 👎 0

# tarjan 桥
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(set)
        dfn = [-1] * n
        low = [-1] * n
        for vi, vj in connections:
            g[vi].add(vj)
            g[vj].add(vi)
        ans = []

        def dfs(parent, node, timestamp):
            dfn[node] = timestamp
            low[node] = timestamp
            for child in g[node]:
                if child == parent:
                    continue
                if low[child] == -1:  # 没有访问过
                    low[node] = min(low[node], dfs(node, child, timestamp + 1))
                else:
                    low[node] = min(low[node], low[child])
            if node != 0 and low[node] > dfn[parent]:#root节点的父节点为dummynode，不考虑
                ans.append([parent, node])
            return low[node]

        dfs(-1, 0, 0)
        return ans
