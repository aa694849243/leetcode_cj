#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。
#
#  示例 1：
#
#  输入：[1,0,1,1,0]
# 输出：4
# 解释：翻转第一个 0 可以得到最长的连续 1。
#      当翻转以后，最大连续 1 的个数为 4。
#
#
#
#
#  注：
#
#
#  输入数组只包含 0 和 1.
#  输入数组的长度为正整数，且不超过 10,000
#
#
#
#
#  进阶：
# 如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？
#  Related Topics 数组 动态规划 滑动窗口
#  👍 85 👎 0


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        pre, cnt = 0, 0
        res = 0
        for num in nums:
            cnt += 1
            if num == 0:
                pre = cnt
                cnt = 0
            res = max(res, pre + cnt)
        return res


# 对于无限流数据
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = -1
        pq = collections.deque()
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                pq.append(r)
            while len(pq) >= 2:
                l = pq.popleft()
            res = max(res, r - l)
        return res


Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0])
