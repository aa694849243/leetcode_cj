#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 有些数的素因子只有 3，5，7，请设计一个算法找出第 k 个数。注意，不是必须有这些素因子，而是必须不包含其他的素因子。例如，前几个数按顺序应该是 1，3，
# 5，7，9，15，21。
#
#  示例 1:
#
#  输入: k = 5
#
# 输出: 9
#
#  Related Topics 哈希表 数学 动态规划 堆（优先队列）
#  👍 69 👎 0
import heapq


class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        pq = [1]
        ans = 0
        for _ in range(k):
            a = heapq.heappop(pq)
            while a <= ans:
                a = heapq.heappop(pq)
            heapq.heappush(pq, a * 3)
            heapq.heappush(pq, a * 5)
            heapq.heappush(pq, a * 7)
            ans=a
        return ans