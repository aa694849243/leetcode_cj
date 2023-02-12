# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 23:01 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ''
        ma = math.inf
        m = collections.Counter(t)
        l = 0
        tmp = collections.Counter()
        for r, ch in enumerate(s):
            tmp[ch] += 1
            for x in m:
                if tmp[x] < m[x]:
                    break
            else:
                if r - l + 1 < ma:
                    ans = s[l:r + 1]
                    ma = r - l + 1
                while l < r:
                    tmp[s[l]] -= 1
                    if tmp[s[l]] < m[s[l]]:
                        l += 1
                        break
                    l += 1
                    if r - l + 1 < ma:
                        ans = s[l:r + 1]
                        ma = r - l + 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().minWindow(
        "ADOBECODEBANC", "ABC")
)

