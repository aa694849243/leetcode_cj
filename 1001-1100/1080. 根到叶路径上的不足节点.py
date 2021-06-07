# -*- coding: utf-8 -*-
# 给定一棵二叉树的根 root，请你考虑它所有 从根到叶的路径：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）
#
#  假如通过节点 node 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 limit，则该节点被称之为「不足节点」，需要被删除。
#
#  请你删除所有不足节点，并返回生成的二叉树的根。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
#
# 输出：[1,2,3,4,null,null,7,8,9,null,14]
#
#
#  示例 2：
#
#
# 输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
#
# 输出：[5,4,8,11,null,17,4,7,null,null,null,5]
#
#  示例 3：
#
#
# 输入：root = [5,-6,-6], limit = 0
# 输出：[]
#
#
#
#  提示：
#
#
#  给定的树有 1 到 5000 个节点
#  -10^5 <= node.val <= 10^5
#  -10^9 <= limit <= 10^9
#
#
#
#  Related Topics 深度优先搜索
#  👍 36 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 考虑每个节点左右两颗子树是否应该删除
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        def dfs(node, pre):
            if not node.left and not node.right: #叶子节点不用考虑左右节点被删的问题
                return node.val + pre < limit  # 需要删除
            l_delete = True
            r_delete = True  # 默认都要删
            if node.left:
                l_delete = dfs(node.left, pre + node.val)
            if node.right:
                r_delete = dfs(node.right, pre + node.val)
            if l_delete:
                node.left = None
            if r_delete:
                node.right = None
            return l_delete and r_delete # 如果两颗子树都删了，说明这个节点也要删

        a=dfs(root, 0)
        return root if not a else None


from leetcode.trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[1,2,-3,-5,null,4,null]')

Solution().sufficientSubset(a, -1)
