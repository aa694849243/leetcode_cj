'''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/powx-n
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

#---------指数收敛---------------------------------------
#caojie--49%-------------------------------
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1
        flag = 1 if x > 0 or n % 2 == 0 else -1
        sign = 1 if n > 0 else 0
        n = abs(n)
        x = abs(x)
        atom = x
        ans = atom
        while n > 1:
            i = 1
            while i < n:
                ans *= atom
                n -= i
                atom *= atom
                i *= 2
            else:
                atom = x
        return flag * ans if sign else 1 / ans
#官方，快速幂+迭代，巧妙
# https://leetcode-cn.com/problems/powx-n/solution/powx-n-by-leetcode-solution/


x = -2
n = 2
Solution().myPow(x, n)
