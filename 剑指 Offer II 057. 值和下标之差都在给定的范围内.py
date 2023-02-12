# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 21:37 
# ide： PyCharm
from sortedcontainers import SortedList

from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if not nums or len(nums)<2 or k<1 or t<0:
            return False
        lst = SortedList(nums[:k + 1])
        for i in range(1, len(lst)):
            if lst[i] - lst[i - 1]<= t:
                return True
        for j in range(k + 1, len(nums)):
            lst.remove(nums[j - k - 1])
            p = lst.bisect_left(nums[j])
            if p < len(lst) and lst[p] - nums[j] <= t or p > 0 and nums[j] - lst[p - 1] <= t:
                return True
            lst.add(nums[j])
        return False


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().containsNearbyAlmostDuplicate(
        [1, 5, 9, 1, 5, 9],
        2,
        3
    )
)

