'''给定多个 words，words[i] 的权重为 i 。

设计一个类 WordFilter 实现函数WordFilter.f(String prefix, String suffix)。这个函数将返回具有前缀 prefix 和后缀suffix 的词的最大权重。如果没有这样的词，返回 -1。

例子:

输入:
WordFilter(["apple"])
WordFilter.f("a", "e") // 返回 0
WordFilter.f("b", "") // 返回 -1
注意:

words的长度在[1, 15000]之间。
对于每个测试用例，最多会有words.length次对WordFilter.f的调用。
words[i]的长度在[1, 10]之间。
prefix, suffix的长度在[0, 10]之前。
words[i]和prefix, suffix只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/prefix-and-suffix-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections
import functools

# 1双向字典树 超时
Trie = lambda: collections.defaultdict(Trie)
WEIGHT = '#'


class WordFilter(object):
    def __init__(self, words):  # 正向包括的所有值与反向包括的所有值取交集
        self.trie1 = Trie()  # prefix
        self.trie2 = Trie()  # suffix
        for weight, word in enumerate(words):
            cur = self.trie1
            self.addw(cur, weight)
            for letter in word:
                cur = cur[letter]
                self.addw(cur, weight)

            cur = self.trie2
            self.addw(cur, weight)
            for letter in word[::-1]:
                cur = cur[letter]
                self.addw(cur, weight)

    def addw(self, node, w):
        if WEIGHT not in node:
            node[WEIGHT] = {w}
        else:
            node[WEIGHT].add(w)

    def f(self, prefix, suffix):
        cur1 = self.trie1
        for letter in prefix:
            if letter not in cur1: return -1
            cur1 = cur1[letter]

        cur2 = self.trie2
        for letter in suffix[::-1]:
            if letter not in cur2: return -1
            cur2 = cur2[letter]

        return max(cur1[WEIGHT] & cur2[WEIGHT]) if cur1[WEIGHT] & cur2[WEIGHT] else -1


# Your WordFilter object will be instantiated and called as such:
# map妙用
# 2特殊字典树 首尾入字典树

from itertools import zip_longest

Trie = lambda: collections.defaultdict(Trie)
flag = '$'


class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()
        for weight, word in enumerate(words):
            cur = self.trie
            cur[flag] = weight
            for i, ch in enumerate(word):
                tmp = cur
                for s in word[i:]:
                    tmp = tmp[s, None]
                    tmp[flag] = weight
                tmp = cur
                for s in word[:-i or None][::-1]:
                    tmp = tmp[None, s]
                    tmp[flag] = weight
                cur = cur[word[i], word[~i]]
                cur[flag] = weight

    def f(self, prefix, suffix):
        cur = self.trie
        for a, b in zip_longest(prefix, suffix[::-1]):
            if (a, b) not in cur: return -1
            cur = cur[a, b]
        return cur[flag]


# 3构建长序列
class WordFilter(object):
    def __init__(self, words):
        self.trie = Trie()
        for weight, word in enumerate(words):
            cur = self.trie
            cur[flag] = weight
            word += '#'
            for i, ch in enumerate(word):
                tmp = cur
                for j in range(i, 2 * len(word) - 1):
                    tmp = tmp[word[j % len(word)]]
                    tmp[flag] = weight

    def f(self, prefix, suffix):
        s = suffix + '#' + prefix
        cur=self.trie
        for ch in s:
            if ch not in cur:return -1
            cur=cur[ch]
        return cur['$']


obj = WordFilter(['apbe', 'bce', 'bcee'])
obj.f('bce', 'e')
