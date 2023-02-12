# -*- coding: utf-8 -*-
# datetime： 2023-02-05 0:26
# ide： PyCharm
# 负数二进制
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            tot = sum((num >> i) & 1 for num in nums)
            if tot % 3:
                if i == 31:
                    ans -= (1 << i)
                else:
                    ans |= (1 << i)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().singleNumber(
        [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2]
    )
)

