# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一个整数 num，请你找出同时满足下面全部要求的两个整数：
#
#
#  两数乘积等于 num + 1 或 num + 2
#  以绝对差进行度量，两数大小最接近
#
#
#  你可以按任意顺序返回这两个整数。
#
#
#
#  示例 1：
#
#  输入：num = 8
# 输出：[3,3]
# 解释：对于 num + 1 = 9，最接近的两个因数是 3 & 3；对于 num + 2 = 10, 最接近的两个因数是 2 & 5，因此返回 3 & 3
# 。
#
#
#  示例 2：
#
#  输入：num = 123
# 输出：[5,25]
#
#
#  示例 3：
#
#  输入：num = 999
# 输出：[40,25]
#
#
#
#
#  提示：
#
#
#  1 <= num <= 10^9
#
#  Related Topics 数学
#  👍 19 👎 0


class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        a=num+1
        b=num+2
        for i in range(int(a**0.5),0,-1):
            if a%i==0:
                lia=[i,a//i]
                break
        for i in range(int(b**0.5),0,-1):
            if b%i==0:
                lib=[i,b//i]
                break
        return lia if abs(lia[0]-lia[1])<abs(lib[0]-lib[1]) else lib

Solution().closestDivisors(123)