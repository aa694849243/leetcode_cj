# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-05 23:40 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
import sortedcontainers
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        pre_cum = [0] + list(accumulate(nums))
        ans = 0
        lst = sortedcontainers.SortedList([0])
        for i in range(1, len(pre_cum)):
            ans += bisect.bisect_right(lst, pre_cum[i] - k) - bisect.bisect_left(lst, pre_cum[i] - k)
            lst.add(pre_cum[i])
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().subarraySum(
        [1, 1, 1], 2
    )
)

