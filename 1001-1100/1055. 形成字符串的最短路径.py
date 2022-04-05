# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 对于任何字符串，我们可以通过删除其中一些字符（也可能不删除）来构造该字符串的子序列。
#
#  给定源字符串 source 和目标字符串 target，找出源字符串中能通过串联形成目标字符串的子序列的最小数量。如果无法通过串联源字符串中的子序列来构造
# 目标字符串，则返回 -1。
#
#
#
#  示例 1：
#
#  输入：source = "abc", target = "abcbc"
# 输出：2
# 解释：目标字符串 "abcbc" 可以由 "abc" 和 "bc" 形成，它们都是源字符串 "abc" 的子序列。
#
#
#  示例 2：
#
#  输入：source = "abc", target = "acdbc"
# 输出：-1
# 解释：由于目标字符串中包含字符 "d"，所以无法由源字符串的子序列构建目标字符串。
#
#
#  示例 3：
#
#  输入：source = "xyz", target = "xzyxz"
# 输出：3
# 解释：目标字符串可以按如下方式构建： "xz" + "y" + "xz"。
#
#
#
#
#  提示：
#
#
#  source 和 target 两个字符串都只包含 "a"-"z" 的英文小写字母。
#  source 和 target 两个字符串的长度介于 1 和 1000 之间。
#
#  Related Topics 贪心 字符串 动态规划 👍 73 👎 0


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        a = set(source)
        b = set(target)
        if a & b != b:
            return -1
        cnt = 0
        target = collections.deque(list(target))
        pq = collections.deque()
        while target:
            w = target.popleft()
            while pq and pq[0] != w:
                pq.popleft()
            if pq and pq[0] == w:
                pq.popleft()
                continue
            if not pq:
                cnt += 1
                pq = collections.deque(list(source))
                while pq and pq[0] != w:
                    pq.popleft()
                pq.popleft()
        return cnt
Solution().shortestWay("abc","abcbc")