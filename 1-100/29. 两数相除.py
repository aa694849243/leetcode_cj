'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

 

示例 1:

输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
示例 2:

输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
 

提示：

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。本题中，如果除法结果溢出，则返回 231 − 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#---------------caojie---88%--------------------------------------------------------------------------------------------
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == 0:
            raise ZeroDivisionError
        if dividend == 0:
            return 0
        flag = 1 if (dividend > 0 and divisor > 0) != (dividend < 0 and divisor < 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        j = 0
        while dividend >= divisor:
            i = 1
            temp = divisor
            while dividend >= temp:
                x = temp
                temp += temp
                dx = i
                i += i
            j += dx
            dividend -= x
        j = j if flag >= 0 else -j
        return max(min(j, 2 ** 31 - 1), -2 ** 31)


#-------------------------------移位法-----------------------------------------------------------------------------------
#链接：https://leetcode-cn.com/problems/divide-two-integers/solution/xiao-xue-sheng-du-hui-de-lie-shu-shi-suan-chu-fa-b/
def divide(self, dividend: int, divisor: int) -> int:
    sign = (dividend > 0) ^ (divisor > 0)
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0
    #把除数不断左移，直到它大于被除数
    while dividend >= divisor:
        count += 1
        divisor <<= 1
    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        if divisor <= dividend:
            result += 1 << count #这里的移位运算是把二进制（第count+1位上的1）转换为十进制
            dividend -= divisor
    if sign: result = -result
    return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1






a = -1
b = 1
ret = Solution().divide(a, b)
