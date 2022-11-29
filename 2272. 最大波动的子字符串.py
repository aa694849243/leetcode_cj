# -*- coding: utf-8 -*-
# 字符串的 波动 定义为子字符串中出现次数 最多 的字符次数与出现次数 最少 的字符次数之差。
#
#  给你一个字符串 s ，它只包含小写英文字母。请你返回 s 里所有 子字符串的 最大波动 值。
#
#  子字符串 是一个字符串的一段连续字符序列。
#
#
#
#  示例 1：
#
#
# 输入：s = "aababbb"
# 输出：3
# 解释：
# 所有可能的波动值和它们对应的子字符串如以下所示：
# - 波动值为 0 的子字符串："a" ，"aa" ，"ab" ，"abab" ，"aababb" ，"ba" ，"b" ，"bb" 和 "bbb" 。
# - 波动值为 1 的子字符串："aab" ，"aba" ，"abb" ，"aabab" ，"ababb" ，"aababbb" 和 "bab" 。
# - 波动值为 2 的子字符串："aaba" ，"ababbb" ，"abbb" 和 "babb" 。
# - 波动值为 3 的子字符串 "babbb" 。
# 所以，最大可能波动值为 3 。
#
#
#  示例 2：
#
#
# 输入：s = "abcde"
# 输出：0
# 解释：
# s 中没有字母出现超过 1 次，所以 s 中每个子字符串的波动值都是 0 。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁴
#  s 只包含小写英文字母。
#
#
#  Related Topics 数组 动态规划
#  👍 48 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestVariance(self, s: str) -> int:
        m = collections.defaultdict(list)
        for i in range(len(s)):
            m[s[i]].append(i)
        ans = 0
        for c0, ma_lst in m.items():
            for c1, mi_lst in m.items():
                if c0 != c1:
                    i, j = 0, 0
                    f, g = 0, float('-inf')  # f:可不包含c1的最大值，g:至少包含1个c1的最大值
                    while i < len(ma_lst) or j < len(mi_lst):
                        if j == len(mi_lst) or (i < len(ma_lst) and ma_lst[i] < mi_lst[j]):
                            f = max(f, 0) + 1
                            g += 1
                            i += 1
                        else:
                            g, f = max(g, f, 0) - 1, max(f, 0) - 1
                            j += 1
                        ans = max(ans, g)
        return ans

# leetcode submit region end(Prohibit modification and deletion)
