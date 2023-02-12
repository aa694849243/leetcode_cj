# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 23:15 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for mid in range(len(s)):
            ans += 1
            for l in range(1, mid + 1):
                if mid + l < len(s) and s[mid - l] == s[mid + l]:
                    ans += 1
                else:
                    break
        for mid in range(1, len(s)):
            if s[mid - 1] == s[mid]:
                ans += 1
                for l in range(1, mid):
                    if mid + l < len(s) and s[mid - l - 1] == s[mid + l]:
                        ans += 1
                    else:
                        break
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().countSubstrings(
        'aaa')
)

