# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List
# 给定一个二进制字符串 S（一个仅由若干 '0' 和 '1' 构成的字符串）和一个正整数 N，如果对于从 1 到 N 的每个整数 X，其二进制表示都是 S 的
# 子串，就返回 true，否则返回 false。
#
#
#
#  示例 1：
#
#  输入：S = "0110", N = 3
# 输出：true
#
#
#  示例 2：
#
#  输入：S = "0110", N = 4
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= S.length <= 1000
#  1 <= N <= 10^9
#
#  Related Topics 字符串
#  👍 26 👎 0


class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for num in range(n,n>>1,-1): #n>>1~1里面的值为x,则x<<1都被我们遍历了
            if bin(num)[2:] not in s:
                return False
        return True