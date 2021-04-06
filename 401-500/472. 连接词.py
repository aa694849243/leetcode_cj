'''给定一个不含重复单词的列表，编写一个程序，返回给定单词列表中所有的连接词。

连接词的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。

示例:

输入: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

输出: ["catsdogcats","dogcatsdog","ratcatdogcat"]

解释: "catsdogcats"由"cats", "dog" 和 "cats"组成;
     "dogcatsdog"由"dog", "cats"和"dog"组成;
     "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
说明:

给定数组的元素总数不超过 10000。
给定数组中元素的长度总和不超过 600000。
所有输入字符串只包含小写字母。
不需要考虑答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/concatenated-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 字典树 不含重复字符串说明空字符串‘’没有用处
class trie:
    def __init__(self):
        self.look = {}

    def insert(self, s):
        tree = self.look
        if not s:
            tree[''] = '$'
        for ch in s:
            if ch not in tree:
                tree[ch] = {}
            tree = tree[ch]
        tree['$'] = '$'

    def search(self, s):
        if not s:
            return '' in self.look
        tree = self.look
        for ch in s:
            if ch not in tree:
                return False
            tree = tree[ch]
        return '$' in tree


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        m = trie()

        def check(word):
            if not word:
                return True
            for i in range(len(word)):
                if m.search(word[:i + 1]) and check(word[i + 1:]):
                    return True
            return False

        res = []
        for word in words:
            if not word:
                continue
            if check(word):
                res.append(word)
            m.insert(word)
        return res


# 改合体的方法
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        look = {}

        def treeinsert(s):
            tree = look
            if not s:
                tree[''] = '$'
            for ch in s:
                if ch not in tree:
                    tree[ch] = {}
                tree = tree[ch]
            tree['$'] = '$'

        def check(word):
            if not word:
                return True
            for i in range(len(word)):
                if search(word[:i + 1]) and check(word[i + 1:]):
                    return True
            return False

        def search(s):
            tree = look
            for ch in s:
                if ch not in tree:
                    return False
                tree = tree[ch]
            return '$' in tree

        res = []
        for word in words:
            if not word:
                continue
            if check(word):
                res.append(word)
            treeinsert(word)
        return res


# 动态规划
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        m = set()

        def check(s):
            if not s:
                return False
            dp = [True] + [False] * len(s)
            for i in range(1, len(s) + 1):
                for j in range(i):
                    if dp[j]==True and s[j:i] in m:
                        dp[i] = True
                        break
            return dp[-1]

        res = []
        for word in words:
            if check(word):
                res.append(word)
            m.add(word)
        return res

class Solution:

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        minl = max(1,len(words[0]))
        m = set()

        def dfs(word):
            if not word:
                return True
            for i in range(minl, len(word) + 1):
                if word[:i] in m and dfs(word[i:]):
                    return True
            return False

        res = []
        for word in words:
            if word and dfs(word):
                res.append(word)
            m.add(word)
        return res
b=["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

c=Solution().findAllConcatenatedWordsInADict(b)
