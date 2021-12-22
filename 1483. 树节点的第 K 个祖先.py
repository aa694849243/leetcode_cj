# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一棵树，树上有 n 个节点，按从 0 到 n-1 编号。树以父节点数组的形式给出，其中 parent[i] 是节点 i 的父节点。树的根节点是编号为 0
#  的节点。
#
#  请你设计并实现 getKthAncestor(int node, int k) 函数，函数返回节点 node 的第 k 个祖先节点。如果不存在这样的祖先节
# 点，返回 -1 。
#
#  树节点的第 k 个祖先节点是从该节点到根节点路径上的第 k 个节点。
#
#
#
#  示例：
#
#
#
#  输入：
# ["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
# [[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]
#
# 输出：
# [null,1,0,-1]
#
# 解释：
# TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);
#
# treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
# treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
# treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点
#
#
#
#
#  提示：
#
#
#  1 <= k <= n <= 5*10^4
#  parent[0] == -1 表示编号为 0 的节点是根节点。
#  对于所有的 0 < i < n ，0 <= parent[i] < n 总成立
#  0 <= node < n
#  至多查询 5*10^4 次
#
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 二分查找 动态规划 👍 86 👎 0


class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.dp = [[-1] * 19 for _ in range(n + 1)]
        for vi, vj in enumerate(parent):  # dp[i][j]表示i节点的第2**(j)个祖先
            self.dp[vi][0] = vj
        for j in range(1, 19):  # 当求node的第10个祖先时，结果为: dp[dp[node][2^3]][2^1]，和幂运算类似，底数不变，指数相加
            for i in range(n):
                self.dp[i][j] = self.dp[self.dp[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        res = node
        li = [*map(int, bin(res)[2:])][::-1]
        while 1:
            num = li.pop()
            if num & 1:
                res = self.dp[res][len(li)]
            if not li:
                break
        return res

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
