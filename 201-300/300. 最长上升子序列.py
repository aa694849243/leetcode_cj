'''
给定一个无序的整数数组，找到其中最长上升子序列的长度。

示例:

输入: [10,9,2,5,3,7,101,18]
输出: 4
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
说明:

可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
你算法的时间复杂度应该为 O(n2) 。
进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?'''
from typing import List


# 动态规划
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        m = 0
        for i in range(len(nums)):
            a = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    a = max(a, dp[j])
            dp.append(a + 1)
            m = max(m, a + 1)
        return m


# 贪心 二分法 LIS算法
# 尽可能缓慢的增长序列
import bisect


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        a = []
        for i in range(len(nums)):
            if not a or nums[i]>a[-1]:
                a.append(nums[i])
            else:
                j=bisect.bisect_left(a,nums[i])
                a[j]=nums[i]
        return len(a)



Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])
