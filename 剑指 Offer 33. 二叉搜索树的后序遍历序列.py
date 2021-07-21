#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。
#
#
#
#  参考以下这颗二叉搜索树：
#
#       5
#     / \
#    2   6
#   / \
#  1   3
#
#  示例 1：
#
#  输入: [1,6,3,2,5]
# 输出: false
#
#  示例 2：
#
#  输入: [1,3,2,6,5]
# 输出: true
#
#
#
#  提示：
#
#
#  数组长度 <= 1000
#
#  Related Topics 栈 树 二叉搜索树 递归 二叉树 单调栈
#  👍 302 👎 0


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        def dfs(li, mi, ma):
            if not li:
                return True
            root = li[-1]
            if root <= mi or root >= ma:
                return False
            l, r = [], []
            i = 0
            for i, val in enumerate(li[:-1]):
                if val <= mi or val >= ma:
                    return False
                if val > root:
                    break
                l.append(val)
            else:
                i += 1
            r = li[i:-1]
            return dfs(l, mi, root) and dfs(r, root, ma)

        return dfs(postorder, float('-inf'), float('inf'))


Solution().verifyPostorder([4, 6, 7, 5])
