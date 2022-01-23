#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bisect
from typing import List

from sortedcontainers import SortedSet


# N 个灯泡排成一行，编号从 1 到 N 。最初，所有灯泡都关闭。每天只打开一个灯泡，直到 N 天后所有灯泡都打开。
#
#  给你一个长度为 N 的灯泡数组 blubs ，其中 bulls[i] = x 意味着在第 (i+1) 天，我们会把在位置 x 的灯泡打开，其中 i 从 0
#  开始，x 从 1 开始。
#
#  给你一个整数 K ，请你输出在第几天恰好有两个打开的灯泡，使得它们中间 正好 有 K 个灯泡且这些灯泡 全部是关闭的 。
#
#  如果不存在这种情况，返回 -1 。如果有多天都出现这种情况，请返回 最小的天数 。
#
#
#
#  示例 1：
#
#
# 输入：
# bulbs: [1,3,2]
# K: 1
# 输出：2
# 解释：
# 第一天 bulbs[0] = 1，打开第一个灯泡 [1,0,0]
# 第二天 bulbs[1] = 3，打开第三个灯泡 [1,0,1]
# 第三天 bulbs[2] = 2，打开第二个灯泡 [1,1,1]
# 返回2，因为在第二天，两个打开的灯泡之间恰好有一个关闭的灯泡。
#
#
#  示例 2：
#
#
# 输入：
# bulbs: [1,2,3]
# k: 1
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= N <= 20000
#  1 <= bulbs[i] <= N
#  bulbs 是一个由从 1 到 N 的数字构成的排列
#  0 <= K <= 20000
#
#  Related Topics 树状数组 数组 有序集合 滑动窗口
#  👍 59 👎 0
# https://leetcode-cn.com/problems/k-empty-slots/solution/cpython3-1you-xu-ji-he-by-hanxin_hanxin-jzjb/
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        li = SortedSet()
        for i, x in enumerate(bulbs):
            li.add(x)
            r = bisect.bisect_right(li, x)
            if r < len(li):
                if li[r] - x == k + 1:
                    return i + 1
            l = bisect.bisect_left(li, x) - 1
            if l >= 0:
                if x - li[l] == k + 1:
                    return i + 1
        return -1


class ftree:
    def __init__(self, n):
        self.li = [0] * (n + 1)
        self.n = n

    @staticmethod
    def lowbit(num):
        return num & -num

    def update(self, i, diff):
        while i <= self.n:
            self.li[i] += diff
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.li[i]
            i -= self.lowbit(i)
        return res


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        tree = ftree(n)
        visted = set()
        for i, num in enumerate(bulbs):
            visted.add(num)
            tree.update(num, 1)
            l = num - k - 1
            if l > 0 and l in visted:
                if tree.query(num) - tree.query(l) == 1:
                    return i + 1
            r = num + k + 1
            if r <= n and r in visted:
                if tree.query(r) - tree.query(num) == 1:
                    return i + 1
        return -1


# 标准线段树
class segtree:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left = None
        self.right = None
        self.treesum = 0

    @property
    def _mid(self):
        return (self.l + self.r) // 2

    @property
    def _left(self):
        self.left=self.left or segtree(self.l, self._mid)
        return self.left
    @property
    def _right(self):
        self.right=self.right or segtree(self._mid + 1, self.r)
        return self.right

    def update(self, id, diff):
        self.treesum += diff
        if self.l >= self.r:
            return
        if id <= self._mid:
            self._left.update(id, diff)
        else:
            self._right.update(id, diff)

    def query(self, ql, qr):
        if qr < self.l or ql > self.r:
            return 0
        if ql <= self.l and qr >= self.r:
            return self.treesum
        return self._left.query(ql, qr) + self._right.query(ql, qr)


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        n = len(bulbs)
        tree = segtree(0, n)
        visted = set()
        for i, id in enumerate(bulbs):
            tree.update(id, 1)
            visted.add(id)
            l = id - k - 1
            if l in visted:
                diff = tree.query(l, id)
                if diff == 2:
                    return id
            r = id + k + 1
            if r in visted:
                diff = tree.query(id, r)
                if diff == 2:
                    return id
        return -1


Solution().kEmptySlots([1, 3, 2], 1)
