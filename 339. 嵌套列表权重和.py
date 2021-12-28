#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一个嵌套的整数列表 nestedList ，每个元素要么是整数，要么是列表。同时，列表中元素同样也可以是整数或者是另一个列表。
#
#  整数的 深度 是其在列表内部的嵌套层数。例如，嵌套列表 [1,[2,2],[[3],2],1] 中每个整数的值就是其深度。
#
#  请返回该列表按深度加权后所有整数的总和。
#
#
#
#  示例 1：
#
#
#
#
# 输入：nestedList = [[1,1],2,[1,1]]
# 输出：10
# 解释：因为列表中有四个深度为 2 的 1 ，和一个深度为 1 的 2。
#
#  示例 2：
#
#
# 输入：nestedList = [1,[4,[6]]]
# 输出：27
# 解释：一个深度为 1 的 1，一个深度为 2 的 4，一个深度为 3 的 6。所以，1 + 4*2 + 6*3 = 27。
#
#  示例 3：
#
#
# 输入：nestedList = [0]
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= nestedList.length <= 50
#  嵌套列表中整数的值在范围 [-100, 100] 内
#  任何整数的最大 深度 都小于或等于 50
#
#  Related Topics 深度优先搜索 广度优先搜索
#  👍 75 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:

        def dfs(nest: List[NestedInteger], depth):
            ans = 0
            for nxt in nest:
                if nxt.isInteger():
                    ans += nxt.getInteger() * depth
                else:
                    ans += dfs(nxt.getList(), depth + 1)
            return ans

        return dfs(nestedList, 1)
