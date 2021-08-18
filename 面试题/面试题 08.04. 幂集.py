#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 幂集。编写一种方法，返回某集合的所有子集。集合中不包含重复的元素。
#
#  说明：解集不能包含重复的子集。
#
#  示例:
#
#   输入： nums = [1,2,3]
#  输出：
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#
#  Related Topics 位运算 数组 回溯
#  👍 67 👎 0


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(i, path):
            if i == n:
                ans.append(path)
                return
            dfs(i+1,path+[nums[i]])
            dfs(i+1,path)


        dfs(0, [])
        return ans


Solution().subsets([1, 2, 3])
