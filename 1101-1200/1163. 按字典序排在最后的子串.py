# -*- coding: utf-8 -*-
# 给你一个字符串 s，找出它的所有子串并按字典序排列，返回排在最后的那个子串。
#
#  
#
# 示例 1：
#
# 输入："abab"
# 输出："bab"
# 解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。
# 示例 2：
#
# 输入："leetcode"
# 输出："tcode"
#  
#
# 提示：
#
# 1 <= s.length <= 4 * 10^5
# s 仅含有小写英文字符。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/last-substring-in-lexicographical-order
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections


class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(s) == 1:
            return s
        flag = max(s)
        m = collections.defaultdict(lambda: -1)
        step = 0
        for i, val in enumerate(s):
            if val == flag:
                m[step] = i
                step += 1
        if len(m) == 1:
            return s[m[0]:]
        l, r = m[0], m[1]
        rank = 2
        while l < len(s) and r < len(s):
            nxt = m[rank]
            if s[l:r] >= s[r:2 * r - l]:
                if nxt == -1:
                    break
                r = nxt
            else:
                step = r - l + 1
                while s[l:l + step] == s[r:2 * r - l]:
                    step += 1
                if s[l:l + step] >= s[r:r + step]:
                    if nxt == -1:
                        break
                    r = nxt
                else:
                    l = r
                    if nxt == -1:
                        break
                    r = nxt
            rank += 1

        return s[l:]


Solution().lastSubstring("zvfzmezzw")
