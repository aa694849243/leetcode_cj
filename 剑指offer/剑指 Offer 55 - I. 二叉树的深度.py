#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
#
#  例如：
#
#  给定二叉树 [3,9,20,null,null,15,7]，
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最大深度 3 。
#
#
#
#  提示：
#
#
#  节点总数 <= 10000
#
#
#  注意：本题与主站 104 题相同：https://leetcode-cn.com/problems/maximum-depth-of-binary-tre
# e/
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树
#  👍 129 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, level):
            if not node:
                return
            self.ans = max(level, self.ans)
            dfs(node.left,level+1)
            dfs(node.right,level+1)

        dfs(root, 1)
        return self.ans
