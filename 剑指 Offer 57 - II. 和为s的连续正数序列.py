#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
#
#
#  示例 1：
#
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#
#
#  示例 2：
#
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#
#
#
#
#  限制：
#
#
#  1 <= target <= 10^5
#
#
#
#  Related Topics 数学 双指针 枚举
#  👍 292 👎 0


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        l = 0
        cum = 0
        ans = []
        li = list(range(1, (target + 1) // 2 + 1))
        for i, val in enumerate(li):
            cum += val
            while cum > target:
                cum -= li[l]
                l += 1
            if cum==target:
                ans.append(li[l:i+1])
        return ans
