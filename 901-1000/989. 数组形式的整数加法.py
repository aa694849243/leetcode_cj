# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
#
#  给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
#
#
#
#
#
#
#  示例 1：
#
#  输入：A = [1,2,0,0], K = 34
# 输出：[1,2,3,4]
# 解释：1200 + 34 = 1234
#
#
#  示例 2：
#
#  输入：A = [2,7,4], K = 181
# 输出：[4,5,5]
# 解释：274 + 181 = 455
#
#
#  示例 3：
#
#  输入：A = [2,1,5], K = 806
# 输出：[1,0,2,1]
# 解释：215 + 806 = 1021
#
#
#  示例 4：
#
#  输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
# 输出：[1,0,0,0,0,0,0,0,0,0,0]
# 解释：9999999999 + 1 = 10000000000
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 10000
#  0 <= A[i] <= 9
#  0 <= K <= 10000
#  如果 A.length > 1，那么 A[0] != 0
#
#  Related Topics 数组
#  👍 151 👎 0


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k = list(str(k))
        for i in range((n := len(num)) - 1, -1, -1):
            if k:
                num[i] += int(k.pop())
            else:
                break
        while k:
            num=[int(k.pop())]+num
        carry = 0
        n=len(num)
        for i in range(n - 1, -1, -1):
            num[i] += carry
            carry, remain = divmod(num[i], 10)
            num[i] = remain
        if carry:
            num=[carry]+num
        return num
Solution().addToArrayForm([6], 809)