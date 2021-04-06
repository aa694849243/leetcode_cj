'''
给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。

示例 1: 

输入: [5,7]
输出: 4
示例 2:

输入: [0,1]
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bitwise-and-of-numbers-range
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 位操作 公共前缀
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        count = 0
        while m != n:
            m = m >> 1
            n = n >> 1
            count += 1
        m = m << count
        return m


# Brian Kernighan 算法 公共前缀

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while n > m:
            n &= (n - 1)
        return n&m


m = 5
n = 10000
Solution().rangeBitwiseAnd(m, n)
