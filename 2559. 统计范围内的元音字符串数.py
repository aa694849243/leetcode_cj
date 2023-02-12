# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-11 13:34 
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        nums = [0] * len(words)
        for i, word in enumerate(words):
            if word[0] in ['a', 'e', 'i', 'o', 'u'] and word[-1] in ['a', 'e', 'i', 'o', 'u']:
                nums[i] = 1
        pre_cum = [0] + list(itertools.accumulate(nums))
        ans = []
        for l, r in queries:
            ans.append(pre_cum[r + 1] - pre_cum[l])
        return ans
# leetcode submit region end(Prohibit modification and deletion)
# ide： PyCharm
