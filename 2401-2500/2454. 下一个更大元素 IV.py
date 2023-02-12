# -*- coding: utf-8 -*-
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:  # 双递减栈
        res, dec_stk, stk = [-1] * len(nums), [], []
        for i, num in enumerate(nums):
            while stk and nums[stk[-1]] < num:
                res[stk.pop()] = num
            tmp_stk = []
            while dec_stk and nums[dec_stk[-1]] <num:
                tmp_stk.append(dec_stk.pop())
            dec_stk.append(i)
            stk += tmp_stk[::-1]
        return res

# leetcode submit region end(Prohibit modification and deletion)
