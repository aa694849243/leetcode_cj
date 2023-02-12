# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 22:18 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        H = TreeNode(1)
        H.left = root

        def dfs(node):
            if not node.left and not node.right:
                return node, node.val == 1
            flag_left = flag_right = False
            if node.left:
                left, flag_left = dfs(node.left)
                if not flag_left:
                    node.left = None
            if node.right:
                right, flag_right = dfs(node.right)
                if not flag_right:
                    node.right = None
            return node, node.val == 1 or flag_left or flag_right

        node, flag = dfs(H)
        return node.left

# leetcode submit region end(Prohibit modification and deletion)
