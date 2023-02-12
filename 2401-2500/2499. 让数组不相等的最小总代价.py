# -*- coding: utf-8 -*-
# datetime： 2023-01-28 18:35
# ide： PyCharm
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans = mode = mx = swap_cnt = 0
        n = len(nums1)
        cnt = [0] * (n + 1)
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if a == b:
                ans += i
                cnt[a] += 1
                swap_cnt += 1
                if cnt[a] > mx:
                    mx = cnt[a]
                    mode = a
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            if 2 * cnt[mode] <= swap_cnt: break
            if a != b and a != mode and b != mode:
                swap_cnt += 1
                ans += i
        return ans if swap_cnt >= 2 * cnt[mode] else -1
    # leetcode submit region end(Prohibit modification and deletion)


print(Solution().minimumTotalCost(
    [2, 2, 2, 1, 3],
    [1, 2, 2, 3, 3]
))

