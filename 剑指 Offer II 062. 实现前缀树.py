# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 22:41 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.f = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.f
        for ch in word:
            if ch not in tree:
                tree[ch] = {}
            tree = tree[ch]
        tree['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.f
        for ch in word:
            if ch not in tree:
                return False
            tree = tree[ch]
        return '#' in tree

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.f
        for ch in prefix:
            if ch not in tree:
                return False
            tree = tree[ch]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)

