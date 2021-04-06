'''给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

 



 

返回其前序遍历: [1,3,5,6,2,4]。

 

说明: 递归法很简单，你可以使用迭代法完成此题吗?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


from typing import List


# 1递归
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def rec(root):
            if not root:
                return
            res.append(root.val)
            for node in root.children:
                rec(node)

        rec(root)
        return res


# 2非递归


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            stack.extend(node.children[::-1])
        return res


l2 = Node(2)
l3 = Node(3, [Node(5), Node(6)])
l1 = Node(1, [l3, l2])
Solution().preorder(l1)
