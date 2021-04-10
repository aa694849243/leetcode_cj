'''给定字符串 S 和单词字典 words, 求 words[i] 中是 S 的子序列的单词个数。

示例:
输入:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
输出: 3
解释: 有三个是 S 的子序列的单词: "a", "acd", "ace"。
注意:

所有在words和 S 里的单词都只由小写字母组成。
S 的长度在 [1, 50000]。
words 的长度在 [1, 5000]。
words[i]的长度在[1, 50]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-matching-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections

import copy


# 做桶
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = [[] for _ in range(26)]
        for word in words:
            d[ord(word[0]) - ord('a')].append(word[1:])  # 首字母做桶
        cnt = 0
        for i, ch in enumerate(s):
            p = ord(ch) - ord('a')
            oldbucket = d[p]
            d[p] = []
            while oldbucket:  # 每匹配到一个首字母，则丢掉一个首字母，换桶
                nx = oldbucket.pop()
                if nx:
                    d[ord(nx[0]) - ord('a')].append(nx[1:])
                else:
                    cnt += 1
        return cnt


# 2查找下一个字母
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        n = len(s)
        d = [[n] * 26 for _ in range(n + 1)]
        for i in range(len(s) - 1, -1, -1):
            a = ord(s[i]) - ord('a')
            for j in range(26):
                if j == a:
                    d[i][a] = i
                else:
                    d[i][j] = d[i + 1][j]
        cnt = 0
        for word in words:
            pos = 0
            for ch in word:
                nxtpos = d[pos][ord(ch) - ord('a')]
                if nxtpos >= n:
                    break
                pos = nxtpos+1
            else:
                cnt += 1

        return cnt


Solution().numMatchingSubseq("dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"])
