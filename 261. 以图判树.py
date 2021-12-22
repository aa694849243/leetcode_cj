# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定从 0 到 n-1 标号的 n 个结点，和一个无向边列表（每条边以结点对来表示），请编写一个函数用来判断这些边是否能够形成一个合法有效的树结构。
#
#  示例 1：
#
#  输入: n = 5, 边列表 edges = [[0,1], [0,2], [0,3], [1,4]]
# 输出: true
#
#  示例 2:
#
#  输入: n = 5, 边列表 edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# 输出: false
#
#  注意：你可以假定边列表 edges 中不会出现重复的边。由于所有的边是无向边，边 [0,1] 和边 [1,0] 是相同的，因此不会同时出现在边列表
# edges 中。
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 147 👎 0


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n != len(edges) + 1:
            return False
        if not edges:
            return True
        visted = {0}
        g = collections.defaultdict(set)
        for vi, vj in edges:
            g[vi].add(vj)
            g[vj].add(vi)
        t = [0]
        while 1:
            tree = []
            for node in t:
                for nxt in g[node]:
                    if nxt not in visted:
                        tree.append(nxt)
                        visted.add(nxt)
            if not tree:
                break
            t = tree
        return len(visted)==n
Solution().validTree(5, [[0,1],[0,2],[0,3],[1,4]])