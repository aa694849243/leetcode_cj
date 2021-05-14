# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 给定一个由 0 和 1 组成的数组 A，将数组分成 3 个非空的部分，使得所有这些部分表示相同的二进制值。
#
#  如果可以做到，请返回任何 [i, j]，其中 i+1 < j，这样一来：
#
#
#  A[0], A[1], ..., A[i] 组成第一部分；
#  A[i+1], A[i+2], ..., A[j-1] 作为第二部分；
#  A[j], A[j+1], ..., A[A.length - 1] 是第三部分。
#  这三个部分所表示的二进制值相等。
#
#
#  如果无法做到，就返回 [-1, -1]。
#
#  注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如，[1,1,0] 表示十进制中的 6，而不会是 3。此外，前导零也是被允许的，所以 [0,
# 1,1] 和 [1,1] 表示相同的值。
#
#
#
#  示例 1：
#
#  输入：[1,0,1,0,1]
# 输出：[0,3]
#
#
#  示例 2：
#
#  输出：[1,1,0,1,1]
# 输出：[-1,-1]
#
#
#
#  提示：
#
#
#  3 <= A.length <= 30000
#  A[i] == 0 或 A[i] == 1
#
#
#
#  Related Topics 贪心算法 数学 二分查找
#  👍 47 👎 0


class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        a = sum(arr)
        if a % 3: return [-1, -1]  # 重量必须三等分
        if a == 0: return [0, len(arr) - 1]
        T = a // 3
        su = 0
        breaks = []
        for i, val in enumerate(arr):
            if val:
                su += val
                if su in {1, T + 1, 2 * T + 1}:  # 第1个1
                    breaks.append(i)
                if su in {T, 2 * T, 3 * T}:
                    breaks.append(i)
        i1, i2, j1, j2, k1, k2 = breaks
        if not arr[i1:i2+1]==arr[j1:j2+1]==arr[k1:k2+1]: return [-1,-1] #每一段都要相等，比如‘1101’‘111’就是不同的
        zero1 = j1 - i2 - 1
        zero2 = k1 - j2 - 1
        zero3 = len(arr) - k2 - 1  # 计算每个0的余量，最后一个的余量一定要是最少的，因为后面的要算进位，二前面的可以算成前导0，不计数
        if zero1 < zero3 or zero2 < zero3: return [-1, -1]
        return [i2 + zero3, j2 + zero3 + 1]
Solution().threeEqualParts([1,1,1,0,0,1,1,0,1,0,1,1,1,1,1,1])