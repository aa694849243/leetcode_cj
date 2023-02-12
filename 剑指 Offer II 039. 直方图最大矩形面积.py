# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 20:14 
# ide： PyCharm
from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        n = len(heights)
        right = [n] * n
        for i in range(len(heights)):
            while stk and heights[stk[-1]] > heights[i]:
                p = stk.pop()
                right[p] = i
            stk.append(i)
        stk=[]
        left = [-1] * n
        for i in range(n - 1, -1, -1):
            while stk and heights[stk[-1]] > heights[i]:
                p = stk.pop()
                left[p] = i
            stk.append(i)
        ans = 0
        for i in range(n):
            ans = max(ans, (right[i] - left[i] - 1) * heights[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().largestRectangleArea(
    [2, 1, 5, 6, 2, 3]
))

