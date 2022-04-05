# -*- coding: utf-8 -*-
import heapq
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个字符串 num 和一个整数 k 。其中，num 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 数位 。
#
#  你可以交换这个整数相邻数位的数字 最多 k 次。
#
#  请你返回你能得到的最小整数，并以字符串形式返回。
#
#
#
#  示例 1：
#
#
#
#
# 输入：num = "4321", k = 4
# 输出："1342"
# 解释：4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。
#
#
#  示例 2：
#
#
# 输入：num = "100", k = 1
# 输出："010"
# 解释：输出可以包含前导 0 ，但输入保证不会有前导 0 。
#
#
#  示例 3：
#
#
# 输入：num = "36789", k = 1000
# 输出："36789"
# 解释：不需要做任何交换。
#
#
#  示例 4：
#
#
# 输入：num = "22", k = 22
# 输出："22"
#
#
#  示例 5：
#
#
# 输入：num = "9438957234785635408", k = 23
# 输出："0345989723478563548"
#
#
#
#
#  提示：
#
#
#  1 <= num.length <= 30000
#  num 只包含 数字 且不含有 前导 0 。
#  1 <= k <= 10^9
#
#  Related Topics 贪心 树状数组 线段树 字符串 👍 61 👎 0

class ftree:
    def __init__(self, n):
        self.li = [0] * (n + 1)
        self.n = n

    @staticmethod
    def lowbit(num):
        return num & (-num)

    def update(self, num, dt):
        while num <= self.n:
            self.li[num] += dt
            num += self.lowbit(num)

    def quiry(self, num):
        ans = 0
        while num > 0:
            ans += self.li[num]
            num -= self.lowbit(num)
        return ans

    def quiryrange(self, x, y):  # 求[x+1,y]的个数
        return self.quiry(y) - self.quiry(x)


# https://leetcode-cn.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/solution/zui-duo-k-ci-jiao-huan-xiang-lin-shu-wei-hou-de-da/
class Solution:
    def minInteger(self, num: str, k: int) -> str:
        m = [[] for _ in range(10)]
        for i, ch in enumerate(num):  # i+1指的是从1位开始，0-9分别存到相应位置上
            m[int(ch)].append(i + 1)
        for i in range(10):  # 离最高位近的先弹出
            m[i] = m[i][::-1]
        tree = ftree(len(num))
        ans = ''
        for i in range(len(num)):  # 从最高位到最低位遍历，找最近的最小的值交换到最低位
            for j in range(10):
                if m[j]:
                    behind = tree.quiryrange(m[j][-1], len(num))  # 从m[j][-1]位置后交换到前面的个数
                    # 注意m[j][-1]==i时相当于次序不变，+0是正常的，另外m[j][-1]<i的情况是不可能的,因为小的在前面的已经遍历过了，最多就是不变
                    dist = m[j][-1] - 1 - i + behind
                    if dist <= k:  # 每次至少找到一个字母符合要求，最惨情况不变嘛
                        k -= dist
                        tree.update(m[j].pop(), 1)
                        ans += str(j)
                        break
        return ans
