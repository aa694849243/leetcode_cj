'''
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def rec(Node1, Node2):
            if not Node1 and not Node2:
                return True
            if not Node1 or not Node2:
                return False
            if Node1.val != Node2.val:
                return False
            a = rec(Node1.left, Node2.right)
            b = rec(Node1.right, Node2.left)
            return a and b

        if not root:
            return False
        return rec(root.left, root.right)


# 迭代
from collections import deque


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return True

        if not root:
            return True
        deq = deque([(root.left, root.right), ])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.right))
                deq.append((p.right, q.left))
        return True
