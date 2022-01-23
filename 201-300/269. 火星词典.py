# -*- coding: utf-8 -*-
import heapq
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 现有一种使用英语字母的火星语言，这门语言的字母顺序与英语顺序不同。
#
#  给你一个字符串列表 words ，作为这门语言的词典，words 中的字符串已经 按这门新语言的字母顺序进行了排序 。
#
#  请你根据该词典还原出此语言中已知的字母顺序，并 按字母递增顺序 排列。若不存在合法字母顺序，返回 "" 。若存在多种可能的合法字母顺序，返回其中 任意一种
#  顺序即可。
#
#  字符串 s 字典顺序小于 字符串 t 有两种情况：
#
#
#  在第一个不同字母处，如果 s 中的字母在这门外星语言的字母顺序中位于 t 中字母之前，那么 s 的字典顺序小于 t 。
#  如果前面 min(s.length, t.length) 字母都相同，那么 s.length < t.length 时，s 的字典顺序也小于 t 。
#
#
#
#
#  示例 1：
#
#
# 输入：words = ["wrt","wrf","er","ett","rftt"]
# 输出："wertf"
#
#
#  示例 2：
#
#
# 输入：words = ["z","x"]
# 输出："zx"
#
#
#  示例 3：
#
#
# 输入：words = ["z","x","z"]
# 输出：""
# 解释：不存在合法字母顺序，因此返回 "" 。
#
#
#
#
#  提示：
#
#
#  1 <= words.length <= 100
#  1 <= words[i].length <= 100
#  words[i] 仅由小写英文字母组成
#
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 数组 字符串 👍 195 👎 0


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return ''.join(set(words[0]))
        wsum = set(''.join(words))
        g = collections.defaultdict(list)
        for i in range(1, len(words)):
            for j in range(min(len(words[i]), len(words[i - 1]))):
                if words[i][j] != words[i - 1][j]:
                    g[words[i - 1][j]].append(words[i][j])
                    break
            else:
                if len(words[i - 1]) > len(words[i]):
                    return ''
        indegree = collections.defaultdict(int)
        for ch in g:
            for nxt in g[ch]:
                indegree[nxt] += 1
        zeros = [w for w in wsum if indegree[w] == 0]
        heapq.heapify(zeros)
        ans = ''
        while zeros:
            ch = heapq.heappop(zeros)
            ans += ch
            for nxt in g[ch]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    heapq.heappush(zeros, nxt)
        return ans if len(ans) == len(wsum) else ''  # 防止访问不全的情况，所以len(ans)==len(wsum)
