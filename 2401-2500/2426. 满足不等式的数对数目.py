# -*- coding: utf-8 -*-
# 给你两个下标从 0 开始的整数数组 nums1 和 nums2 ，两个数组的大小都为 n ，同时给你一个整数 diff ，统计满足以下条件的 数对 (i,
# j) ：
#
#
#  0 <= i < j <= n - 1 且
#  nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
#
#
#  请你返回满足条件的 数对数目 。
#
#
#
#  示例 1：
#
#  输入：nums1 = [3,2,5], nums2 = [2,2,1], diff = 1
# 输出：3
# 解释：
# 总共有 3 个满足条件的数对：
# 1. i = 0, j = 1：3 - 2 <= 2 - 2 + 1 。因为 i < j 且 1 <= 1 ，这个数对满足条件。
# 2. i = 0, j = 2：3 - 5 <= 2 - 1 + 1 。因为 i < j 且 -2 <= 2 ，这个数对满足条件。
# 3. i = 1, j = 2：2 - 5 <= 2 - 1 + 1 。因为 i < j 且 -3 <= 2 ，这个数对满足条件。
# 所以，我们返回 3 。
#
#
#  示例 2：
#
#  输入：nums1 = [3,-1], nums2 = [-2,2], diff = -1
# 输出：0
# 解释：
# 没有满足条件的任何数对，所以我们返回 0 。
#
#
#
#
#  提示：
#
#
#  n == nums1.length == nums2.length
#  2 <= n <= 10⁵
#  -10⁴ <= nums1[i], nums2[i] <= 10⁴
#  -10⁴ <= diff <= 10⁴
#
#
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序
#  👍 12 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 逆序对
class FenWickTree:
    def __init__(self, n):
        self.n = n
        self.li = [0] * (n + 1)

    @staticmethod
    def lowbit(num):
        return num & -num

    def update(self, num, dt):
        while num <= self.n:
            self.li[num] += dt
            num += self.lowbit(num)

    def query(self, num):
        cnt = 0
        while num > 0:
            cnt += self.li[num]
            num -= self.lowbit(num)
        return cnt


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        nums = [(nums1[i] - nums2[i]) for i in range(len(nums1))]
        ranks = {}
        nums_diff = sorted(set(nums + [num + diff for num in nums]))
        for i, num in enumerate(nums_diff):
            ranks[num] = i + 1
        ans = 0
        ftree = FenWickTree(len(nums_diff))
        for num in nums:
            ans += ftree.query(ranks[num + diff])
            ftree.update(ranks[num], 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
