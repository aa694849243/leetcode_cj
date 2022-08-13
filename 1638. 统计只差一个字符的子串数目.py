# https://leetcode.cn/problems/count-substrings-that-differ-by-one-character/solution/tong-ji-zhi-chai-yi-ge-zi-fu-de-zi-chuan-shu-mu-by/
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        ans = 0
        for delta in range(-m + 1, n):  # 如果m==n，0点对齐只出现一次
            i, j = 0, 0
            if delta < 0:
                i = -delta
            else:
                j = delta
            fij = gij = 0
            while i < m and j < n:
                if s[i] == t[j]:
                    gij += 1
                else:
                    fij = gij + 1
                    gij = 0
                ans += fij
                i += 1
                j += 1
        return ans
        