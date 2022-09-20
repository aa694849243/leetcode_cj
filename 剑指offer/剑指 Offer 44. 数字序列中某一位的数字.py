#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，
# 等等。
#
#  请写一个函数，求任意第n位对应的数字。
#
#
#
#  示例 1：
#
#  输入：n = 3
# 输出：3
#
#
#  示例 2：
#
#  输入：n = 11
# 输出：0
#
#
#
#  限制：
#
#
#  0 <= n < 2^31
#
#
#  注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/
#  Related Topics 数学 二分查找
#  👍 147 👎 0


class Solution:
    def findNthDigit(self, n: int) -> int:
        for digit in range(1, 11):
            if n - 9 * digit * 10 ** (digit - 1) <= 0:
                break
            n -= 9 * digit * 10 ** (digit - 1)
        num = 10 ** (digit - 1) + (n - 1) // digit  # 因为10 ** (digit - 1)才是第一个，所以要-1
        a = str(num)[(n - 1) % digit]
        return int(a)


Solution().findNthDigit(3)
