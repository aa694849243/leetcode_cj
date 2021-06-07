# -*- coding: utf-8 -*-
import collections
from typing import List


# 在一个仓库里，有一排条形码，其中第 i 个条形码为 barcodes[i]。
#
#  请你重新排列这些条形码，使其中两个相邻的条形码 不能 相等。 你可以返回任何满足该要求的答案，此题保证存在答案。
#
#
#
#  示例 1：
#
#  输入：[1,1,1,2,2,2]
# 输出：[2,1,2,1,2,1]
#
#
#  示例 2：
#
#  输入：[1,1,1,1,2,2,3,3]
# 输出：[1,3,1,3,2,1,2,1]
#
#
#
#  提示：
#
#
#  1 <= barcodes.length <= 10000
#  1 <= barcodes[i] <= 10000
#
#
#
#  Related Topics 堆 排序
#  👍 67 👎 0


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        m = collections.Counter(barcodes)
        n = len(barcodes)
        ans = [0] * len(barcodes)
        p = 0
        li=sorted(m.keys(),key=lambda x:m[x],reverse=True)
        for key in li:
            while p < n and m[key] > 0:
                ans[p] = key
                m[key] -= 1
                p+=2
            if p >= n:
                break
        p = 1
        for key in li:
            while p < n and m[key] > 0:
                ans[p] = key
                m[key] -= 1
                p+=2
        return ans
