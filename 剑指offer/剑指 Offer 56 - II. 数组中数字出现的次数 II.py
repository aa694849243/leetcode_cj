#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
#
#
#
#  示例 1：
#
#  输入：nums = [3,4,3,3]
# 输出：4
#
#
#  示例 2：
#
#  输入：nums = [9,1,7,9,7,9,7]
# 输出：1
#
#
#
#  限制：
#
#
#  1 <= nums.length <= 10000
#  1 <= nums[i] < 2^31
#
#
#
#  Related Topics 位运算 数组
#  👍 205 👎 0


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s_1, s_2 = 0, 0
        for num in nums:
            s_1 = ~s_2 & (s_1 ^ num)
            s_2 = ~s_1 & (s_2 ^ num)
        return s_1
