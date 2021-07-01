# -*- coding: utf-8 -*-
import heapq
from typing import List


# 给你一个整数数组 target 。一开始，你有一个数组 A ，它的所有元素均为 1 ，你可以执行以下操作：
#
#
#  令 x 为你数组里所有元素的和
#  选择满足 0 <= i < target.size 的任意下标 i ，并让 A 数组里下标为 i 处的值为 x 。
#  你可以重复该过程任意次
#
#
#  如果能从 A 开始构造出目标数组 target ，请你返回 True ，否则返回 False 。
#
#
#
#  示例 1：
#
#  输入：target = [9,3,5]
# 输出：true
# 解释：从 [1, 1, 1] 开始
# [1, 1, 1], 和为 3 ，选择下标 1
# [1, 3, 1], 和为 5， 选择下标 2
# [1, 3, 5], 和为 9， 选择下标 0
# [9, 3, 5] 完成
#
#
#  示例 2：
#
#  输入：target = [1,1,1,2]
# 输出：false
# 解释：不可能从 [1,1,1,1] 出发构造目标数组。
#
#
#  示例 3：
#
#  输入：target = [8,5]
# 输出：true
#
#
#
#
#  提示：
#
#
#  N == target.length
#  1 <= target.length <= 5 * 10^4
#  1 <= target[i] <= 10^9
#
#  Related Topics 数组 堆（优先队列）
#  👍 59 👎 0


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        if len(target) == 1:
            return target[0]==1
        li = []
        for val in target:
            heapq.heappush(li, -val)
        while li[0] != -1:
            s = -sum(li)
            x, y = heapq.heappop(li), heapq.heappop(li)
            x *= -1
            y *= -1
            k = (x - y - 1) // (s - x) + 1
            if y != 1:
                x -= k * (s - x)
                if x == y or x < 1:
                    return False
                heapq.heappush(li, -x)
                heapq.heappush(li, -y)
            else:
                return x - k * (s - x) == 1


Solution().isPossible([25, 1, 1, 37, 1, 3, 1])
