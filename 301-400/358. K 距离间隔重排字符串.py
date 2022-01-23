#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections

# 给你一个非空的字符串 s 和一个整数 k，你要将这个字符串中的字母进行重新排列，使得重排后的字符串中相同字母的位置间隔距离至少为 k。
#
#  所有输入的字符串都由小写字母组成，如果找不到距离至少为 k 的重排结果，请返回一个空字符串 ""。
#
#  示例 1：
#
#  输入: s = "aabbcc", k = 3
# 输出: "abcabc"
# 解释: 相同的字母在新的字符串中间隔至少 3 个单位距离。
#
#
#  示例 2:
#
#  输入: s = "aaabc", k = 3
# 输出: ""
# 解释: 没有办法找到可能的重排结果。
#
#
#  示例 3:
#
#  输入: s = "aaadbbcc", k = 2
# 输出: "abacabcd"
# 解释: 相同的字母在新的字符串中间隔至少 2 个单位距离。
#
#  Related Topics 贪心 哈希表 字符串 计数 排序 堆（优先队列）
#  👍 80 👎 0
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        m = collections.Counter(s)
        pq = collections.deque()
        heap = []
        for key in m:
            heapq.heappush(heap, (-m[key], key))
        ans = ''
        for i in range(n := len(s)):
            if not heap:
                return ''
            val, ch = heapq.heappop(heap)
            ans += ch
            val += 1
            pq.append((val, ch))
            if i + 1 >= k:
                a = pq.popleft()
                if a[0] < 0:
                    heapq.heappush(heap, a)
        return ans


Solution().rearrangeString(s="aabbcc", k=3)

