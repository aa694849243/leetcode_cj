# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 21:50 
# ide： PyCharm
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        ans = []
        for i in sorted(c,key=lambda x:c[x])[::-1]:
            ans.append(i)
            if len(ans) == k:
                break
        return ans

# leetcode submit region end(Prohibit modification and deletion)
