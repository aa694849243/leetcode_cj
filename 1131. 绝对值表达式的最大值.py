# -*- coding: utf-8 -*-
from typing import List


# 给你两个长度相等的整数数组，返回下面表达式的最大值：
#
#  |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
#
#  其中下标 i，j 满足 0 <= i, j < arr1.length。
#
#
#
#  示例 1：
#
#  输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# 输出：13
#
#
#  示例 2：
#
#  输入：arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
# 输出：20
#
#
#
#  提示：
#
#
#  2 <= arr1.length == arr2.length <= 40000
#  -10^6 <= arr1[i], arr2[i] <= 10^6
#
#  Related Topics 位运算 数学
#  👍 48 👎 0

# https://leetcode-cn.com/problems/maximum-of-absolute-value-expression/solution/python-jie-fa-bao-li-shu-xue-by-jiayangwu/
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        a = b = c = d = float('-inf')
        ami = bmi = cmi = dmi = float('inf')
        for i in range(len(arr1)):
            a, ami = max(a, arr1[i] + arr2[i] + i), min(ami, arr1[i] + arr2[i] + i)
            b, bmi = max(b, arr1[i] + arr2[i] - i), min(bmi, arr1[i] + arr2[i] - i)
            c, cmi = max(c, arr1[i] - arr2[i] + i), min(cmi, arr1[i] - arr2[i] + i)
            d, dmi = max(d, arr1[i] - arr2[i] - i), min(dmi, arr1[i] - arr2[i] - i)
        ans = max(a - ami, b - bmi, c - cmi, d - dmi)
        return ans
Solution().maxAbsValExpr([1,-2], [8,8])