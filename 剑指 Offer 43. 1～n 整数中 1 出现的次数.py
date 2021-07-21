#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
#
#  例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。
#
#
#
#  示例 1：
#
#
# 输入：n = 12
# 输出：5
#
#
#  示例 2：
#
#
# 输入：n = 13
# 输出：6
#
#
#
#  限制：
#
#
#  1 <= n < 2^31
#
#
#  注意：本题与主站 233 题相同：https://leetcode-cn.com/problems/number-of-digit-one/
#  Related Topics 递归 数学 动态规划
#  👍 203 👎 0

# 数位dp


class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0
        for i in range(len(str(n))):
            a = (n // (10 ** (i + 1))) * (10 ** i)  # 非顶格
            b = min(max(n % (10 ** (i + 1)) - 10 ** i + 1, 0), 10 ** i)  # 顶格
            ans += a + b
        return ans


Solution().countDigitOne(113)
