# -*- coding: utf-8 -*-
# datetime： 2023-02-01 23:04
# ide： PyCharm
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        mp = collections.defaultdict(collections.deque)
        tmp = 0
        ans = 0
        l = 0
        for i, num in enumerate(nums):
            mp[num].append(i)
            n = len(mp[num])
            tmp += n - 1
            while tmp >= k and l < i:
                tmp -= len(mp[nums[l]]) - 1
                mp[nums[l]].popleft()
                l += 1
            ans += l
        return ans

# leetcode submit region end(Prohibit modification and deletion)

