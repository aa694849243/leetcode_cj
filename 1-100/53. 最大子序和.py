'''
53. 最大子序和
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
进阶:

如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
'''

from typing import List


# 普通方法——caojie--74%------------
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        flag = 0
        maxsum = float('-inf')
        maxsum2 = float('-inf')
        if not nums:
            return
        for i in range(len(nums)):
            if nums[i] >= 0:
                flag = 1
                sum += nums[i]
            else:
                maxsum = max(maxsum, sum)
                sum += nums[i]
            if sum < 0:
                maxsum2 = max(maxsum2, sum)
                sum = 0

        return max(maxsum, sum) if flag else maxsum2


# 动态规划-----------------------------------------------------------------
# 链接：https://leetcode-cn.com/problems/maximum-subarray/solution/dong-tai-gui-hua-fen-zhi-fa-python-dai-ma-java-dai/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        # 起名叫 pre 表示的意思是“上一个状态”的值
        pre = nums[0]
        res = pre
        for i in range(1, size):
            pre = max(nums[i], pre + nums[i])
            res = max(res, pre)
        return res


# 参考链接同上
# 简单来说就是将数组分为三个部分，左半边，右半边，中心扩散（包含中间数的数组）
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size - 1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1  # 划分两部分
        return max(self.__max_sub_array(nums, left, mid),  # 左边
                   self.__max_sub_array(nums, mid + 1, right),  # 中间
                   self.__max_cross_array(nums, left, mid, right))  # 右边

    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含 nums[mid] 元素的最大连续子数组的和，
        # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:  # 一定包含中间-1数
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1

        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:  # 一定包含中间+1数
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max  # 最终中心扩散最大值


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Solution().maxSubArray(nums)
