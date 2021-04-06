'''给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/increasing-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 深度优先搜索 dfs
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        m = set()

        def dfs(nums, residue):
            for i in range(len(residue)):
                if residue[i] >= nums[-1]:
                    x = nums + [residue[i]]
                    if tuple(x) not in m:
                        m.add(tuple(x))
                        res.append(x)
                        dfs(x, residue[i + 1:])

        for i in range(len(nums)):
            dfs([nums[i]], nums[i + 1:])
        return res
