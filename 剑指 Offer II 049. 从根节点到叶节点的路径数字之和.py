# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 22:57 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, pre):
            if not node.left and not node.right:
                self.ans += pre * 10 + node.val
                return
            if node.left:
                dfs(node.left, pre * 10 + node.val)
            if node.right:
                dfs(node.right, pre * 10 + node.val)
        dfs(root, 0)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)

