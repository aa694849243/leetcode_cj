# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
#
#  你可以假定该序列中的数都是不相同的。
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
#  输入: [5,2,6,1,3]
# 输出: false
#
#  示例 2：
#
#  输入: [5,2,1,3,6]
# 输出: true
#
#  进阶挑战：
#
#  您能否使用恒定的空间复杂度来完成此题？
#  Related Topics 栈 树 二叉搜索树 递归 二叉树 单调栈 👍 131 👎 0

# 局部递减，整体递增
# https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree/solution/255-yan-zheng-qian-xu-bian-li-xu-lie-er-ubb4d/
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        stack = []
        minum = float('-inf')
        for num in preorder:
            if num < minum:
                return False
            while stack and stack[-1] < num:
                minum = stack.pop()
            stack.append(num)
        return True


Solution().verifyPreorder([5, 2, 1, 3, 6])
