# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-01 23:16 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k==0:
            return 0 if nums1==nums2 else -1
        bal = 0
        cnt = 0
        for a, b in zip(nums1, nums2):
            if abs(a - b) % k:
                return -1
            bal += (a - b) // k
            cnt += abs(a - b) // k
        return cnt // 2 if bal == 0 else -1


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().minOperations(
        [10, 5, 15, 20],
        [20, 10, 15, 5],
        0
    )
)
