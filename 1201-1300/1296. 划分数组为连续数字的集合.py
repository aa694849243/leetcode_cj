# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一个整数数组 nums 和一个正整数 k，请你判断是否可以把这个数组划分成一些由 k 个连续数字组成的集合。
# 如果可以，请返回 True；否则，返回 False。
#
#
#
#  注意：此题目与 846 重复：https://leetcode-cn.com/problems/hand-of-straights/
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3,3,4,4,5,6], k = 4
# 输出：true
# 解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。
#
#
#  示例 2：
#
#
# 输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
# 输出：true
# 解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。
#
#
#  示例 3：
#
#
# 输入：nums = [3,3,2,2,1,1], k = 3
# 输出：true
#
#
#  示例 4：
#
#
# 输入：nums = [1,2,3,4], k = 3
# 输出：false
# 解释：数组不能分成几个大小为 3 的子数组。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10^5
#  1 <= nums[i] <= 10^9
#  1 <= k <= nums.length
#
#  Related Topics 贪心算法 数组
#  👍 53 👎 0


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        m = collections.Counter(nums)
        while True:
            a = min(m.keys())
            cnt = m[a]
            for i in range(k):
                if m[a] < cnt:
                    return False
                m[a] -= cnt
                if m[a] == 0:
                    m.pop(a)
                a += 1
            if not m:
                break
        return True
