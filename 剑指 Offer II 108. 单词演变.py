# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 20:45 
# ide： PyCharm
import collections

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        g = collections.defaultdict(list)
        wordList.append(beginWord)
        s = set(wordList)
        for word in wordList:
            for i, ch in enumerate(word):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    if letter != ch:
                        tmp = word[:i] + letter + word[i + 1:]
                        if tmp in s:
                            g[word].append(tmp)
        step = 0
        T = {beginWord}
        visted = {beginWord}
        while 1:
            tree = set()
            for word in T:
                if word == endWord:
                    return step + 1
                for next_word in g[word]:
                    if next_word not in visted:
                        tree.add(next_word)
                        visted.add(next_word)
            if not tree:
                break
            T = tree
            step += 1
        return 0


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
)

