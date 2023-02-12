# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 21:40 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        c = collections.Counter(p)
        tmp = collections.Counter()
        res = []
        for r, ch in enumerate(s):
            tmp[ch] += 1
            if r >= len(p):
                tmp[s[r - len(p)]] -= 1
            for k in c:
                if c[k] != tmp[k]:
                    break
            else:
                res.append(r-len(p)+1)
        return  res
# leetcode submit region end(Prohibit modification and deletion)

