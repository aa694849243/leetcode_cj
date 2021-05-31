# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
#
#
#
#  示例：
#
#  输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 30000
#  -10000 <= A[i] <= 10000
#  2 <= K <= 10000
#
#  Related Topics 数组 哈希表
#  👍 263 👎 0


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        cum = [0] + [*itertools.accumulate(nums)]
        m = collections.defaultdict(int)
        for i, val in enumerate(cum):
            cum[i] %= k
            m[cum[i]]+=1
        ans=0
        for val in m.values():
            ans+=(val*(val-1))//2
        return ans
