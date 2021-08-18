#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List

# 设计一个算法，找出数组中最小的k个数。以任意顺序返回这k个数均可。
#
#  示例：
#
#  输入： arr = [1,3,5,7,2,4,6,8], k = 4
# 输出： [1,2,3,4]
#
#
#  提示：
#
#
#  0 <= len(arr) <= 100000
#  0 <= k <= min(100000, len(arr))
#
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列）
#  👍 72 👎 0

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        from sortedcontainers import SortedList
        a = SortedList(arr)
        return a[:k]