# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。
#
#  我们用一个由所有「边」组成的数组 edges 来表示一棵无向树，其中 edges[i] = [u, v] 表示节点 u 和 v 之间的双向边。
#
#  树上的节点都已经用 {0, 1, ..., edges.length} 中的数做了标记，每个节点上的标记都是独一无二的。
#
#
#
#  示例 1：
#
#
#
#  输入：edges = [[0,1],[0,2]]
# 输出：2
# 解释：
# 这棵树上最长的路径是 1 - 0 - 2，边数为 2。
#
#
#  示例 2：
#
#
#
#  输入：edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
# 输出：4
# 解释：
# 这棵树上最长的路径是 3 - 2 - 1 - 4 - 5，边数为 4。
#
#
#
#
#  提示：
#
#
#  0 <= edges.length < 10^4
#  edges[i][0] != edges[i][1]
#  0 <= edges[i][j] <= edges.length
#  edges 会形成一棵无向树
#
#  Related Topics 树 深度优先搜索 广度优先搜索 👍 78 👎 0

# 两次bfs
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        g = collections.defaultdict(list)
        for vi, vj in edges:
            g[vi].append(vj)
            g[vj].append(vi)
        visted = set()
        visted.add(0)
        t = [0]
        while 1:
            tree = []
            for node in t:
                for nxt in g[node]:
                    if nxt not in visted:
                        visted.add(nxt)
                        tree.append(nxt)
            if not tree:
                p = t[0]
                break
            t = tree
        cnt = -1
        visted = {p}
        t = [p]
        while 1:
            tree = []
            cnt += 1
            for node in t:
                for nxt in g[node]:
                    if nxt not in visted:
                        tree.append(nxt)
                        visted.add(nxt)
            if len(tree)==0:
                break
            t = tree
        return cnt
print(Solution().treeDiameter([[0,1],[0,2]]))