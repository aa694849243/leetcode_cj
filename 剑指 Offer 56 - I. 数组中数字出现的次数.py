#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#
#
#
#  示例 1：
#
#  输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
#
#
#  示例 2：
#
#  输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]
#
#
#
#  限制：
#
#
#  2 <= nums.length <= 10000
#
#
#
#  Related Topics 位运算 数组
#  👍 432 👎 0


class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        x = 0
        for num in nums:
            x ^= num
        flag = x & (-x)
        ans1=0
        ans2=0
        for num in nums:
            if num&flag:
                ans1^=num
            else:
                ans2^=num
        return [ans1,ans2]