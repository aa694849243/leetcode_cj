'''
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from leetcode.trick.treenode.T import stringToTreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def rec(node):
            if not node:
                return
            rec(node.left)
            rec(node.right)
            res.append(node.val)

        rec(root)

        return res


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        node = root
        stack = []
        res = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left if node.left else node.right
            node = stack.pop()
            res.append(node.val)
            if stack and stack[-1].left == node:
                node = stack[-1].right
            else:
                node = None
        return res


a = stringToTreeNode('[1,null,2,3]')
Solution().postorderTraversal(a)
