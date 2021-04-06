'''给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :

 



 

返回其后序遍历: [5,6,3,2,4,1].

 

说明: 递归法很简单，你可以使用迭代法完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


# 1递归
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def rec(root):
            if not root:
                return
            for node in root.children:
                rec(node)
            res.append(root.val)

        rec(root)
        return res


# 2非递归
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node:
                stack.extend(node.children)
                res.append(node.val)
        return res[::-1]
