'''给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。

如果有多个目标子集，返回其中任何一个均可。

 

示例 1:

输入: [1,2,3]
输出: [1,2] (当然, [1,3] 也正确)
示例 2:

输入: [1,2,4,8]
输出: [1,2,4,8]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-divisible-subset
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            maxsize = 1
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    maxsize = max(dp[j] + 1, maxsize)
            dp[i] = maxsize
        m = max(dp)
        max_index = dp.index(m)
        x = nums[max_index]
        ans = []
        for i in range(max_index, -1, -1):
            if x % nums[i] == 0 and dp[i] == m:
                m -= 1
                ans.append(nums[i])
                x = nums[i]
        return ans


a = [4]
Solution().largestDivisibleSubset(a)
