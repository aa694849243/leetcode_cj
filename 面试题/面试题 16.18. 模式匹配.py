#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections


# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatg
# o"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相
# 同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。
#
#  示例 1：
#
#  输入： pattern = "abba", value = "dogcatcatdog"
# 输出： true
#
#
#  示例 2：
#
#  输入： pattern = "abba", value = "dogcatcatfish"
# 输出： false
#
#
#  示例 3：
#
#  输入： pattern = "aaaa", value = "dogcatcatdog"
# 输出： false
#
#
#  示例 4：
#
#  输入： pattern = "abba", value = "dogdogdogdog"
# 输出： true
# 解释： "a"="dogdog",b=""，反之也符合规则
#
#
#  提示：
#
#
#  1 <= len(pattern) <= 1000
#  0 <= len(value) <= 1000
#  你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。
#
#  Related Topics 数学 字符串 回溯 枚举
#  👍 117 👎 0


class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        c = collections.Counter(pattern)
        sum_ = len(value)
        a, b = c['a'], c['b']
        if a < b:
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
            a, b = b, a
        if not value:
            return b == 0
        if not pattern:
            return False
        for len_a in range(sum_ // a + 1):
            rest = sum_ - len_a * a
            if (rest == 0 and b == 0) or (b != 0 and rest % b == 0):
                len_b = 0 if b == 0 else rest // b
                pos, correct = 0, True
                v_a, v_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        if not v_a:
                            v_a = value[pos:pos + len_a]
                        elif value[pos:pos + len_a] != v_a:
                            correct = False
                            break
                        pos += len_a
                    else:
                        if not v_b:
                            v_b = value[pos:pos + len_b]
                        elif value[pos:pos + len_b] != v_b:
                            correct = False
                            break
                        pos += len_b
                if correct and v_a != v_b:
                    return True
        return False
