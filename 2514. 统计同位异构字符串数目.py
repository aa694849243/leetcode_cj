# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-01-30 21:21 
# ide： PyCharm
import collections
class Solution:
    def countAnagrams(self, s: str) -> int:
        mod = 10 ** 9 + 7
        lst = s.split()
        n = max(lst, key=len)
        facs = [1]
        for i in range(1, len(n) + 1):
            facs.append(facs[-1] * i % mod)
        facinv = [pow(fac,mod-2,mod) for fac in facs]
        ans = 1
        for word in lst:
            cnt = collections.Counter(word)
            x = facs[len(word)]
            for v in cnt.values():
                x = x * facinv[v] % mod
            ans = ans * x % mod
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().countAnagrams("too hot")
)
