# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 23:14 
# ide： PyCharm
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        cur, pre = root, None
        stk = []
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            if pre == p:
                return cur
            pre = cur
            cur = cur.right
        return None

# leetcode submit region end(Prohibit modification and deletion)
