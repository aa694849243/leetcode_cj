# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个 每个结点的值互不相同 的二叉树，和一个目标值 k，找出树中与目标值 k 最近的叶结点。
#
#  这里，与叶结点 最近 表示在二叉树中到达该叶节点需要行进的边数与到达其它叶结点相比最少。而且，当一个结点没有孩子结点时称其为叶结点。
#
#  在下面的例子中，输入的树以逐行的平铺形式表示。实际上的有根树 root 将以TreeNode对象的形式给出。
#
#  示例 1：
#
#  输入：
# root = [1, 3, 2], k = 1
# 二叉树图示：
#           1
#          / \
#         3   2
#
# 输出： 2 (或 3)
#
# 解释： 2 和 3 都是距离目标 1 最近的叶节点。
#
#
#
#
#  示例 2：
#
#  输入：
# root = [1], k = 1
# 输出：1
#
# 解释： 最近的叶节点是根结点自身。
#
#
#
#
#  示例 3：
#
#  输入：
# root = [1,2,3,4,null,null,null,5,null,6], k = 2
# 二叉树图示：
#              1
#             / \
#            2   3
#           /
#          4
#         /
#        5
#       /
#      6
#
# 输出：3
# 解释： 值为 3（而不是值为 6）的叶节点是距离结点 2 的最近结点。
#
#
#
#
#  注：
#
#
#  root 表示的二叉树最少有 1 个结点且最多有 1000 个结点。
#  每个结点都有一个唯一的 node.val ，范围为 [1, 1000]。
#  给定的二叉树中有某个结点使得 node.val == k。
#
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 79 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 树变图
class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.node = None
        g = collections.defaultdict(list)

        def dfs(node):
            if not node:
                return
            if node.val == k:
                self.node = node
            if node.left:
                g[node].append(node.left)
                g[node.left].append(node)
                dfs(node.left)
            if node.right:
                g[node].append(node.right)
                g[node.right].append(node)
                dfs(node.right)

        dfs(root)
        t = [self.node]
        visted = {self.node.val}
        while 1:
            tree = []
            for node in t:
                if not node.left and not node.right:
                    return node.val
                for nxt in g[node]:
                    if nxt.val not in visted:
                        visted.add(nxt.val)

                        tree.append(nxt)
            if not tree:
                break
            t = tree
        return -1


from trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[1,2,3,null,null,4,5,6,null,null,7,8,9,10]')
print(Solution().findClosestLeaf(a, 3))
