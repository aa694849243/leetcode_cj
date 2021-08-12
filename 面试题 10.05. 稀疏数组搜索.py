#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 稀疏数组搜索。有个排好序的字符串数组，其中散布着一些空字符串，编写一种方法，找出给定字符串的位置。
#
#  示例1:
#
#   输入: words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""],
#  s = "ta"
#  输出：-1
#  说明: 不存在返回-1。
#
#
#  示例2:
#
#   输入：words = ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""],
# s = "ball"
#  输出：4
#
#
#  提示:
#
#
#  words的长度在[1, 1000000]之间
#
#  Related Topics 数组 字符串 二分查找
#  👍 50 👎 0


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        def find(l, r):
            if l > r:
                return '', -1
            for i in range(l, r + 1):
                if words[i]:
                    return words[i], i
            return '', -1

        l, r = 0, len(words) - 1
        while l <= r:
            mid = (l + r) // 2
            t = words[mid]
            if not t:
                t, temp = find(mid + 1, r)
                if not t:
                    r = mid - 1
                    continue
                else:
                    mid = temp

            if t < s:
                l = mid + 1
            elif t > s:
                r = mid - 1
            else:
                return mid
        return -1


Solution().findString(["JgZkQBoFzW", "OOI Jhncw", "dHtFhkkXvGmbomYFsT", "hSrUyWaU"], "jgT ChqUFnkxyNdgfWxz")
