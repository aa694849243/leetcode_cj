# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 22:38 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
# 不重不漏的增加数对
from typing import List
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        lst = [[nums1[i] + nums2[0], i, 0] for i in range(min(n, k))]
        ans = []
        while lst and len(ans) < k:
            _, i, j = heapq.heappop(lst)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < m:
                heapq.heappush(lst, [nums1[i] + nums2[j + 1], i, j + 1])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().kSmallestPairs(
        [1, 2],
        [3],
        3
    ),
)

