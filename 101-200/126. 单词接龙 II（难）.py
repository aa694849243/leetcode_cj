'''
给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：

每次转换只能改变一个字母。
转换后得到的单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回一个空列表。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: []

解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from collections import defaultdict
from collections import deque
from typing import List


# 图 邻接表法
from collections import defaultdict
from collections import deque
from typing import List

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        g = collections.defaultdict(set)
        wordList.append(beginWord)
        s = set(wordList)
        cost = collections.defaultdict(lambda: math.inf)
        for word in wordList:
            for i, ch in enumerate(word):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    if letter != ch:
                        tmp = word[:i] + letter + word[i + 1:]
                        if tmp in s:
                            g[word].add(tmp)
        q = collections.deque([beginWord])
        cost[beginWord] = 0
        res = []
        while q:
            cur_word = q.popleft()
            for nxt in g[cur_word]:
                if cost[nxt] == math.inf:
                    cost[nxt] = cost[cur_word] + 1
                    q.append(nxt)
            if cost[endWord] != math.inf:
                break
        if cost[endWord] == math.inf:
            return []
        m = collections.defaultdict(set)
        for word in wordList:
            m[cost[word]].add(word)
        g2 = collections.defaultdict(set)
        for word in wordList:
            g2[word] = g[word] & m[cost[word] - 1]
        path = [endWord]

        def dfs(word):
            if word == beginWord:
                res.append(path[:][::-1])
                return
            for nxt in g2[word]:
                path.append(nxt)
                dfs(nxt)
                path.pop()

        dfs(endWord)
        return res

Solution().findLadders(beginWord, endWord, wordList)
