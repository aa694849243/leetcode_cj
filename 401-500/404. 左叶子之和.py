'''计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    num = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def dfs(root):
            if root:
                if root.left:
                    if not root.left.left and not root.left.right:
                        self.num += root.left.val
                    else:
                        dfs(root.left)
                if root.right:
                    dfs(root.right)

        dfs(root)
        return self.num
