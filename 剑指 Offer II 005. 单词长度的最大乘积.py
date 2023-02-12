# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-05 0:37 
# ide： PyCharm

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        lst = []
        for word in words:
            mask = 0
            for ch in word:
                mask |= (1 << (ord(ch) - 97))
            lst.append(mask)
        ans = 0
        for i, m1 in enumerate(lst):
            for j, m2 in enumerate(lst[i + 1:], i + 1):
                if m1 & m2 == 0:
                    ans = max(ans, len(words[i])*len(words[j]))
        return ans

# leetcode submit region end(Prohibit modification and deletion)

