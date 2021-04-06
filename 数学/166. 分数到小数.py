'''
给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。

如果小数部分为循环小数，则将循环的部分括在括号内。

示例 1:

输入: numerator = 1, denominator = 2
输出: "0.5"
示例 2:

输入: numerator = 2, denominator = 1
输出: "2"
示例 3:

输入: numerator = 2, denominator = 3
输出: "0.(6)"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-to-recurring-decimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return
        if numerator == 0:
            return '0'
        if numerator<=-2**31 or numerator>=2**31:
            return
        flag = -1 if (numerator < 0) ^ (denominator < 0) else 1
        b = abs(numerator) // abs(denominator)
        integer = '-'+str(b) + '.' if flag<0 else str(b)+'.'
        ans = ''
        s = {}
        i = 0
        a = abs(numerator) % abs(denominator)
        if a==0:
            return integer[:-1]
        while a not in s or a == 0:
            if a == 0:
                return integer + ans
            else:
                s[a] = i
                a *= 10
                while a // denominator == 0:
                    a *= 10
                    ans += '0'
                    i += 1
                b = a // abs(denominator)
                a= a % abs(denominator)
                ans += str(b)
                i += 1
        m = s[a]
        return integer + ans[:m] + '({})'.format(ans[m:])


a =7
b = -12
Solution().fractionToDecimal(a, b)
