'''
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。

注意:
n 是正数且在32位整数范围内 ( n < 231)。

示例 1:

输入:
3

输出:
3
示例 2:

输入:
11

输出:
0

说明:
第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。'''


class Solution:
    def findNthDigit(self, n: int) -> int:
        for digits in range(1, 11):
            if n < 9 * digits * 10 ** (digits - 1):
                break
            n -= 9 * digits * 10 ** (digits - 1)
        firstnum = 10 ** (digits - 1) + (n-1) // digits
        return int(str(firstnum)[(n-1) % digits]) if n!=0 else 9 #如果n==0刚好进位前最后一个数最后1位，即为9


Solution().findNthDigit(189)
