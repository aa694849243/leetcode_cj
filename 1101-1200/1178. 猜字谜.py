# -*- coding: utf-8 -*-
import collections
from typing import List


# 外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。
#
#  字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：
#
#
#  单词 word 中包含谜面 puzzle 的第一个字母。
#  单词 word 中的每一个字母都可以在谜面 puzzle 中找到。
#  例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"
# （不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）都不能作为谜底。
#
#
#  返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜
# 底的单词数目。
#
#
#
#  示例：
#
#
# 输入：
# words = ["aaaa","asas","able","ability","actt","actor","access"],
# puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
# 输出：[1,1,3,2,4,0]
# 解释：
# 1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"
# 1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
# 3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
# 2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
# 4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
# 没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。
#
#
#
#
#  提示：
#
#
#  1 <= words.length <= 10^5
#  4 <= words[i].length <= 50
#  1 <= puzzles.length <= 10^4
#  puzzles[i].length == 7
#  words[i][j], puzzles[i][j] 都是小写英文字母。
#  每个 puzzles[i] 所包含的字符都不重复。
#
#  Related Topics 位运算 哈希表
#  👍 206 👎 0

# 1状态压缩+哈希
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        m = collections.defaultdict(int)

        def calword(word):
            mask = 0
            a = set(word)
            if len(a) > 7:
                return
            for ch in set(word):
                mask |= (1 << (ord(ch) - 97))
            m[mask] += 1

        for word in words:
            calword(word)
        ans = []
        for puzzle in puzzles:
            amask = 0
            total = 0
            for ch in puzzle[1:]:
                amask |= (1 << (ord(ch) - 97))
            flag = amask
            while amask > 0:  # amask逐渐减小，向下搜索
                s = amask | (1 << (ord(puzzle[0]) - 97))  # 增加必要条件
                total += m[s]
                amask = (amask - 1) & flag  # 减少是可行的因为111-1最多只减少一个1，而反过来就不行了比如111+1->1000
            total += m[1 << (ord(puzzle[0]) - 97)]  # 增加只有首字母的情况
            ans.append(total)
        return ans


# 字典树类，前缀树类
class Trie:
    def __init__(self):
        self.child = dict()
        self.freq = 0


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        t = Trie()
        for word in words:
            a = sorted(set(word))
            if len(a) > 7:
                continue
            cur = t
            for ch in a:
                if ch not in cur.child:
                    cur.child[ch] = Trie()
                cur = cur.child[ch]
            cur.freq += 1

        def cal(puzzle, require, pos, cur):
            if not cur:
                return 0
            if pos == 7:  # 全部搜索完毕
                return cur.freq
            t = 0
            if puzzle[pos] in cur.child:  # 选择要这个字符
                t += cal(puzzle, require, pos + 1, cur.child[puzzle[pos]])
            if puzzle[pos] != require:  # 如果不是必要字符，这个字符可以舍弃,cur位置不变
                t += cal(puzzle, require, pos + 1, cur)
            return t

        ans = []
        for puzzle in puzzles:
            total = 0
            total += cal(sorted(puzzle), puzzle[0], 0, t)
            ans.append(total)
        return ans


Solution().findNumOfValidWords(["aaaa", "asas", "able", "ability", "actt", "actor", "access"], ["aboveyz", "abrodyz", "abslute", "absoryz", "actresz", "gaswxyz"])
