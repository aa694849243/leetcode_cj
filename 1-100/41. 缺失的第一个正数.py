class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while nums[i] < len(nums) and nums[i] > 0 and nums[i] != i + 1 and nums[nums[i]-1] != nums[i]:
                p = nums[i] - 1
                nums[i], nums[p] = nums[p], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        else:
            return len(nums) + 1


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().firstMissingPositive(
        [3, 4, -1, 1]
    )
)
