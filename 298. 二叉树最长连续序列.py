#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给你一棵指定的二叉树的根节点 root ，请你计算其中 最长连续序列路径 的长度。
#
#  最长连续序列路径 是依次递增 1 的路径。该路径，可以是从某个初始节点到树中任意节点，通过「父 - 子」关系连接而产生的任意路径。且必须从父节点到子节点，
# 反过来是不可以的。
#
#
#  示例 1：
#
#
# 输入：root = [1,null,3,2,4,null,null,null,5]
# 输出：3
# 解释：当中，最长连续序列是 3-4-5 ，所以返回结果为 3 。
#
#
#  示例 2：
#
#
# 输入：root = [2,null,3,2,null,1]
# 输出：2
# 解释：当中，最长连续序列是 2-3 。注意，不是 3-2-1，所以返回 2 。
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [1, 3 * 104] 内
#  -3 * 104 <= Node.val <= 3 * 104
#
#  Related Topics 树 深度优先搜索 二叉树
#  👍 78 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 1

        def dfs(node, pre, leng):
            if not node:
                self.res = max(self.res, leng)
                return
            if node.val == pre + 1:
                self.res = max(self.res, leng + 1)
                dfs(node.left, node.val, leng + 1)
                dfs(node.right, node.val, leng + 1)
            else:
                self.res = max(self.res, leng)
                dfs(node.left, node.val, 1)
                dfs(node.right, node.val, 1)

        dfs(root.left, root.val, 1)
        dfs(root.right, root.val, 1)
        return self.res
