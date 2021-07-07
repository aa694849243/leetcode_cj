# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
#
#
#  该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
#
#
#  如果不存在祖父节点值为偶数的节点，那么返回 0 。
#
#
#
#  示例：
#
#
#
#  输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：18
# 解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。
#
#
#
#
#  提示：
#
#
#  树中节点的数目在 1 到 10^4 之间。
#  每个节点的值在 1 到 100 之间。
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树
#  👍 55 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans=0
        def dfs(node,pre,prepre):
            if not node:
                return
            if prepre:
                if prepre.val%2==0:
                    self.ans+=node.val
            dfs(node.left,node,pre)
            dfs(node.right,node,pre)
        dfs(root,None,None)
        return self.ans

from leetcode.trick.treenode.T import stringToTreeNode
a=stringToTreeNode('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]')
Solution().sumEvenGrandparent(a)