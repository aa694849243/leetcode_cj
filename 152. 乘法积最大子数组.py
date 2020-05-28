"""给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积
示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。"""


class Solution:
    def maxProduct(self, nums: list) -> int:
        """动态规划求解,序列最后一个数选择乘或不乘得到当前最大值，因为负数存在，一个最小值的数乘最小值和最大值都有可能得到最大值，所以需要维护前一步的最小值和最大值，时间复杂度为O(n)"""
        a = b = nums[0]
        max_ = float('-inf')
        for i in range(1, len(nums)):
            temp = a
            a = max(nums[i], nums[i] * a, nums[i] * b)  # a维护前一步最大值
            b = min(nums[i], nums[i] * temp, nums[i] * b)  # b维护前一步最小值
            max_ = max(a, b, max_)  # max_维护最大值
        return max_
A=Solution().maxProduct()


