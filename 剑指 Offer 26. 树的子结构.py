#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
#  B是A的子结构， 即 A中有出现和B相同的结构和节点值。
#
#  例如:
# 给定的树 A:
#
#  3
#  / \
#  4 5
#  / \
#  1 2
# 给定的树 B：
#
#  4
#  /
#  1
# 返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。
#
#  示例 1：
#
#  输入：A = [1,2,3], B = [3,1]
# 输出：false
#
#
#  示例 2：
#
#  输入：A = [3,4,5,1,2], B = [4,1]
# 输出：true
#
#  限制：
#
#  0 <= 节点个数 <= 10000
#  Related Topics 树 深度优先搜索 二叉树
#  👍 306 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B:
            return False
        def dfs(node1,node2):
            if not node2:
                return True
            if not node1:
                return False
            if node1.val==node2.val:
                return dfs(node1.left,node2.left) and dfs(node1.right,node2.right)
            return False
        def dfs2(node1,node2):
            if not node1:
                return False
            return dfs(node1,node2) or dfs2(node1.left,node2) or dfs2(node1.right,node2)
        return dfs2(A,B)
