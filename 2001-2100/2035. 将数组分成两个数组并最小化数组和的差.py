# -*- coding: utf-8 -*-
# 给你一个长度为 2 * n 的整数数组。你需要将 nums 分成 两个 长度为 n 的数组，分别求出两个数组的和，并 最小化 两个数组和之 差的绝对值 。
# nums 中每个元素都需要放入两个数组之一。
#
#  请你返回 最小 的数组和之差。
#
#
#
#  示例 1：
#
#
#
#  输入：nums = [3,9,7,3]
# 输出：2
# 解释：最优分组方案是分成 [3,9] 和 [7,3] 。
# 数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。
#
#
#  示例 2：
#
#  输入：nums = [-36,36]
# 输出：72
# 解释：最优分组方案是分成 [-36] 和 [36] 。
# 数组和之差的绝对值为 abs((-36) - (36)) = 72 。
#
#
#  示例 3：
#
#
#
#  输入：nums = [2,-1,0,4,-2,-9]
# 输出：0
# 解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
# 数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。
#
#
#
#
#  提示：
#
#
#  1 <= n <= 15
#  nums.length == 2 * n
#  -10⁷ <= nums[i] <= 10⁷
#
#
#  Related Topics 位运算 数组 双指针 二分查找 动态规划 状态压缩 有序集合 👍 52 👎 0
import bisect
from typing import List
import itertools


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        nums1 = nums[:n]
        nums2 = nums[n:]
        sum_nums1 = sum(nums1)
        sum_nums2 = sum(nums2)
        res = abs(sum_nums1 - sum_nums2)
        for cnt1 in range(1, n):
            cnt2 = n - cnt1
            s1, s2 = set(), set()
            for left in itertools.combinations(nums1, cnt1):
                left_sum_neg = sum_nums1 - 2 * sum(left)
                s1.add(left_sum_neg)
            for right in itertools.combinations(nums2, cnt2):
                s2.add(2 * sum(right) - sum_nums2)
            tmp_s1 = sorted(s1)
            tmp_s2 = sorted(s2)
            for left_sum_neg in tmp_s1:
                idx = bisect.bisect_left(tmp_s2, left_sum_neg)
                if idx < len(tmp_s2):
                    res = min(res, -left_sum_neg + tmp_s2[idx])
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimumDifference([3, 9, 7, 3]))
