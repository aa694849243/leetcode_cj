#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 给定一个升序整数数组，写一个函数搜索 nums 中数字 target。如果 target 存在，返回它的下标，否则返回 -1。注意，这个数组的大小是未知的。
# 你只可以通过 ArrayReader 接口访问这个数组，ArrayReader.get(k) 返回数组中第 k 个元素（下标从 0 开始）。
#
#  你可以认为数组中所有的整数都小于 10000。如果你访问数组越界，ArrayReader.get 会返回 2147483647。
#
#
#
#  样例 1：
#
#  输入: array = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 存在在 nums 中，下标为 4
#
#
#  样例 2：
#
#  输入: array = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不在数组中所以返回 -1
#
#
#
#  注释 ：
#
#
#  你可以认为数组中所有元素的值互不相同。
#  数组元素的值域是 [-9999, 9999]。
#
#  Related Topics 数组 二分查找 交互
#  👍 47 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader:
    def get(self, index: int) -> int:
        pass


class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        index = 1
        while reader.get(index) <= target or reader.get(index) != 2147483647:
            index *= 2
        l, r = 0, index
        while l < r:
            mid = (l + r) // 2
            if reader.get(mid) == 2147483647:
                r = mid
                continue
            if reader.get(mid) < target:
                l = mid + 1
            else:
                r = mid
        return l if reader.get(l)==target else -1
