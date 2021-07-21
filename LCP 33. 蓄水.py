# -*- coding: utf-8 -*-
import heapq
from typing import List


# 给定 N 个无限容量且初始均空的水缸，每个水缸配有一个水桶用来打水，第 `i` 个水缸配备的水桶容量记作 `bucket[i]`。小扣有以下两种操作：
# - 升级水桶：选择任意一个水桶，使其容量增加为 `bucket[i]+1`
# - 蓄水：将全部水桶接满水，倒入各自对应的水缸
#
# 每个水缸对应最低蓄水量记作 `vat[i]`，返回小扣至少需要多少次操作可以完成所有水缸蓄水要求。
#
# 注意：实际蓄水量 **达到或超过** 最低蓄水量，即完成蓄水要求。
#
# **示例 1：**
# >输入：`bucket = [1,3], vat = [6,8]`
# >
# >输出：`4`
# >
# >解释：
# >第 1 次操作升级 bucket[0]；
# >第 2 ~ 4 次操作均选择蓄水，即可完成蓄水要求。
# ![vat1.gif](https://pic.leetcode-cn.com/1616122992-RkDxoL-vat1.gif)
#
#
#
# **示例 2：**
# >输入：`bucket = [9,0,1], vat = [0,2,2]`
# >
# >输出：`3`
# >
# >解释：
# >第 1 次操作均选择升级 bucket[1]
# >第 2~3 次操作选择蓄水，即可完成蓄水要求。
#
# **提示：**
# - `1 <= bucket.length == vat.length <= 100`
# - `0 <= bucket[i], vat[i] <= 10^4`
#  Related Topics 贪心 数组 堆（优先队列）
#  👍 27 👎 0


class Solution:
    def storeWater(self, bucket: List[int], vat: List[int]) -> int:
        step = 0
        li = []
        for i, val in enumerate(vat):
            if val == 0:
                li.append((0, i))
            elif bucket[i] == 0:
                li.append((float('-inf'), i))
            else:
                x = (val - 1) // bucket[i] + 1
                li.append((-x, i))
        heapq.heapify(li)

        minstep = float('inf')
        while step < minstep:
            cnt, i = heapq.heappop(li)
            minstep = min(step - cnt, minstep)
            step += 1
            bucket[i] += 1
            heapq.heappush(li, (-((vat[i] - 1) // bucket[i] + 1), i))
        return minstep


Solution().storeWater([9, 0, 1], [0, 2, 2])
