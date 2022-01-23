# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一棵二叉树，请按以下要求的顺序收集它的全部节点：
#
#
#  依次从左到右，每次收集并删除所有的叶子节点
#  重复如上过程直到整棵树为空
#
#
#
#
#  示例:
#
#  输入: [1,2,3,4,5]
#  
#           1
#          / \
#         2   3
#        / \
#       4   5
#
# 输出: [[4,5,3],[2],[1]]
#
#
#
#
#  解释:
#
#  1. 删除叶子节点 [4,5,3] ，得到如下树结构：
#
#            1
#          /
#         2
#
#
#
#
#  2. 现在删去叶子节点 [2] ，得到如下树结构：
#
#            1
#
#
#
#
#  3. 现在删去叶子节点 [1] ，得到空树：
#
#            []
#
#  Related Topics 树 深度优先搜索 二叉树 👍 151 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        tmp = []
        if not root:
            return []
        def dfs(node):
            if not node.left and not node.right:
                tmp.append(node.val)
                return True
            l, r = True, True
            if not node.left:
                r = dfs(node.right)
            elif not node.right:
                l = dfs(node.left)
            else:
                l, r = dfs(node.left), dfs(node.right)
            if l:
                node.left = None
            if r:
                node.right = None
            return False

        while root.left or root.right:
            tmp = []
            dfs(root)
            res.append(tmp)
        res.append([root.val])
        return res
