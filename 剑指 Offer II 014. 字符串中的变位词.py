# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 21:37 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = -1
        c = collections.Counter(s1)
        tmp = collections.Counter()
        for r, ch in enumerate(s2):
            tmp[ch] += 1
            if r >= len(s1):
                tmp[s2[r - len(s1)]] -= 1
            for k in c:
                if c[k] != tmp[k]:
                    break
            else:
                return True

        return False

