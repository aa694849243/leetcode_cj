#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
#
#
#
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
#  示例 1:
#
#  输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2
#
#
#
#  限制：
#
#  1 <= 数组长度 <= 50000
#
#
#
#  注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/
#
#
#  Related Topics 数组 哈希表 分治 计数 排序
#  👍 174 👎 0


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        flg = None
        for num in nums:
            if num == flg:
                cnt += 1
            else:
                if cnt == 0:
                    flg = num
                    cnt = 1
                else:
                    cnt -= 1
        return flg

Solution().majorityElement([1,2,3,2,2,2,5,4,2])
