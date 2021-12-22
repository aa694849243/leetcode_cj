# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个二叉树的根节点 root ，请你将此二叉树上下翻转，并返回新的根节点。
#
#  你可以按下面的步骤翻转一棵二叉树：
#
#
#  原来的左子节点变成新的根节点
#  原来的根节点变成新的右子节点
#  原来的右子节点变成新的左子节点
#
#
#  上面的步骤逐层进行。题目数据保证每个右节点都有一个同级节点（即共享同一父节点的左节点）且不存在子节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,4,5]
# 输出：[4,5,2,null,null,3,1]
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 10] 内
#  1 <= Node.val <= 10
#  树中的每个右节点都有一个同级节点（即共享同一父节点的左节点）
#  树中的每个右节点都没有子节点
#
#  Related Topics 树 深度优先搜索 二叉树 👍 87 👎 0


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent = parent_right = None
        while root:
            root_left = root.left
            root.left = parent_right
            parent_right = root.right
            root.right = parent
            parent = root
            root = root_left
        return parent


from trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[1,2,3,4,5]')
Solution().upsideDownBinaryTree(a)
