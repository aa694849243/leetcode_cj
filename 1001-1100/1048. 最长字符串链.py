# -*- coding: utf-8 -*-
import collections
from typing import List


# 给出一个单词列表，其中每个单词都由小写英文字母组成。
#
#  如果我们可以在 word1 的任何地方添加一个字母使其变成 word2，那么我们认为 word1 是 word2 的前身。例如，"abc" 是 "abac
# " 的前身。
#
#  词链是单词 [word_1, word_2, ..., word_k] 组成的序列，k >= 1，其中 word_1 是 word_2 的前身，word_
# 2 是 word_3 的前身，依此类推。
#
#  从给定单词列表 words 中选择单词组成词链，返回词链的最长可能长度。
#
#
#  示例：
#
#  输入：["a","b","ba","bca","bda","bdca"]
# 输出：4
# 解释：最长单词链之一为 "a","ba","bda","bdca"。
#
#
#
#
#  提示：
#
#
#  1 <= words.length <= 1000
#  1 <= words[i].length <= 16
#  words[i] 仅由小写英文字母组成。
#
#
#
#  Related Topics 哈希表 动态规划
#  👍 111 👎 0


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))
        dp = [1] * len(words)
        m = collections.defaultdict(list)

        def check(word1, word2):
            if len(word2) - len(word1) != 1:
                return False
            p = 0
            flag = 0
            for i in range(len(word1)):
                if word1[i] != word2[p]:
                    if flag:
                        return False
                    flag += 1
                    p += 1
                    if word1[i] != word2[p]:
                        return False
                p += 1
            return True

        for i, word in enumerate(words[1:], 1):
            for j in range(i):
                if check(words[j], words[i]):
                    m[i].append(j)

        for i, word in enumerate(words[1:], 1):
            for j in m[i]:
                dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)


Solution().longestStrChain(["a","b","ab","bac"])
