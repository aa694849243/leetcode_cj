# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-01 23:38 
# ide： PyCharm
from typing import List
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        q = sorted(zip(nums2, nums1, range(len(nums1))))[::-1]
        tmp = []
        cum = 0
        for num2, num1, i in q:
            if len(tmp) >= k:
                cum -= heapq.heappop(tmp)
            heapq.heappush(tmp, num1)
            cum += num1
            if len(tmp) == k:
                ans = max(ans, cum * num2)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().maxScore(nums1=[1, 3, 3, 2], nums2=[2, 1, 3, 4], k=3),
)
