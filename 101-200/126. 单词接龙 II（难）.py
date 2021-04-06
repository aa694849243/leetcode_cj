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
        if beginWord not in wordList:
            wordList = [beginWord] + wordList
        map1, map2 = {}, {}
        stop = len(wordList)
        # 构造映射id
        for i in range(stop):
            map1[wordList[i]] = i
            map2[i] = wordList[i]
        # 做桶
        buckets = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                match = word[:i] + '_' + word[i + 1:]
                buckets[match].append(map1[word])
        # 做邻接表
        buckets2 = defaultdict(list)
        values = buckets.values()
        for i in values:
            for j in i:
                buckets2[j].extend(i)
                buckets2[j].remove(j)
        cost = [float('inf')] * stop  # cost表示从beginword到i处数组的转换代价
        res = []
        cost[map1[beginWord]] = 0

        def bfs(vi):
            qu = deque()
            qu.append([vi])
            while qu:
                a = qu.popleft()
                for i in buckets2[a[-1]]:
                    if cost[a[-1]] >= cost[map1[endWord]]:
                        return
                    if cost[i] >= cost[a[-1]] + 1:
                        cost[i] = cost[a[-1]] + 1
                        qu.append(a + [i])
                        if i == map1[endWord]:
                            res.append(a + [i])

        bfs(map1[beginWord])

        res2 = []
        for m in res:
            ans2 = []
            for n in m:
                ans2.append(map2[n])
            res2.append(ans2)
        return res2
Solution().findLadders(beginWord, endWord, wordList)
# 先做桶再做邻接表
