# -*- coding: utf-8 -*-
# 对于字符串 S 和 T，只有在 S = T + ... + T（T 自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。
#
#  返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。
#
#
#
#  示例 1：
#
#
# 输入：str1 = "ABCABC", str2 = "ABC"
# 输出："ABC"
#
#
#  示例 2：
#
#
# 输入：str1 = "ABABAB", str2 = "ABAB"
# 输出："AB"
#
#
#  示例 3：
#
#
# 输入：str1 = "LEET", str2 = "CODE"
# 输出：""
#
#
#
#
#  提示：
#
#
#  1 <= str1.length <= 1000
#  1 <= str2.length <= 1000
#  str1[i] 和 str2[i] 为大写英文字母
#
#  Related Topics 字符串
#  👍 197 👎 0


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        if str2 not in str1:
            return ''
        len1, len2 = len(str1), len(str2)
        for l in range(len(str2), 0, -1):
            if len1 // l == len1 / l and len2 // l == len2 / l:
                if str2[:l] * (len1 // l) == str1 and str2[:l] * (len2 // l) == str2:
                    return str2[:l]
        return ''
