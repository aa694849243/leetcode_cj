import collections, heapq, itertools
from typing import List
# 给你一个整数数组 nums 和一个目标值 goal 。
#
#  你需要从 nums 中选出一个子序列，使子序列元素总和最接近 goal 。也就是说，如果子序列元素和为 sum ，你需要 最小化绝对差 abs(sum -
#  goal) 。
#
#  返回 abs(sum - goal) 可能的 最小值 。
#
#  注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。
#
#
#
#  示例 1：
#
#  输入：nums = [5,-7,3,5], goal = 6
# 输出：0
# 解释：选择整个数组作为选出的子序列，元素和为 6 。
# 子序列和与目标值相等，所以绝对差为 0 。
#
#
#  示例 2：
#
#  输入：nums = [7,-9,15,-2], goal = -5
# 输出：1
# 解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
# 绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。
#
#
#  示例 3：
#
#  输入：nums = [1,2,3], goal = -7
# 输出：7
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 40
#  -10⁷ <= nums[i] <= 10⁷
#  -10⁹ <= goal <= 10⁹
#
#
#  Related Topics 位运算 数组 双指针 动态规划 状态压缩 👍 77 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        if min(nums) > 0 and goal < 0:
            return abs(goal)
        elif max(nums) < 0 and goal > 0:
            return abs(goal)
        n = len(nums)
        ln, rn = n >> 1, n - (n >> 1)
        res = abs(goal)
        llst, rlst = nums[:ln], nums[ln:]
        # 状态压缩求和
        def state_compress(lst):
            n = len(lst)
            bit = {1 << i: lst[i] for i in range(n)}
            dp = [0] * (1 << n)
            for i in range(1, 1 << n):
                dp[i] = dp[i & (i - 1)] + bit[i & -i]
                # dp[i] = dp[i ^ i & -i] + bit[i & -i]
            return sorted(set(dp))

        lsum = state_compress(llst)
        rsum = state_compress(rlst)
        l, r = 0, len(rsum) - 1
        while l < len(lsum) and r >= 0:
            tmp = lsum[l] + rsum[r]
            res = min(res, abs(tmp - goal))
            if tmp < goal:
                l += 1
            else:
                r -= 1
        return res
