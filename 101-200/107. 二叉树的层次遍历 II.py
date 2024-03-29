'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# 层序遍历
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = [root]
        res = []
        while True:
            trees = []
            ans = []
            for node in stack:
                if not node:
                    continue
                ans.append(node.val)
                trees.append(node.left)
                trees.append(node.right)
            if not trees:
                break
            stack = trees
            res.append(ans)
        res.reverse()
        return res


from leetcode.trick.treenode.T import stringToTreeNode

root = stringToTreeNode('[3,9,20,null,null,15,7]')
Solution().levelOrderBottom(root)
