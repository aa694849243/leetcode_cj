# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-02 23:50 
# ide： PyCharm
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def expandBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return
            if node.left:
                l = node.left
                node.left = TreeNode(-1, node.left)
                node.left.left = l
                dfs(node.left.left)
            if node.right:
                r = node.right
                node.right = TreeNode(-1, None, node.right)
                node.right.right = r
                dfs(node.right.right)

        dfs(root)
        return root
# leetcode submit region end(Prohibit modification and deletion)
