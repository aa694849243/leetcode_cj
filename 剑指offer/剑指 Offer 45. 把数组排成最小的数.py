#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
#
#
#  示例 1:
#
#  输入: [10,2]
# 输出: "102"
#
#  示例 2:
#
#  输入: [3,30,34,5,9]
# 输出: "3033459"
#
#
#
#  提示:
#
#
#  0 < nums.length <= 100
#
#
#  说明:
#
#
#  输出结果可能非常大，所以你需要返回一个字符串而不是整数
#  拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0
#
#  Related Topics 贪心 字符串 排序
#  👍 246 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        li = list(map(str, nums))

        def qsort(lst, l, r):
            if l >= r:
                return
            pivot = lst[l]
            i = l
            for j in range(l + 1, r + 1):
                if lst[j] + pivot < pivot + lst[j]:
                    i+=1
                    lst[j],lst[i]=lst[i],lst[j]
            lst[l],lst[i]=lst[i],lst[l]
            qsort(lst,l,i-1)
            qsort(lst,i+1,r)
        qsort(li,0,len(li)-1)
        return ''.join(li)
Solution().minNumber([1,4,7,2,5,8,0,3,6,9])