#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给定一个整数，打印该整数的英文描述。
#
#  示例 1:
#
#
# 输入: 123
# 输出: "One Hundred Twenty Three"
#
#
#  示例 2:
#
#
# 输入: 12345
# 输出: "Twelve Thousand Three Hundred Forty Five"
#
#  示例 3:
#
#
# 输入: 1234567
# 输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#  示例 4:
#
#
# 输入: 1234567891
# 输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thou
# sand Eight Hundred Ninety One"
#
#  注意：本题与 273 题相同：https://leetcode-cn.com/problems/integer-to-english-words/
#  Related Topics 递归 数学 字符串
#  👍 16 👎 0


class Solution:
    def numberToWords(self, num: int) -> str:
        def one(num):
            m = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
            return m[num] if num > 0 else ''

        def lt_20(num):
            m = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
                 19: 'Nineteen'}
            return m[num]

        def gt_20(num):
            m = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
            a, rest = divmod(num, 10)
            s=one(rest)
            return m[a*10] + ' ' + s if s else m[a*10]

        def hd(num):
            a, rest = divmod(num, 100)
            f, s = '', ''
            f += one(a) + ' Hundred'
            if rest < 10:
                s += one(rest)
            elif 10 <= rest < 20:
                s += lt_20(rest)
            else:
                s += gt_20(rest)
            return f + ' ' + s if s else f

        def cal(num):
            if num < 10:
                return one(num)
            elif 10 <= num < 20:
                return lt_20(num)
            elif 20 <= num < 100:
                return gt_20(num)
            else:
                return hd(num)

        if num == 0:
            return 'Zero'
        billion = num // (10 ** 9)
        million = (num-billion*10**9) // (10 ** 6)
        thousand = (num-billion*10**9-million*10**6) // 1000
        rest = num % 1000
        ans = ''
        if billion > 0:
            ans += cal(billion) + ' Billion '
        if million > 0:
            ans += cal(million) + ' Million '
        if thousand > 0:
            ans += cal(thousand) + ' Thousand '
        if rest > 0:
            ans += cal(rest)
        return ans.rstrip()
Solution().numberToWords(50868)