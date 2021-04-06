'''
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# ------失败-caojie——使用递归时间过长-----------------------------------------------------------------------------------------
class Solution:

    def gen_pnext_c(self, p):
        k = -1
        m = len(p)
        pnext = [-1] * m
        j = 0
        while j < m - 1:
            if p[j] == p[k] or k == -1:
                k += 1
                j += 1
                if p[j] == p[k]:
                    pnext[j] = pnext[k]
                else:
                    pnext[j] = k
            else:
                k = pnext[k]
        return pnext

    def matching_KMP(self, t, p, pnext):
        n = len(t)
        m = len(p)
        i = 0
        j = 0
        ans = []
        while i < n:
            if t[i] == p[j] or j == -1:
                i += 1
                j += 1
            else:
                j = pnext[j]
            if j == m:
                ans.append(i - m)
                j = 0
                i = i - m + 1
        return ans

    def rec(self, start, end, s, lenth, words, res):
        if not words:
            res.append(start)
        if s[end:end + lenth] in words and s[start - lenth:start] in words:
            wrd = s[end:end + lenth]
            self.rec(start, end + lenth, s, lenth, words[:words.index(wrd)] + words[words.index(wrd) + 1:], res)
            wrd = s[start - lenth:start]
            self.rec(start - lenth, end, s, lenth, words[:words.index(wrd)] + words[words.index(wrd) + 1:], res)
        elif s[start - lenth:start] in words:
            wrd = s[start - lenth:start]
            start = start - lenth
            self.rec(start, end, s, lenth, words[:words.index(wrd)] + words[words.index(wrd) + 1:], res)
        elif s[end:end + lenth] in words:
            wrd = s[end:end + lenth]
            end = end + lenth
            self.rec(start, end, s, lenth, words[:words.index(wrd)] + words[words.index(wrd) + 1:], res)

    # self.rec(start, end, s, lenth, words, wrd, res)

    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return 0
        p = words.pop()
        pnext = self.gen_pnext_c(p)
        lenth = len(p)
        ans = self.matching_KMP(s, p, pnext)
        res = []
        for i in ans:
            self.rec(i, i + lenth, s, lenth, words, res)
        return list(set(res))


# -----------------------
class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not words:
            return []
        lenth = len(words[0])
        words_copy = words.copy()
        res = []
        right = 0
        left = 0
        l=lenth*len(words)
        i = 0
        while left <= len(s) - l:
            if s[i:i + lenth] in words_copy:
                words_copy.remove(s[i:i + lenth])
                i += lenth
                if not words_copy:
                    res.append(left)
                    words_copy = words.copy()
                    left += 1
                    i = left
            # elif s[i:i + lenth] in words:
            #     words_copy = words.copy()
            #     left = i
            else:
                left += 1
                i = left
                words_copy = words.copy()
        return res


s="wordgoodgoodgoodbestword"
words=["word","good","best","good"]
Solution().findSubstring(s, words)
from collections import Counter
words=Counter(words)
words