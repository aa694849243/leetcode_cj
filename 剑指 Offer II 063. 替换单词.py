# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 22:50 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.f = {}

    def search(self, word):
        tree = self.f
        for c in word:
            if c not in tree:
                return False
            tree = tree[c]
        return '#' in tree

    def insert(self, word):
        tree = self.f
        for c in word:
            if c not in tree:
                tree[c] = {}
            tree = tree[c]
        tree['#'] = True


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        ans = []
        for word in sentence.split():
            tree = trie.f
            for i, c in enumerate(word):
                if c not in tree:
                    ans.append(word)
                    break
                tree = tree[c]
                if '#' in tree:
                    ans.append(word[:i + 1])
                    break
            else:
                ans.append(word)
        return ' '.join(ans)
# leetcode submit region end(Prohibit modification and deletion)

