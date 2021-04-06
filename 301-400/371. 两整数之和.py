'''不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:

输入: a = 1, b = 2
输出: 3
示例 2:

输入: a = -2, b = 3
输出: 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
import math


# 位操作 64位负数表现形式
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        a &= mask  # 如果为正数，数字不变，如果为负数则映射为无符号整数，如-2在32位中表现为0b11....110,这个值在无符号二进制中为int(0b11...110)
        b &= mask
        while b:
            carry = a & b  #
            a = a ^ b
            b = carry << 1 & mask
        return a if a <= 2 ** 31 - 1 else ~(a ^ mask)  # ~(a^mask)为无符号整数负数的还原操作
 #https://leetcode-cn.com/problems/sum-of-two-integers/solution/python-wei-yun-suan-yi-xie-keng-by-lih/


Solution().getSum(-2, -3)
