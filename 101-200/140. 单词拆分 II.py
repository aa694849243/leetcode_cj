'''
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。

说明：

分隔时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
输出:
[
  "cats and dog",
  "cat sand dog"
]
示例 2：

输入:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
输出:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
解释: 注意你可以重复使用字典中的单词。
示例 3：

输入:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
输出:
[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# dfs超时
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def dfs(s, worddict, ans):
            if not s:
                res.append(ans)
                return
            for i in range(len(s)):
                if s[:i + 1] in worddict:
                    dfs(s[i + 1:], worddict, ans + s[:i + 1] + ' ')

        dfs(s, wordDict, '')
        res2 = []
        for i in range(len(res)):
            res2.append(i.rstrip())
        return res2


# 动态规划

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = ['']
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j:i + 1] in wordDict:
                    for x in dp[j]:
                        dp[i + 1].append(x + s[j:i + 1] + ' ')
        res = []
        for i in dp[-1]:
            res.append(i.rstrip())

        return res


from collections import defaultdict

#回溯法 特殊回溯 精妙回溯 dfs 特殊dfs 精妙dfs
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        mem = {}

        def dfs(s):
            if s in mem:
                return mem[s]
            if not s:
                return []
            res = []
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict:
                    if i == len(s):
                        res.append(s[:i])
                    else:
                        rest=dfs(s[i:])
                        for j in rest:
                            res.append(s[:i] + ' ' + j)
            mem[s] = res
            return res
        return dfs(s)


# s="catsanddog"
# a=["cat","cats","and","sand","dog"]
# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
s= 'aaaaa'
a = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
Solution().wordBreak(s, a)
