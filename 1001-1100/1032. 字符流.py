# -*- coding: utf-8 -*-
import collections
from functools import reduce
from typing import List


# 按下述要求实现 StreamChecker 类：
#
#
#  StreamChecker(words)：构造函数，用给定的字词初始化数据结构。
#  query(letter)：如果存在某些 k >= 1，可以用查询的最后 k个字符（按从旧到新顺序，包括刚刚查询的字母）拼写出给定字词表中的某一字词时，返
# 回 true。否则，返回 false。
#
#
#
#
#  示例：
#
#  StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // 初始化字典
# streamChecker.query('a');          // 返回 false
# streamChecker.query('b');          // 返回 false
# streamChecker.query('c');          // 返回 false
# streamChecker.query('d');          // 返回 true，因为 'cd' 在字词表中
# streamChecker.query('e');          // 返回 false
# streamChecker.query('f');          // 返回 true，因为 'f' 在字词表中
# streamChecker.query('g');          // 返回 false
# streamChecker.query('h');          // 返回 false
# streamChecker.query('i');          // 返回 false
# streamChecker.query('j');          // 返回 false
# streamChecker.query('k');          // 返回 false
# streamChecker.query('l');          // 返回 true，因为 'kl' 在字词表中。
#
#
#
#  提示：
#
#
#  1 <= words.length <= 2000
#  1 <= words[i].length <= 2000
#  字词只包含小写英文字母。
#  待查项只包含小写英文字母。
#  待查项最多 40000 个。
#
#  Related Topics 字典树
#  👍 59 👎 0
# 不做笔记
class StreamChecker:

    def __init__(self, words: List[str]):
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()
        for word in words:
            reduce(dict.__getitem__, word[::-1], self.trie)['#'] = word
        self.q = ''

    def query(self, letter: str) -> bool:
        self.q += letter
        cur = self.trie
        for ch in self.q[::-1]:
            if ch not in cur:
                return False
            if '#' in cur[ch]:
                return True
            cur = cur[ch]
        return False
# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
