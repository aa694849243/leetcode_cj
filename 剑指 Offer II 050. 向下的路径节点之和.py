# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 23:00 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.ans = 0

        def dfs(node, lst):
            if not node:
                return
            lst = [node.val + i for i in lst] + [node.val]
            self.ans += lst.count(targetSum)
            dfs(node.left, lst)
            dfs(node.right, lst)

        dfs(root, [])
        return self.ans

# leetcode submit region end(Prohibit modification and deletion)
