#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
#
#  返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。
#
#  示例 1:
#
#
# 输入: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","
# L","M"]
#
# 输出: ["A","1","B","C","D","2","3","4","E","5","F","G","6","7"]
#
#
#  示例 2:
#
#
# 输入: ["A","A"]
#
# 输出: []
#
#
#  提示：
#
#
#  array.length <= 100000
#
#  Related Topics 数组 哈希表 前缀和
#  👍 38 👎 0


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        if not array:
            return []
        nums, chs = [], []
        m = {0: -1}
        ma, l = 0, 0
        for i, val in enumerate(array):
            if val.isdigit():
                if nums:
                    nums.append(nums[-1] + 1)
                else:
                    nums.append(1)
                if chs:
                    chs.append(chs[-1])
                else:
                    chs.append(0)
            else:
                if nums:
                    nums.append(nums[-1])
                else:
                    nums.append(0)
                if chs:
                    chs.append(chs[-1] + 1)
                else:
                    chs.append(1)
            dif = nums[-1] - chs[-1]
            if dif in m and i - m[dif] > ma:
                ma = i - m[dif]
                l = m[dif]
            if dif not in m:
                m[dif] = i
        return array[l+1:l + ma+1]
Solution().findLongestSubarray(["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"])