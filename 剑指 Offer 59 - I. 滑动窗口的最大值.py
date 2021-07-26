#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
#
#  示例:
#
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#
#
#
#  提示：
#
#  你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
#  注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/
#  Related Topics 队列 滑动窗口 单调队列 堆（优先队列）
#  👍 292 👎 0


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from sortedcontainers import SortedList
        if not nums:
            return []
        li = SortedList(nums[:k])
        ans = []
        ans.append(li[-1])
        for i in range(k, len(nums)):
            li.add(nums[i])
            li.remove(nums[i - k])
            ans.append(li[-1])
        return ans


# 单调队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        q = collections.deque([0])
        ans = []
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ans.append(nums[q[0]])
        for i in range(k, len(nums)):
            while q and i - q[0] >= k:
                q.popleft()
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans
Solution().maxSlidingWindow([1,-1], 1)