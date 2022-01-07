# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个二进制串 s （一个只包含 0 和 1 的字符串），我们可以将 s 分割成 3 个 非空 字符串 s1, s2, s3 （s1 + s2 + s3
# = s）。
#
#  请你返回分割 s 的方案数，满足 s1，s2 和 s3 中字符 '1' 的数目相同。
#
#  由于答案可能很大，请将它对 10^9 + 7 取余后返回。
#
#
#
#  示例 1：
#
#  输入：s = "10101"
# 输出：4
# 解释：总共有 4 种方法将 s 分割成含有 '1' 数目相同的三个子字符串。
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
#
#
#  示例 2：
#
#  输入：s = "1001"
# 输出：0
#
#
#  示例 3：
#
#  输入：s = "0000"
# 输出：3
# 解释：总共有 3 种分割 s 的方法。
# "0|0|00"
# "0|00|0"
# "00|0|0"
#
#
#  示例 4：
#
#  输入：s = "100100010100110"
# 输出：12
#
#
#
#
#  提示：
#
#
#  s[i] == '0' 或者 s[i] == '1'
#  3 <= s.length <= 10^5
#
#  Related Topics 数学 字符串 👍 8 👎 0


class Solution:
    def numWays(self, s: str) -> int:
        if len(s) < 3:
            return 0
        m = collections.Counter(s)
        mod = 10 ** 9 + 7
        n = len(s)
        x = m['1']
        if x % 3:
            return 0
        if x == 0:
            return ((n - 1) * (n - 2) // 2) % mod
        x //= 3
        cnt = 0
        pre = 0
        aft = 0
        for ch in s:
            if ch == '1':
                cnt += 1
            if cnt == x:
                pre += 1
            elif cnt == 2 * x:
                aft += 1
        return (pre * aft) % mod
