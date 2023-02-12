# -*- coding: utf-8 -*-
# datetime： 2023-01-28 0:38
# ide： PyCharm
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        p = nums.index(k)
        cnt = collections.defaultdict(int)
        c = 0
        cnt[0] = 1
        for i in range(p + 1, len(nums)):
            c += 1 if nums[i] > k else -1
            cnt[c] += 1
        ans = cnt[0] + cnt[1]
        c = 0
        for i in range(p - 1, -1, -1):
            c += 1 if nums[i] < k else -1
            ans += cnt[c] + cnt[c + 1]
        return ans
# leetcode submit region end(Prohibit modification and deletion)

