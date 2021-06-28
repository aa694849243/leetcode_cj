# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一个字符串 s ，每一次操作你都可以在字符串的任意位置插入任意字符。
#
#  请你返回让 s 成为回文串的 最少操作次数 。
#
#  「回文串」是正读和反读都相同的字符串。
#
#
#
#  示例 1：
#
#
# 输入：s = "zzazz"
# 输出：0
# 解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。
#
#
#  示例 2：
#
#
# 输入：s = "mbadm"
# 输出：2
# 解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。
#
#
#  示例 3：
#
#
# 输入：s = "leetcode"
# 输出：5
# 解释：插入 5 个字符后字符串变为 "leetcodocteel" 。
#
#
#  示例 4：
#
#
# 输入：s = "g"
# 输出：0
#
#
#  示例 5：
#
#
# 输入：s = "no"
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 500
#  s 中所有字符都是小写字母。
#
#  Related Topics 字符串 动态规划
#  👍 99 👎 0


class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        cost=[[0]*n for _ in range(n)]
        for leng in range(2,n+1):
            for l in range(n-leng+1):
                r=l+leng-1
                if l+1==r: #长度为2的字符串特殊处理，这里可以不处理，但模板适用于各种情况
                    cost[l][r]=1 if s[l]!=s[r] else 0
                else:
                    if s[l]==s[r]:
                        cost[l][r]=cost[l+1][r-1]
                    else:
                        cost[l][r]=min(cost[l+1][r],cost[l][r-1])+1
        return cost[0][n-1]
Solution().minInsertions("g")