#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定两个字符串 s 和 t，判断他们的编辑距离是否为 1。
#
#  注意：
#
#  满足编辑距离等于 1 有三种可能的情形：
#
#
#  往 s 中插入一个字符得到 t
#  从 s 中删除一个字符得到 t
#  在 s 中替换一个字符得到 t
#
#
#  示例 1：
#
#  输入: s = "ab", t = "acb"
# 输出: true
# 解释: 可以将 'c' 插入字符串 s 来得到 t。
#
#
#  示例 2:
#
#  输入: s = "cab", t = "ad"
# 输出: false
# 解释: 无法通过 1 步操作使 s 变为 t。
#
#  示例 3:
#
#  输入: s = "1203", t = "1213"
# 输出: true
# 解释: 可以将字符串 s 中的 '0' 替换为 '1' 来得到 t。
#  Related Topics 双指针 字符串
#  👍 86 👎 0


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        s, t = (s, t) if len(s) >= len(t) else (t, s)
        cnt = 1
        st1 = list(s)
        st2 = list(t)
        if len(s) == len(t)+1:
            while st1:
                if not st2:
                    return cnt == 1 and len(st1) == 1
                if st1[-1] != st2[-1]:
                    if cnt > 0:
                        cnt -= 1
                        st1.pop()
                    else:
                        return False
                else:
                    st1.pop()
                    st2.pop()
                    if not st1 and not st2:
                        return cnt==0
            return False
        elif len(s) - len(t) == 0:
            while st1:
                if st1[-1] != st2[-1]:
                    if cnt > 0:
                        cnt -= 1
                    else:
                        return False
                st1.pop()
                st2.pop()
                if not st1 and not st2:
                    return cnt==0
        return False
Solution().isOneEditDistance("acbbcda" , "abbdad")