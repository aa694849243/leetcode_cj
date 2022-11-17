# -*- coding: utf-8 -*-
# 给你两个 从小到大排好序 且下标从 0 开始的整数数组 nums1 和 nums2 以及一个整数 k ，请你返回第 k （从 1 开始编号）小的 nums1
# [i] * nums2[j] 的乘积，其中 0 <= i < nums1.length 且 0 <= j < nums2.length 。
#
#
#
#  示例 1：
#
#  输入：nums1 = [2,5], nums2 = [3,4], k = 2
# 输出：8
# 解释：第 2 小的乘积计算如下：
# - nums1[0] * nums2[0] = 2 * 3 = 6
# - nums1[0] * nums2[1] = 2 * 4 = 8
# 第 2 小的乘积为 8 。
#
#
#  示例 2：
#
#  输入：nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
# 输出：0
# 解释：第 6 小的乘积计算如下：
# - nums1[0] * nums2[1] = (-4) * 4 = -16
# - nums1[0] * nums2[0] = (-4) * 2 = -8
# - nums1[1] * nums2[1] = (-2) * 4 = -8
# - nums1[1] * nums2[0] = (-2) * 2 = -4
# - nums1[2] * nums2[0] = 0 * 2 = 0
# - nums1[2] * nums2[1] = 0 * 4 = 0
# 第 6 小的乘积为 0 。
#
#
#  示例 3：
#
#  输入：nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
# 输出：-6
# 解释：第 3 小的乘积计算如下：
# - nums1[0] * nums2[4] = (-2) * 5 = -10
# - nums1[0] * nums2[3] = (-2) * 4 = -8
# - nums1[4] * nums2[0] = 2 * (-3) = -6
# 第 3 小的乘积为 -6 。
#
#
#
#
#  提示：
#
#
#  1 <= nums1.length, nums2.length <= 5 * 10⁴
#  -10⁵ <= nums1[i], nums2[j] <= 10⁵
#  1 <= k <= nums1.length * nums2.length
#  nums1 和 nums2 都是从小到大排好序的。
#
#
#  Related Topics 数组 二分查找 👍 25 👎 0

from typing import List
import bisect


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        lneg, rneg = [], []
        lpos, rpos = [], []
        for num in nums1:
            if num < 0:
                lneg.append(num)
            else:
                lpos.append(num)
        for num in nums2:
            if num < 0:
                rneg.append(num)
            else:
                rpos.append(num)
        neg_sum = len(lneg) * len(rpos) + len(lpos) * len(rneg)
        lneg.sort(), lpos.sort(), rneg.sort(), rpos.sort()

        def find_pos_neg(llst, rlst, num):
            if not llst or not rlst:
                return 0
            cnt = 0
            for left in llst:
                if left == 0:
                    if num >= 0:
                        cnt += len(rlst)
                    continue
                pivot = num / left
                cnt += bisect.bisect_right(rlst, pivot)
            return cnt

        def find_neg_neg(llst, rlst, num):
            if not llst or not rlst:
                return 0
            cnt = 0
            for left in llst:
                pivot = num / left
                cnt += len(rlst) - bisect.bisect_left(rlst, pivot)
            return cnt

        def find_pos_pos(llst, rlst, num):
            if not llst or not rlst:
                return 0
            cnt = 0
            for left in llst:
                if left == 0:
                    if num >= 0:
                        cnt += len(rlst)
                    continue
                pivot = num / left
                cnt += bisect.bisect_right(rlst, pivot)
            return cnt

        if neg_sum >= k:
            l, r = -10 ** 10, 0
            while l < r:
                mid = (l + r) // 2
                cnt = find_pos_neg(lpos, rneg, mid) + find_pos_neg(rpos, lneg, mid)
                if cnt >= k:
                    r = mid
                else:
                    l = mid + 1
            return l
        else:
            k -= neg_sum
            l, r = 0, 10 ** 10
            while l < r:
                mid = (l + r) // 2
                cnt = find_pos_pos(lpos, rpos, mid) + find_neg_neg(lneg, rneg, mid)
                if cnt >= k:
                    r = mid
                else:
                    l = mid + 1
            return l


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().kthSmallestProduct(nums1=[-2, -1, 0, 1, 2], nums2=[-3, -1, 2, 4, 5], k=3))
