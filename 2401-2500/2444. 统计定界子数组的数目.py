# -*- coding: utf-8 -*-
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_i, max_i, p = -1, -1, -1
        ans = 0
        for i, num in enumerate(nums):  # 枚举右端点
            if num == minK:
                min_i = i
            if num == maxK:
                max_i = i
            if not minK <= num <= maxK:
                p = i
            ans += max(0, min(max_i, min_i) - p)  # 以右端点为结尾的定界可以延伸的最远端位置
        return ans
# leetcode submit region end(Prohibit modification and deletion)
