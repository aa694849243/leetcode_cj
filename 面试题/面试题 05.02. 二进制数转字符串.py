#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 二进制数转字符串。给定一个介于0和1之间的实数（如0.72），类型为double，打印它的二进制表达式。如果该数字无法精确地用32位以内的二进制表示，则打印
# “ERROR”。
#
#  示例1:
#
#
#  输入：0.625
#  输出："0.101"
#
#
#  示例2:
#
#
#  输入：0.1
#  输出："ERROR"
#  提示：0.1无法被二进制准确表示
#
#
#  提示：
#
#
#  32位包括输出中的"0."这两位。
#
#  Related Topics 位运算 数学 字符串
#  👍 24 👎 0


class Solution:
    def printBin(self, num: float) -> str:
        ans='0.'
        while num!=0 and len(ans)<=33:
            num*=2
            if num>=1:
                ans+='1'
                num-=1
            else:
                ans+='0'
        return ans if num==0 else 'ERROR'
