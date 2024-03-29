#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
#
#
#
#  示例 1:
#
#  给定二叉树 [3,9,20,null,null,15,7]
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回 true 。
#
# 示例 2:
#
#  给定二叉树 [1,2,2,3,3,null,null,4,4]
#
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
#
#
#  返回 false 。
#
#
#
#  限制：
#
#
#  0 <= 树的结点个数 <= 10000
#
#
#  注意：本题与主站 110 题相同：https://leetcode-cn.com/problems/balanced-binary-tree/
#
#
#  Related Topics 树 深度优先搜索 二叉树
#  👍 177 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if l == -1 or r == -1 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        return True if dfs(root)!=-1 else False