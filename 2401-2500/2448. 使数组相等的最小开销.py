# -*- coding: utf-8 -*-
# 给你两个下标从 0 开始的数组 nums 和 cost ，分别包含 n 个 正 整数。
#
#  你可以执行下面操作 任意 次：
#
#
#  将 nums 中 任意 元素增加或者减小 1 。
#
#
#  对第 i 个元素执行一次操作的开销是 cost[i] 。
#
#  请你返回使 nums 中所有元素 相等 的 最少 总开销。
#
#
#
#  示例 1：
#
#  输入：nums = [1,3,5,2], cost = [2,3,1,14]
# 输出：8
# 解释：我们可以执行以下操作使所有元素变为 2 ：
# - 增加第 0 个元素 1 次，开销为 2 。
# - 减小第 1 个元素 1 次，开销为 3 。
# - 减小第 2 个元素 3 次，开销为 1 + 1 + 1 = 3 。
# 总开销为 2 + 3 + 3 = 8 。
# 这是最小开销。
#
#
#  示例 2：
#
#  输入：nums = [2,2,2,2,2], cost = [4,2,8,1,3]
# 输出：0
# 解释：数组中所有元素已经全部相等，不需要执行额外的操作。
#
#
#
#
#  提示：
#
#
#  n == nums.length == cost.length
#  1 <= n <= 10⁵
#  1 <= nums[i], cost[i] <= 10⁶
#
#
#  Related Topics 贪心 数组 二分查找 前缀和 排序
#  👍 28 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def minCost(self, nums: List[int], cost: List[int]) -> int:  # 枚举每个点
#         li = sorted(zip(nums, cost))
#         ans = total = sum((x - li[0][0]) * c for x, c in li)
#         sum_cost = sum(cost)
#         for (num1, c1), (num2, c2) in pairwise(li):
#             sum_cost -= c1 * 2
#             total -= sum_cost * (num2 - num1)
#             ans = min(ans, total)
#         return ans


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:  # 选择中位数
        li = sorted(zip(nums, cost))
        mid = (sum(cost) + 1) // 2
        s = 0
        for x, c in li:
            s += c
            if s >= mid:
                return sum(abs(y-x) * c for y, c in li)
# leetcode submit region end(Prohibit modification and deletion)
Solution().minCost(nums = [1,3,5,2], cost = [2,3,1,14])
