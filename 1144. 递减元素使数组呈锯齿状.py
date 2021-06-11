# -*- coding: utf-8 -*-
from typing import List


# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
#
#  如果符合下列情况之一，则数组 A 就是 锯齿数组：
#
#
#  每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
#  或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
#
#
#  返回将数组 nums 转换为锯齿数组所需的最小操作次数。
#
#
#
#  示例 1：
#
#  输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
#
#
#  示例 2：
#
#  输入：nums = [9,6,1,6,2]
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 1000
#  1 <= nums[i] <= 1000
#
#  Related Topics 数组
#  👍 31 👎 0

# 要么只改变奇数位置，要么只改变偶数位置的操作数是最小的，因为只能向下改变，比如0位置下降了，则1位置一定处于波峰处，波峰处如果下降，那2位置可能还要下降，那就增加操作数了，所以全部波峰处的位置都是不变的
# https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag/solution/fen-qing-kuang-tao-lun-python3-by-smoon1989/
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        n = len(nums)
        ans1 = ans2 = 0
        for i, num in enumerate(nums):
            if i % 2:  # 只改变奇数位置,偶数位置处于波峰
                d1 = num - nums[i - 1] + 1 if i > 0 and num - nums[i - 1] >= 0 else 0
                d2 = num - nums[i + 1] + 1 if i < n and num - nums[i + 1] >= 0 else 0
                ans1 += max(d1, d2)
            else:  # 只改变偶数位置
                d1 = num - nums[i - 1] + 1 if i > 0 and num - nums[i - 1] >= 0 else 0
                d2 = num - nums[i + 1] + 1 if i < n and num - nums[i + 1] >= 0 else 0
                ans2 += max(d1, d2)
        return max(ans1,ans2)

