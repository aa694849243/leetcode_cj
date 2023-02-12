# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-05 23:44 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        bal = 0
        m = collections.defaultdict(int)
        m[0] = -1
        ans = 0
        for i, num in enumerate(nums):
            bal += 1 if num == 1 else -1
            if bal not in m:
                m[bal] = i
            ans = max(ans, i - m[bal])
        return ans

# leetcode submit region end(Prohibit modification and deletion)

