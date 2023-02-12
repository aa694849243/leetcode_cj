# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-02 21:37 
# ide： PyCharm
class Solution:
    def minCost(self, nums: List[int], k: int) -> int:
        dp = [math.inf] * (len(nums) + 1)
        dp[0] = 0
        for i in range(len(nums)):
            tmp = collections.Counter()
            length = 0
            for j in range(i, -1, -1):
                tmp[nums[j]] += 1
                if tmp[nums[j]] == 2:
                    length += 2
                elif tmp[nums[j]] > 2:
                    length += 1
                dp[i + 1] = min(dp[i + 1], dp[j] + length + k)
        return dp[-1]
# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().minCost(
        [1, 2, 1, 2, 1, 3, 3], 2
    )
)

