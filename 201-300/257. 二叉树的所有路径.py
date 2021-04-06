'''
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
from leetcode.trick.treenode.T import stringToTreeNode


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []

        def rec(node, s):
            s = s + str(node.val) + '->'
            if not node.left and not node.right:
                res.append(s[:-2])
            else:
                if not node.left:
                    rec(node.right, s)
                elif not node.right:
                    rec(node.left, s)
                else:
                    rec(node.left, s)
                    rec(node.right, s)

        rec(root, '')
        return res
#迭代
class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths


# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / binary - tree - paths / solution / er - cha - shu - de - suo - you - lu - jing - by - leetcode /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

a = stringToTreeNode('[1,2,3,null,5]')
Solution().binaryTreePaths(a)
