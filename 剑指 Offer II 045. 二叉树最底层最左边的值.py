# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 21:29 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
    #         self.left = left
    #         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        T = [root]
        while 1:
            tree=[]
            for node in T:
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            if not tree:
                return T[0].val
            T = tree

# leetcode submit region end(Prohibit modification and deletion)

