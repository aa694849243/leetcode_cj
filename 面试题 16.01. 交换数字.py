#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 编写一个函数，不用临时变量，直接交换numbers = [a, b]中a与b的值。
#
#  示例：
#
#
# 输入: numbers = [1,2]
# 输出: [2,1]
#
#
#  提示：
#
#
#  numbers.length == 2
#  -2147483647 <= numbers[i] <= 2147483647
#
#  Related Topics 位运算 数学
#  👍 52 👎 0


class Solution:
    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] = numbers[0] ^ numbers[1]
        numbers[1] = numbers[0] ^ numbers[1]
        numbers[0] = numbers[0] ^ numbers[1]
        return numbers
