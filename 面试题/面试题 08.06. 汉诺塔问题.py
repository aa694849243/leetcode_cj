#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只
# 能放在更大的盘子上面)。移动圆盘时受到以下限制:
# (1) 每次只能移动一个盘子;
# (2) 盘子只能从柱子顶端滑出移到下一根柱子;
# (3) 盘子只能叠在比它大的盘子上。
#
#  请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。
#
#  你需要原地修改栈。
#
#  示例1:
#
#   输入：A = [2, 1, 0], B = [], C = []
#  输出：C = [2, 1, 0]
#
#
#  示例2:
#
#   输入：A = [1, 0], B = [], C = []
#  输出：C = [1, 0]
#
#
#  提示:
#
#
#  A中盘子的数目不大于14个。
#
#  Related Topics 递归 数组
#  👍 106 👎 0


class Solution:
    def hanota(self, A: List[int], B: List[int], C: List[int]) -> None:
        """
        Do not return anything, modify C in-place instead.
        """

        def rec(n, a, b, c):  # 将n个盘子通过b转移到c
            if n == 1:  # 终止条件，只剩最后一个盘子，将a中最后一个盘子转移到c
                c.append(a.pop())
            else:
                rec(n - 1, a, c, b)  # 将n-1个盘子通过c转移到b
                c.append(a.pop())  # 将最后一个底盘转移到c
                rec(n - 1, b, a, c)  # 将n-1个盘子从b通过a转移到c

        rec(len(A), A, B, C)
