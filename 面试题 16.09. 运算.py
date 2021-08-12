#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 请实现整数数字的乘法、减法和除法运算，运算结果均为整数数字，程序中只允许使用加法运算符和逻辑运算符，允许程序中出现正负常数，不允许使用位运算。
#  你的实现应该支持如下操作：
#
#  Operations() 构造函数
#  minus(a, b) 减法，返回a - b
#  multiply(a, b) 乘法，返回a * b
#  divide(a, b) 除法，返回a / b
#
#  示例：
#  Operations operations = new Operations();
# operations.minus(1, 2); //返回-1
# operations.multiply(3, 4); //返回12
# operations.divide(5, -2); //返回-2
#
#  提示：
#
#  你可以假设函数输入一定是有效的，例如不会出现除法分母为0的情况
#  单个用例的函数调用次数不会超过1000次
#
#  Related Topics 设计 数学
#  👍 15 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Operations:

    def __init__(self):
        pass

    def minus(self, a: int, b: int) -> int:
        return a + (~b) + 1

    def abs(self, num):
        if num > 0:
            return num
        return self.minus(0, num)

    def multiply(self, a: int, b: int) -> int:
        @functools.lru_cache(None)
        def rec(a, num):
            if num == 0:
                return 0
            if num == 1:
                return a
            cnt = 1
            s = a
            while cnt + cnt <= num:
                cnt += cnt
                s += s
            ans = s
            ans += rec(a, self.minus(num,cnt))
            return ans

        sign = 1
        if a < 0 and b > 0 or a > 0 and b < 0:
            sign = self.minus(0,1)
        a = self.abs(a)
        b = self.abs(b)
        c = rec(a, b)
        if sign == 1:
            return c
        else:
            return self.minus(0, c)

    def divide(self, a: int, b: int) -> int:
        @functools.lru_cache(None)
        def rec(a, b):
            if a == 0 or a < b:
                return 0
            if b == 1:
                return a
            fac = b
            cnt = 1
            while fac + fac <= a:
                fac += fac
                cnt += cnt
            ans = cnt
            ans += rec(self.minus(a,fac), b)
            return ans
        sign=1
        if a < 0 and b > 0 or a > 0 and b < 0:
            sign = self.minus(0,1)
        a = self.abs(a)
        b = self.abs(b)
        c = rec(a, b)
        if sign == 1:
            return c
        else:
            return self.minus(0, c)
        a = self.abs(a)
        b = self.abs(b)
        c = rec(a, b)
        if sign == 1:
            return c
        else:
            return self.minus(self.minus(0, c),1)


# Your Operations object will be instantiated and called as such:
# obj = Operations()
# param_1 = obj.minus(a,b)
# param_2 = obj.multiply(a,b)
# param_3 = obj.divide(a,b)
# leetcode submit region end(Prohibit modification and deletion)
