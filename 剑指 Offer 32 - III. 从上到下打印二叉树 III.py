#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
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
#   [20,9],
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
#  Related Topics 树 广度优先搜索 二叉树
#  👍 113 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        ans = []
        t = [root]
        flag = 0
        while True:
            tree = []
            tmp = []
            for nod in t:
                tmp.append(nod.val)
                if nod.left:
                    tree.append(nod.left)
                if nod.right:
                    tree.append(nod.right)
            if flag%2:
                ans.append(tmp[::-1])
            else:
                ans.append(tmp)
            if not tree:
                break
            flag+=1
            t=tree
        return ans