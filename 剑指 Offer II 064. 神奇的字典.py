# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 23:02 
# ide： PyCharm
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.f = {}

    def insert(self, word):
        t = self.f
        for i in word:
            if i not in t:
                t[i] = {}
            t = t[i]
        t['#'] = '#'

    def search(self, word, trie, cnt):
        tree = trie
        for i, ch in enumerate(word):
            if ch not in tree:
                if cnt == 1:
                    return False
                for s_ch in tree:
                    if s_ch != '#' and self.search(word[i + 1:], tree[s_ch], cnt + 1):
                        return True
                return False
            else:
                for s_ch in tree:
                    if s_ch != '#' and s_ch != ch and self.search(word[i + 1:], tree[s_ch], cnt + 1):
                        return True
                tree = tree[ch]
        return cnt == 1 and '#' in tree


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.trie.search(searchWord, self.trie.f, 0)


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
# leetcode submit region end(Prohibit modification and deletion)
obj = MagicDictionary()
obj.buildDict(["hello","hallo", "leetcode"])
print(obj.search("hello"))
print(obj.search("hhllo"))
