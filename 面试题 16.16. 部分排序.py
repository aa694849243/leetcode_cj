#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给定一个整数数组，编写一个函数，找出索引m和n，只要将索引区间[m,n]的元素排好序，整个数组就是有序的。注意：n-m尽量最小，也就是说，找出符合条件的最短
# 序列。函数返回值为[m,n]，若不存在这样的m和n（例如整个数组是有序的），请返回[-1,-1]。
#  示例：
#  输入： [1,2,4,7,10,11,7,12,6,7,16,18,19]
# 输出： [3,9]
#
#  提示：
#
#  0 <= len(array) <= 1000000
#
#  Related Topics 栈 贪心 数组 双指针 排序 单调栈
#  👍 74 👎 0

# 双指针 水平线
class Solution:
    def subSort(self, array: List[int]) -> List[int]:
        mi = float('inf')
        res = [-1, -1]
        for i in range(len(array) - 1, -1, -1):
            if array[i] > mi:
                res[0] = i
            else:
                mi = array[i]
        ma = float('-inf')
        for i in range(len(array)):
            if array[i] < ma:
                res[1] = i
            else:
                ma = array[i]
        return res