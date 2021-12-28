#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一棵有 n 个结点的二叉树，你的任务是检查是否可以通过去掉树上的一条边将树分成两棵，且这两棵树结点之和相等。
#
#  样例 1:
#
#  输入:
#     5
#    / \
#   10 10
#     /  \
#    2   3
#
# 输出: True
# 解释:
#     5
#    /
#   10
#
# 和: 15
#
#    10
#   /  \
#  2    3
#
# 和: 15
#
#
#
#
#  样例 2:
#
#  输入:
#     1
#    / \
#   2  10
#     /  \
#    2   20
#
# 输出: False
# 解释: 无法通过移除一条树边将这棵树划分成结点之和相等的两棵子树。
#
#
#
#
#  注释 :
#
#
#  树上结点的权值范围 [-100000, 100000]。
#  1 <= n <= 10000
#
#
#
#  Related Topics 树 深度优先搜索 二叉树
#  👍 42 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: TreeNode) -> bool:
        self.sum_ = 0

        def dfs1(node):
            if not node:
                return
            self.sum_ += node.val
            dfs1(node.left)
            dfs1(node.right)

        dfs1(root)
        self.res = False

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if self.sum_ != 0 and (l == self.sum_ / 2 or r == self.sum_ / 2):
                self.res = True
                return 0
            elif self.sum_ == 0:
                if node.left and l == 0:
                    self.res = True
                    return 0
                if node.right and r == 0:
                    self.res = True
                    return 0
            return l + r + node.val

        dfs(root)
        return self.res
