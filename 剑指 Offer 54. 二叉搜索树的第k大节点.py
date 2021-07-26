#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一棵二叉搜索树，请找出其中第k大的节点。
#
#
#
#  示例 1:
#
#  输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4
#
#  示例 2:
#
#  输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4
#
#
#
#  限制：
#
#  1 ≤ k ≤ 二叉搜索树元素个数
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树
#  👍 180 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.ans = -1
        self.cnt = 0

        def dfs(node):
            if not node:
                return
            dfs(node.right)
            if self.cnt >= k:
                return
            self.cnt += 1
            if self.cnt >= k:
                self.ans = node.val
            else:
                dfs(node.left)

        dfs(root)
        return self.ans


from leetcode.trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[3,1,4,null,2]')
Solution().kthLargest(a,1)