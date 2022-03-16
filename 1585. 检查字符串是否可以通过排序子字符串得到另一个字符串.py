#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给你两个字符串 s 和 t ，请你通过若干次以下操作将字符串 s 转化成字符串 t ：
#
#
#  选择 s 中一个 非空 子字符串并将它包含的字符就地 升序 排序。
#
#
#  比方说，对下划线所示的子字符串进行操作可以由 "14234" 得到 "12344" 。
#
#  如果可以将字符串 s 变成 t ，返回 true 。否则，返回 false 。
#
#  一个 子字符串 定义为一个字符串中连续的若干字符。
#
#
#
#  示例 1：
#
#
# 输入：s = "84532", t = "34852"
# 输出：true
# 解释：你可以按以下操作将 s 转变为 t ：
# "84532" （从下标 2 到下标 3）-> "84352"
# "84352" （从下标 0 到下标 2） -> "34852"
#
#
#  示例 2：
#
#
# 输入：s = "34521", t = "23415"
# 输出：true
# 解释：你可以按以下操作将 s 转变为 t ：
# "34521" -> "23451"
# "23451" -> "23415"
#
#
#  示例 3：
#
#
# 输入：s = "12345", t = "12435"
# 输出：false
#
#
#  示例 4：
#
#
# 输入：s = "1", t = "2"
# 输出：false
#
#
#
#
#  提示：
#
#
#  s.length == t.length
#  1 <= s.length <= 105
#  s 和 t 都只包含数字字符，即 '0' 到 '9' 。
#
#  Related Topics 贪心 字符串 排序
#  👍 51 👎 0
import collections


# 小的数的无法向上转移
class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        n = len(s)
        pos = {i: collections.deque() for i in range(10)}
        for i, dig in enumerate(s):
            d = int(dig)
            pos[d].append(i)
        for i, dig in enumerate(t):
            d = int(dig)
            if not pos[d]:
                return False
            if any(pos[j] and pos[j][0]<pos[d][0] for j in range(d)): #每次定位的是当前最低格子的数，所以当前格子左边的数必须都要大于当前格子数，要不然会阻挡比它小的数转移到右边
                return False
            pos[d].popleft()
        return True

