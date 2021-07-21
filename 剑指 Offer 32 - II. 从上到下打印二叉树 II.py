#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
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
#  返回其层次遍历结果：
#
#  [
#   [3],
#   [9,20],
#   [15,7]
# ]
#
#
#
#
#  提示：
#
#
#  节点总数 <= 1000
#
#
#  注意：本题与主站 102 题相同：https://leetcode-cn.com/problems/binary-tree-level-order-tra
# versal/
#  Related Topics 树 广度优先搜索 二叉树
#  👍 123 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans=[]
        t=[root]
        while True:
            tree=[]
            ans.append([])
            for nod in t:
                ans[-1].append(nod.val)
                if nod.left:
                    tree.append(nod.left)
                if nod.right:
                    tree.append(nod.right)
            if not tree:
                break
            t=tree
        return ans
