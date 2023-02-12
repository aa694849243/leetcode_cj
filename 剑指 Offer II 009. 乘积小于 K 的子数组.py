# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-05 23:29 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        product = nums[0]
        if product < k:
            ans += 1
        for r in range(1, len(nums)):
            product *= nums[r]
            while product >= k and l < r:
                product /= nums[l]
                l += 1
            if product < k:
                ans += r - l + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().numSubarrayProductLessThanK(
        [10, 5, 2, 6], 100
    )
)

