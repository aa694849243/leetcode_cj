# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个二叉树，统计该二叉树数值相同的子树个数。
#
#  同值子树是指该子树的所有节点都拥有相同的数值。
#
#  示例：
#
#  输入: root = [5,1,5,5,5,null,5]
#
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
#
# 输出: 4
#
#  Related Topics 树 深度优先搜索 二叉树 👍 88 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.c = 0

        def dfs(node):
            if not node.left and not node.right:
                self.c += 1
                return True
            uni = True
            if node.left:
                uni = dfs(node.left) and node.left.val == node.val
            if node.right:
                uni = dfs(node.right) and node.right.val == node.val and uni
            self.c += int(uni)
            return uni
        dfs(root)
        return self.c
