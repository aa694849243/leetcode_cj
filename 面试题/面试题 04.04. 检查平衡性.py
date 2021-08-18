#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 实现一个函数，检查二叉树是否平衡。在这个问题中，平衡树的定义如下：任意一个节点，其两棵子树的高度差不超过 1。 示例 1: 给定二叉树 [3,9,20,nu
# ll,null,15,7]     3    / \   9  20     /  \    15   7 返回 true 。示例 2: 给定二叉树 [1,2,
# 2,3,3,null,null,4,4]       1      / \     2   2    / \   3   3  / \ 4   4 返回 fal
# se 。 Related Topics 树 深度优先搜索 二叉树
#  👍 64 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.ans = True

        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if abs(l - r) > 1:
                self.ans = False
            return max(l, r) + 1

        dfs(root)
        return self.ans