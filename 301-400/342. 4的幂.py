'''给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:

输入: 16
输出: true
示例 2:

输入: 5
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-four
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
import math


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        return 4 ** round(math.log(num, 4)) == num


import sys


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        a = math.log10(num) / math.log10(4)
        return (a + sys.float_info.epsilon) % 1 <= 2 * sys.float_info.epsilon


# 位操作  位运算
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num & int('10' * 16, 2) == 0


# 位操作 数学 位运算
# 指数取模 蒙哥马利算法 https://blog.csdn.net/treasure_wang/article/details/84707869

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and num & (num - 1) == 0 and num % 3 == 1


Solution().isPowerOfFour(4 ** 9)
