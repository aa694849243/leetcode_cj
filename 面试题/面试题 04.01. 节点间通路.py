#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 节点间通路。给定有向图，设计一个算法，找出两个节点之间是否存在一条路径。
#
#  示例1:
#
#   输入：n = 3, graph = [[0, 1], [0, 2], [1, 2], [1, 2]], start = 0, target = 2
#  输出：true
#
#
#  示例2:
#
#   输入：n = 5, graph = [[0, 1], [0, 2], [0, 4], [0, 4], [0, 1], [1, 3], [1, 4], [
# 1, 3], [2, 3], [3, 4]], start = 0, target = 4
#  输出 true
#
#
#  提示：
#
#
#  节点数量n在[0, 1e5]范围内。
#  节点编号大于等于 0 小于 n。
#  图中可能存在自环和平行边。
#
#  Related Topics 深度优先搜索 广度优先搜索 图
#  👍 37 👎 0


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        if start==target:
            return True
        g = collections.defaultdict(set)
        for u, v in graph:
            g[u].add(v)
        t = [start]
        m = {start}
        while True:
            tree = []
            for node in t:
                for nxt in g[node]:
                    if nxt == target:
                        return True
                    if nxt not in m:
                        m.add(nxt)
                        tree.append(nxt)
            if not tree:
                break
            t = tree
        return False
