# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一棵二叉搜索树和其中的一个节点 p ，找到该节点在树中的中序后继。如果节点没有中序后继，请返回 null 。
#
#  节点 p 的后继是值比 p.val 大的节点中键值最小的节点。
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [2,1,3], p = 1
# 输出：2
# 解释：这里 1 的中序后继是 2。请注意 p 和返回值都应是 TreeNode 类型。
#
#
#  示例 2：
#
#
#
#
# 输入：root = [5,3,6,2,4,null,null,1], p = 6
# 输出：null
# 解释：因为给出的节点没有中序后继，所以答案就返回 null 了。
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [1, 10⁴] 内。
#  -10⁵ <= Node.val <= 10⁵
#  树中各节点的值均保证唯一。
#
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 138 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 非递归方式的中序遍历
class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right:  # 当有右子节点的情况，找到右子节点的最左端
            p = p.right
            while p.left:
                p = p.left
            return p
        stack = []
        inorder = float('inf')
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if inorder == p.val:
                return root
            else:
                inorder = root.val
            root = root.right
        return None
