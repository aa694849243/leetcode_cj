#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
#
#
#  例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。
#
#
#
#  示例 1：
#
#
# 输入: n = 5, m = 3
# 输出: 3
#
#
#  示例 2：
#
#
# 输入: n = 10, m = 17
# 输出: 2
#
#
#
#
#  限制：
#
#
#  1 <= n <= 10^5
#  1 <= m <= 10^6
#
#  Related Topics 递归 数学
#  👍 405 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        def f(n, m):
            if n == 1: return 0
            return (f(n - 1, m) + m) % n

        return f(n, m)


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            ans = (ans + m) % i #初始为0，一切数%1都为0
        return ans
