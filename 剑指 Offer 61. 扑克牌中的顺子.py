#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任
# 意数字。A 不能视为 14。
#
#
#
#  示例 1:
#
#  输入: [1,2,3,4,5]
# 输出: True
#
#
#
#  示例 2:
#
#  输入: [0,0,1,2,5]
# 输出: True
#
#
#
#  限制：
#
#  数组长度为 5
#
#  数组的数取值为 [0, 13] .
#  Related Topics 数组 排序
#  👍 148 👎 0


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        clown = 0
        p = -1
        for num in nums:
            if num == 0:
                clown += 1
            elif p == -1 or num - p == 1:
                p = num
            elif num - p > 1:
                clown -= num - p - 1
                if clown < 0:
                    return False
                p = num
            elif num==p:
                return False
        return True
