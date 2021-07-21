#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
#
#
#
#  例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#  返回：
#
#  [3,9,20,15,7]
#
#
#
#
#  提示：
#
#
#  节点总数 <= 1000
#
#  Related Topics 树 广度优先搜索 二叉树
#  👍 107 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        t = [root]
        while True:
            tree = []
            for nod in t:
                ans.append(nod.val)
                if nod.left:
                    tree.append(nod.left)
                if nod.right:
                    tree.append(nod.right)
            if not tree:
                break
            t = tree
        return ans
