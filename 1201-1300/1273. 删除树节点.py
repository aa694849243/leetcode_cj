# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一棵以节点 0 为根节点的树，定义如下：
#
#
#  节点的总数为 nodes 个；
#  第 i 个节点的值为 value[i] ；
#  第 i 个节点的父节点是 parent[i] 。
#
#
#  请你删除节点值之和为 0 的每一棵子树。
#
#  在完成所有删除之后，返回树中剩余节点的数目。
#
#
#
#  示例 1：
#
#
#
#  输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-1]
# 输出：2
#
#
#  示例 2：
#
#  输入：nodes = 7, parent = [-1,0,0,1,2,2,2], value = [1,-2,4,0,-2,-1,-2]
# 输出：6
#
#
#  示例 3：
#
#  输入：nodes = 5, parent = [-1,0,1,0,0], value = [-672,441,18,728,378]
# 输出：5
#
#
#  示例 4：
#
#  输入：nodes = 5, parent = [-1,0,0,1,1], value = [-686,-842,616,-739,-746]
# 输出：5
#
#
#
#
#  提示：
#
#
#  1 <= nodes <= 10^4
#  parent.length == nodes
#  0 <= parent[i] <= nodes - 1
#  parent[0] == -1 表示节点 0 是树的根。
#  value.length == nodes
#  -10^5 <= value[i] <= 10^5
#  题目输入数据 保证 是一棵 有效的树 。
#
#  Related Topics 树 深度优先搜索 广度优先搜索 👍 30 👎 0


class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        g = collections.defaultdict(list)
        for i in range(nodes):
            g[parent[i]].append(i)
        self.res = nodes

        def rec(node):
            if node != -1:
                node_num = 1
                cum = value[node]
            else:
                node_num = 0
                cum = 0
            for nxt in g[node]:
                a, b = rec(nxt)
                node_num += a
                cum += b
            if cum == 0 and node != -1:
                self.res -= node_num
                return 0, 0
            return node_num, cum

        rec(-1)
        return self.res


Solution().deleteTreeNodes(1, [-1], [0])
