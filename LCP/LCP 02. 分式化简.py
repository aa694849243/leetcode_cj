# -*- coding: utf-8 -*-
from typing import List


# 有一个同学在学习分式。他需要将一个连分数化成最简分数，你能帮助他吗？
#
#
#
#  连分数是形如上图的分式。在本题中，所有系数都是大于等于0的整数。
#
#
#
#  输入的cont代表连分数的系数（cont[0]代表上图的a0，以此类推）。返回一个长度为2的数组[n, m]，使得连分数的值等于n / m，且n, m最大
# 公约数为1。
#
#
#
#  示例 1：
#
#
# 输入：cont = [3, 2, 0, 2]
# 输出：[13, 4]
# 解释：原连分数等价于3 + (1 / (2 + (1 / (0 + 1 / 2))))。注意[26, 8], [-13, -4]都不是正确答案。
#
#  示例 2：
#
#
# 输入：cont = [0, 0, 3]
# 输出：[3, 1]
# 解释：如果答案是整数，令分母为1即可。
#
#
#
#  限制：
#
#
#  cont[i] >= 0
#  1 <= cont的长度 <= 10
#  cont最后一个元素不等于0
#  答案的n, m的取值都能被32位int整型存下（即不超过2 ^ 31 - 1）。
#
#  Related Topics 数组 数学 数论 模拟
#  👍 72 👎 0


class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        def rec(li):
            if len(li) == 1:
                return [li[0], 1]
            a = li[0]
            b = rec(li[1:])
            u, d = b[::-1]
            f = gcd(a * d + u, d)
            nu,nd=(a*d+u)//f,d//f
            return [nu,nd]
        return rec(cont)
