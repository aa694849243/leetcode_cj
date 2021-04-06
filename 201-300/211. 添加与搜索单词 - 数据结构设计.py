'''
设计一个支持以下两种操作的数据结构：

void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。

示例:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
说明:

你可以假设所有单词都是由小写字母 a-z 组成的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-and-search-word-data-structure-design
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lookup = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.lookup
        for i in word:
            tree.setdefault(i, {})
            tree = tree[i]
        tree["#"] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def dfs(word, tree):
            if not word:
                return True if '#' in tree else False
            # if len(tree) == 1 and '#' in tree:
            #     return False
            if word[0] in tree:
                return dfs(word[1:], tree[word[0]])
            elif word[0] == '.':
                for x in tree:
                    if dfs(word[1:], tree[x]):
                        return True
            return False

        return dfs(word, self.lookup)

x = WordDictionary()
x.addWord('at')
x.search('.at')
x.addWord('bat')
x.search('.at')
x.search('ab.')
x.search('....')
x.search('a...')

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import defaultdict
        self.lookup = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.lookup
        for a in word:
            tree = tree.setdefault(a, {})
        tree["#"] = {}

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def helper(word, tree):
            if not word:
                if "#" in tree:
                    return True
                return False
            if word[0] == ".":
                for t in tree:
                    if helper(word[1:], tree[t]):
                        return True
            elif word[0] in tree:
                if helper(word[1:], tree[word[0]]):
                    return True
            return False

        return helper(word, self.lookup)
x = WordDictionary()
x.addWord('a')
x.addWord('ab')
x.search('.')
x.search('..')
x.search('ab.')
x.search('.a')
x.search('a.')
