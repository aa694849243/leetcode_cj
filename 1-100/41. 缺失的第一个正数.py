'''
给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。

 

示例 1:

输入: [1,2,0]
输出: 3
示例 2:

输入: [3,4,-1,1]
输出: 2
示例 3:

输入: [7,8,9,11,12]
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

#--------------caojie---28%-----------------------------------------------------------------------
#--参考--https://leetcode-cn.com/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:  # 单个元素情况
            return 1 if nums[0] != 1 else 2
        x = 0
        for i in range(n):  # 第一轮扫描，找1，小于1的换成1，没有1就直接返回1
            if nums[i] <= 1:
                if nums[i] < 1:
                    nums[i] = 1
                else:
                    x = 1
        if x != 1:
            return 1

        for i in range(n):  # 第二轮扫描，将存在的值对应位置上的数标为负数
            if abs(nums[i]) <= n - 1:
                nums[abs(nums[i])] = -abs(nums[abs(nums[i])])
            if abs(nums[i]) == n:  # 可以存放的最大值等于列表长度，用0位置代表这个值
                nums[0] = -abs(nums[0])

        for i in range(1, n):  # 第三轮扫描，找第一个大于0的数的下标
            if nums[i] > 0:
                return i
        if nums[0] < 0:
            return n + 1
        else:
            return n


nums = [2,1]
Solution().firstMissingPositive(nums)
