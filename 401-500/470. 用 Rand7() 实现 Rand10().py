'''已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。

 

示例 1:

输入: 1
输出: [7]
示例 2:

输入: 2
输出: [8,4]
示例 3:

输入: 3
输出: [8,1,10]
 

提示:

rand7 已定义。
传入参数: n 表示 rand10 的调用次数。
 

进阶:

rand7()调用次数的 期望值 是多少 ?
你能否尽量少调用 rand7() ?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-rand10-using-rand7
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

import random


def rand7():
    return random.randint(1, 7)


# 下述解法是错误的，因为最后算的是总数的概率 而不是简单的//换算
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        ans = 0
        for i in range(10):
            ans += rand7()
        return ans // 7


# 1拒绝采样
# https://leetcode-cn.com/problems/implement-rand10-using-rand7/solution/yong-rand7-shi-xian-rand10-by-leetcode/
class Solution:
    def rand10(self):
        a = rand7()
        b = rand7()
        c = 7 * (b - 1) + a
        if c > 40:
            return self.rand10()
        return c % 10 if c % 10 != 0 else 10


# 2拒绝采样优化版
class Solution:
    def rand10(self):
        row = rand7()
        col = rand7()
        num = (row - 1) * 7 + col
        if num > 40:
            col = rand7()
            row = num % 10
            num = (row - 1) * 7 + col
            if num > 60:
                col = rand7()
                row = num % 10
                num = (row - 1) * 7 + col
                if num > 20:
                    return self.rand10()
                return num % 10 if num % 10 != 0 else 10
            return num % 10 if num % 10 != 0 else 10
        return num % 10 if num % 10 != 0 else 10
