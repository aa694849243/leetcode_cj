# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 21:48 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        l = 0
        ans = 0
        for r, ch in enumerate(s):
            if ch in c:
                while s[l] != ch and l < r:
                    c.discard(s[l])
                    l += 1
                l += 1
            c.add(ch)
            ans = max(ans, r - l + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().lengthOfLongestSubstring(
        "abcabcbb"
    )
)

