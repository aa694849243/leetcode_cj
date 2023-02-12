# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 21:27 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        T = [root]
        ans = []
        while 1:
            tree = []
            tmp = -math.inf
            for node in T:
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
                tmp = max(tmp, node.val)
            ans.append(tmp)
            if not tree:
                break
            T = tree
        return ans
# leetcode submit region end(Prohibit modification and deletion)

