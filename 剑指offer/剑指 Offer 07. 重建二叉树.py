# -*- coding: utf-8 -*-
from typing import List


# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
#
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
#
#
#  示例 1:
#
#
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#
#
#  示例 2:
#
#
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#
#
#
#
#  限制：
#
#  0 <= 节点个数 <= 5000
#
#
#
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/
#  Related Topics 树 数组 哈希表 分治 二叉树
#  👍 505 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pl, pr, il, ir):
            if pr < pl:
                return
            node = TreeNode(preorder[pl])
            m = inorder.index(preorder[pl])
            cnt = m - il  # 左子树数量
            l = build(pl + 1, pl + cnt, il, m - 1)
            r = build(pl + cnt + 1, pr, m + 1, ir)
            node.left = l
            node.right = r
            return node

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])