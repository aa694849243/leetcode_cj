# -*- coding: utf-8 -*-
from typing import List


# 找出数组中重复的数字。
#
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
# 找出数组中任意一个重复的数字。
#
#  示例 1：
#
#  输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
#
#
#
#
#  限制：
#
#  2 <= n <= 100000
#  Related Topics 数组 哈希表 排序
#  👍 482 👎 0


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        flag = -1
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            if nums[num] == 0:
                if flag == -1:
                    flag = num
                elif flag == num:
                    return num
                else:
                    return 0
            else:
                nums[num]*=-1
Solution().findRepeatNumber([1, 1, 1])