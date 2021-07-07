# -*- coding: utf-8 -*-
# 给你两个长度为 n 的字符串 s1 和 s2 ，以及一个字符串 evil 。请你返回 好字符串 的数目。
#
#  好字符串 的定义为：它的长度为 n ，字典序大于等于 s1 ，字典序小于等于 s2 ，且不包含 evil 为子字符串。
#
#  由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。
#
#
#
#  示例 1：
#
#  输入：n = 2, s1 = "aa", s2 = "da", evil = "b"
# 输出：51
# 解释：总共有 25 个以 'a' 开头的好字符串："aa"，"ac"，"ad"，...，"az"。还有 25 个以 'c' 开头的好字符串："ca"，"cc
# "，"cd"，...，"cz"。最后，还有一个以 'd' 开头的好字符串："da"。
#
#
#  示例 2：
#
#  输入：n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
# 输出：0
# 解释：所有字典序大于等于 s1 且小于等于 s2 的字符串都以 evil 字符串 "leet" 开头。所以没有好字符串。
#
#
#  示例 3：
#
#  输入：n = 2, s1 = "gx", s2 = "gz", evil = "x"
# 输出：2
#
#
#
#
#  提示：
#
#
#  s1.length == n
#  s2.length == n
#  s1 <= s2
#  1 <= n <= 500
#  1 <= evil.length <= 50
#  所有字符串都只包含小写英文字母。
#
#  Related Topics 字符串 动态规划 字符串匹配
#  👍 54 👎 0
import functools


class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        mod = 10 ** 9 + 7

        def gen_pnext(p):
            k = -1
            j = 0
            m = len(p)
            pnext = [-1] * m
            while j < m - 1:
                if k == -1 or p[j] == p[k]:
                    k += 1
                    j += 1
                    if p[j] == p[k]:
                        pnext[j] = pnext[k]
                    else:
                        pnext[j] = k
                else:
                    k = pnext[k]
            return pnext

        pnext = gen_pnext(evil)
        np=len(evil)
        def nextstatus(status, ch):  # status代表有几个匹配的
            while status >= 0 and evil[status] != ch:
                status = pnext[status]
            return status + 1  # 下一个开始比较的位置

        @functools.lru_cache(None)
        def dp(pos, status, bound):
            if status == np:  # evil匹配完成
                return 0
            if pos == n:  # 最后一个匹配完成
                return 1
            ans = 0
            l = ord(s1[pos]) if bound & 1 else 97
            r = ord(s2[pos]) if bound & 2 else 122
            for p in range(l, r + 1):
                ch = chr(p)
                n_status = nextstatus(status, ch)  # evil下一个匹配的位置
                if bound==1:
                    n_bound=1 if p==l else 0
                elif bound==2:
                    n_bound=2 if p==r else 0
                elif bound==3:
                    if l==r==p:
                        n_bound=3
                    elif p==l:
                        n_bound=1
                    elif p==r:
                        n_bound=2
                    else:
                        n_bound=0
                else:
                    n_bound=0
                # nxt_bound = (ch == s1[pos] if bound & 1 else 0) ^ ((ch == s2[pos]) << 1 if bound & 2 else 0) 复杂写法
                ans+=dp(pos+1,n_status,n_bound)
            return ans%mod
        return dp(0,0,3)
Solution().findGoodStrings(n = 2, s1 = "gx", s2 = "gz", evil = "x")