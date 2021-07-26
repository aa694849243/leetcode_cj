#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一棵二叉树，其中每个节点都含有一个整数数值(该值或正或负)。设计一个算法，打印节点数值总和等于某个给定值的所有路径的数量。注意，路径不一定非得从二叉树的
# 根节点或叶节点开始或结束，但是其方向必须向下(只能从父节点指向子节点方向)。
#
#  示例:
# 给定如下二叉树，以及目标和 sum = 22，
#
#                5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
#
#
#  返回:
#
#  3
# 解释：和为 22 的路径有：[5,4,11,2], [5,8,4,5], [4,11,7]
#
#  提示：
#
#
#  节点总数 <= 10000
#
#  Related Topics 树 深度优先搜索 二叉树
#  👍 79 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.ans = 0

        def dfs(node, cum):
            if not node:
                return
            if node.val + cum == sum:
                self.ans += 1
            dfs(node.left, cum + node.val)
            dfs(node.right, cum+node.val)

        def dfs2(node):
            if not node:
                return
            dfs(node, 0)
            dfs2(node.left)
            dfs2(node.right)
        dfs2(root)
        return self.ans