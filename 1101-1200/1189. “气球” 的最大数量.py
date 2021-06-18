# -*- coding: utf-8 -*-
import collections


# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
#
#  字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
#
#
#
#  示例 1：
#
#
#
#  输入：text = "nlaebolko"
# 输出：1
#
#
#  示例 2：
#
#
#
#  输入：text = "loonbalxballpoon"
# 输出：2
#
#
#  示例 3：
#
#  输入：text = "leetcode"
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= text.length <= 10^4
#  text 全部由小写英文字母组成
#
#  Related Topics 哈希表 字符串
#  👍 51 👎 0


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        m = collections.Counter(text)
        ans = float('inf')
        for ch in ['b', 'a', 'l', 'o', 'n']:
            if ch in 'ban':
                ans = min(ans, m[ch])
            else:
                ans=min(ans,m[ch]//2)
        return ans