# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 22:54 
# ide： PyCharm
# https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/solution/er-cha-shu-de-xu-lie-hua-yu-fan-xu-lie-hua-by-le-2/

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:
    def rserialize(self, root, string):
        # Recursive serialization.
        if root is None:
            string += "None,"
        else:
            string += str(root.val) + ","
            string = self.rserialize(root.left, string)
            string = self.rserialize(root.right, string)
        return string

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        return self.rserialize(root, "")

    def rdeserialize(self, lst):
        val = lst.popleft()
        if val == 'None':
            return None
        root = TreeNode(val)
        root.left = self.rdeserialize(lst)
        root.right = self.rdeserialize(lst)
        return root

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        lst = deque(data.split(','))
        return self.rdeserialize(lst)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
ser = Codec()
deser = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)
a = ser.serialize(root)
print(a)
b = deser.deserialize(a)
...
