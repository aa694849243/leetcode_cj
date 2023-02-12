# -*- coding: utf-8 -*-
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        def odd_even_split(nums):
            for i in range(len(nums)):
                if nums[i] % 2 == 0:
                    nums[i] *= -1
            return sorted(nums)

        nums = odd_even_split(nums)
        target = odd_even_split(target)
        var = 0  # 变化量
        for a, b in zip(nums, target):
            var += abs(a - b)
        return var // 4
# leetcode submit region end(Prohibit modification and deletion)

