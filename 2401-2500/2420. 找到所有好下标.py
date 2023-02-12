# -*- coding: utf-8 -*-
# 给你一个大小为 n 下标从 0 开始的整数数组 nums 和一个正整数 k 。
#
#  对于 k <= i < n - k 之间的一个下标 i ，如果它满足以下条件，我们就称它为一个 好 下标：
#
#
#  下标 i 之前 的 k 个元素是 非递增的 。
#  下标 i 之后 的 k 个元素是 非递减的 。
#
#
#  按 升序 返回所有好下标。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,1,1,1,3,4,1], k = 2
# 输出：[2,3]
# 解释：数组中有两个好下标：
# - 下标 2 。子数组 [2,1] 是非递增的，子数组 [1,3] 是非递减的。
# - 下标 3 。子数组 [1,1] 是非递增的，子数组 [3,4] 是非递减的。
# 注意，下标 4 不是好下标，因为 [4,1] 不是非递减的。
#
#  示例 2：
#
#
# 输入：nums = [2,1,1,2], k = 2
# 输出：[]
# 解释：数组中没有好下标。
#
#
#
#
#  提示：
#
#
#  n == nums.length
#  3 <= n <= 10⁵
#  1 <= nums[i] <= 10⁶
#  1 <= k <= n / 2
#
#
#  Related Topics 数组 动态规划 前缀和
#  👍 26 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import collections
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        ans_left = [False] * len(nums)
        ans_right = [False] * len(nums)
        left = collections.deque()
        for i in range(k):
            if left and nums[left[-1]] < nums[i]:
                left = collections.deque()
            left.append(i)
        for i in range(k, len(nums)):
            if len(left) == k:
                ans_left[i] = True
            while left and left[0] <= i - k:
                left.popleft()
            if left and nums[left[-1]] < nums[i]:
                left = collections.deque()
            left.append(i)
        right = collections.deque()
        for i in range(len(nums) - 1, len(nums) - 1 - k, -1):
            if right and nums[right[-1]] < nums[i]:
                right = collections.deque()
            right.append(i)
        for i in range(len(nums) - 1 - k, -1, -1):
            if len(right) == k:
                ans_right[i] = True
            while right and right[0] >= i + k:
                right.popleft()
            if right and nums[right[-1]] < nums[i]:
                right = collections.deque()
            right.append(i)
        ans = []
        for i in range(len(nums)):
            if ans_left[i] and ans_right[i]:
                ans.append(i)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().goodIndices([2,1,1,1,3,4,1], 2))