'''
还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:

输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。
示例 2:

输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。
注意:

给定的火柴长度和在 0 到 10^9之间。
火柴数组的长度不超过15。'''
from typing import List

# 深度优先搜索
import functools


# 深度优先搜索
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if sum(nums) % 4 != 0 or len(nums) < 4:
            return False
        nums.sort(reverse=True)  # 倒序的话可以剪枝，超过边长的会更早剪掉
        target = sum(nums) // 4
        n = len(nums)
        m = [0] * 4

        def dfs(index):
            if m[0] == m[1] == m[2] == target:
                return True
            if index >= n:
                return False
            for i in range(4):
                if m[i] + nums[index] <= target:
                    m[i] += nums[index]
                    if dfs(index + 1):
                        return True
                    m[i] -= nums[index]
            return False

        return dfs(0)


# 状态压缩+回溯
# 因为不需要特定火柴到特定的组，只需要相应长度的火柴混合在一组就行了，尝试jjclass Solution:
# 时间复杂度为O(N*2^N) 第一个循环(N)
class Solution:

    def makesquare(self, nums):
        if not nums or sum(nums) % 4 != 0 or len(nums)<4:
            return False
        nums.sort(reverse=True)
        L = len(nums)
        perimeter = sum(nums)
        possible_side = perimeter // 4
        memo = set() #每个mask视为一个状态，如果某个状态已经遍历过得不到解，那直接返回False,1表示还没用过，0表示已经用过了
        def recurse(mask):
            total = 0
            for i in range(L):
                if not (mask & (1 << i)):
                    total += nums[i]
            if total % possible_side == 0 and total // possible_side == 3: #已经填满了三条边，第四条边肯定符合答案
                return True
            if mask in memo:
                return False
            rem = possible_side * (total//possible_side + 1) - total
            for i in range(L):
                if nums[i] <= rem and mask & (1 << i):
                    if recurse(mask ^ (1 << i)):
                        return True
            memo.add(mask)
            return False
        return recurse((1 << L) - 1)




Solution().makesquare([5, 5, 5, 5, 8, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4])
