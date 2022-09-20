#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
from typing import List


# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
#
#
#
#  示例 1：
#
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#
#
#  示例 2：
#
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0]
#
#
#
#  限制：
#
#
#  0 <= k <= arr.length <= 10000
#  0 <= arr[i] <= 10000
#
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列）
#  👍 271 👎 0


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapq.heapify(arr)
        ans = []
        while len(ans) < k:
            ans.append(heapq.heappop(arr))
        return ans


# 快速选择
import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def qsort(l, r):
            c = random.randint(l, r)
            arr[l], arr[c] = arr[c], arr[l]
            pivot = arr[l]
            j = l
            for i in range(l + 1, r + 1):
                if arr[i] <= pivot:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[j] = arr[j], arr[l]
            return j

        if k == 0:
            return []

        l, r = 0, len(arr) - 1
        x = qsort(l, r)
        while x != k - 1:
            if x < k - 1:
                l = x + 1
            else:
                r = x - 1
            x=qsort(l,r)
        return arr[:k]


Solution().getLeastNumbers([2, 1, 2, 2, 2], 3)
