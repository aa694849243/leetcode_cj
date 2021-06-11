# -*- coding: utf-8 -*-
import collections


# 如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。
#
#  给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。
#
#
#
#  示例 1：
#
#  输入：text = "ababa"
# 输出：3
#
#
#  示例 2：
#
#  输入：text = "aaabaaa"
# 输出：6
#
#
#  示例 3：
#
#  输入：text = "aaabbaaa"
# 输出：4
#
#
#  示例 4：
#
#  输入：text = "aaaaa"
# 输出：5
#
#
#  示例 5：
#
#  输入：text = "abcdef"
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= text.length <= 20000
#  text 仅由小写英文字母组成。
#
#  Related Topics 字符串
#  👍 63 👎 0


class Solution:
    def maxRepOpt1(self, text: str) -> int:
        m = collections.Counter(text)
        l, r = 0, 0
        ans = 1
        nxt = -1
        while l < len(text):
            cnt = 0
            flag = 0
            while r < len(text) and (text[r] == text[l] or flag < 2):
                if text[r] != text[l]:
                    if flag == 0:
                        nxt = r
                    flag += 1
                    cnt = 0
                    if flag == 2:
                        break
                else:
                    cnt += 1
                r += 1
            if cnt < m[text[l]]:
                cnt += 1
            ans = max(cnt, ans)
            if nxt > l:
                l, r = nxt, nxt
            else:
                break
        return ans


Solution().maxRepOpt1('abbaaaa')
