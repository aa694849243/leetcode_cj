#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 给定一个字符串，对该字符串可以进行 “移位” 的操作，也就是将字符串中每个字母都变为其在字母表中后续的字母，比如："abc" -> "bcd"。这样，我们可
# 以持续进行 “移位” 操作，从而生成如下移位序列：
#
#  "abc" -> "bcd" -> ... -> "xyz"
#
#  给定一个包含仅小写字母字符串的列表，将该列表中所有满足 “移位” 操作规律的组合进行分组并返回。
#
#
#
#  示例：
#
#  输入：["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
# 输出：
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# 解释：可以认为字母表首尾相接，所以 'z' 的后续为 'a'，所以 ["az","ba"] 也满足 “移位” 操作规律。
#  Related Topics 数组 哈希表 字符串
#  👍 69 👎 0


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        m = collections.defaultdict(list)

        def cal(w):
            li = [ord(ch) - 97 for ch in w]
            return tuple((li[i] - li[i - 1]) % 26 for i in range(1, len(w)))

        for word in strings:
            if len(word) == 1:
                m[1].append(word)
            else:
                m[cal(word)].append(word)
        return list(m.values())