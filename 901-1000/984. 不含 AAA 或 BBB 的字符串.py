# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 给定两个整数 A 和 B，返回任意字符串 S，要求满足：
#
#
#  S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
#  子串 'aaa' 没有出现在 S 中；
#  子串 'bbb' 没有出现在 S 中。
#
#
#
#
#  示例 1：
#
#  输入：A = 1, B = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
#
#
#  示例 2：
#
#  输入：A = 4, B = 1
# 输出："aabaa"
#
#
#
#  提示：
#
#
#  0 <= A <= 100
#  0 <= B <= 100
#  对于给定的 A 和 B，保证存在满足要求的 S。
#
#  Related Topics 贪心算法
#  👍 55 👎 0


class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ''
        l, r = 0, 0
        while a > 0 or b > 0:
            if l >= 2:
                l = 0
                ans += 'b'
                r = 1
                b -= 1
                continue
            if r >= 2:
                r = 0
                ans += 'a'
                l = 1
                a -= 1
                continue
            if a >= b:
                l += 1
                r = 0
                ans += 'a'
                a -= 1
            else:
                l = 0
                r += 1
                ans += 'b'
                b -= 1
        return ans
