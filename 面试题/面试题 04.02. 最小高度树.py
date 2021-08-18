#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。示例: 给定有序数组: [-10,-3,0,5,9], 一个可能
# 的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：           0          / \        -3
#   9        /   /      -10  5 Related Topics 树 二叉搜索树 数组 分治 二叉树
#  👍 95 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def dfs(li):
            if not li:
                return None
            mid = len(li) // 2
            node = TreeNode(li[mid])
            node.left = dfs(li[:mid])
            node.right = dfs(li[mid + 1:])
            return node
        return dfs(nums)