# -*- coding: utf-8 -*-
class Solution:
    def maxProduct(self, s: str) -> int:
        # s = '#' + '#'.join(list(s)) + '#'
        id = 0
        mx = 0
        p = [1] * len(s)
        f1 = [1] * len(s)
        for i in range(length := len(s)):
            if mx > id:
                p[i] = min(mx - i, p[2 * id - i])
            while p[i] + i < length and i - p[i] >= 0 and s[p[i] + i] == s[i - p[i]]:
                f1[p[i] + i] = max(f1[p[i] + i], 2 * p[i] + 1)
                p[i] += 1
            if i + p[i] > mx:
                id, mx = i, i + p[i]
        for i in range(1,len(f1)):
            f1[i]=max(f1[i],f1[i-1])
        p = [1] * len(s)
        f2 = [1] * len(s)
        mx=0
        id=0
        s = s[::-1]
        for i in range(len(s)):
            if mx > id:
                p[i] = min(mx - i, p[2 * id - i])
            while p[i] + i < length and i - p[i] >= 0 and s[p[i] + i] == s[i - p[i]]:
                f2[p[i] + i] = max(f2[p[i] + i], 2 * p[i] + 1)
                p[i] += 1
            if i + p[i] > mx:
                id, mx = i, i + p[i]
        for i in range(1,len(f2)):
            f2[i]=max(f2[i],f2[i-1])
        f2 = f2[::-1]
        res = 1
        for i in range(length - 1):
            res = max(res, f1[i] * f2[i + 1])
        return res
