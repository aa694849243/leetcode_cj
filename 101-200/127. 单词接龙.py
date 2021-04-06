'''
给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
示例 1:

输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
示例 2:

输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import deque
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        map1, map2 = {}, {}
        if (endWord not in wordList) or not beginWord or not wordList:
            return 0
        if beginWord not in wordList:
            wordList = [beginWord] + wordList
        lw, ll = len(beginWord), len(wordList)
        for i in range(ll):
            map1[wordList[i]] = i
            map2[i] = wordList[i]
        buckets = defaultdict(list)
        for i in range(ll):
            for k in range(lw):
                match = wordList[i][:k] + '_' + wordList[i][k + 1:]
                buckets[match].append(map1[wordList[i]])
        values = buckets.values()
        adjacency = defaultdict(list)
        for j in values:
            for i in range(len(j)):
                adjacency[j[i]].extend(j[:i] + j[i + 1:])
        cost = [-1] * ll
        cost[map1[beginWord]] = 0

        def bfs(vi):
            qu = deque()
            qu.append([vi])
            while qu:
                a = qu.popleft()
                for i in adjacency[a[-1]]:
                    if cost[i] == -1:
                        cost[i] = cost[a[-1]] + 1
                        if i == map1[endWord]:
                            return cost[i]+1
                        qu.append(a + [i])
            return 0

        return bfs(map1[beginWord])


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Solution().ladderLength(beginWord,endWord,wordList)
