'''给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：

输入：16
输出：True
示例 2：

输入：14
输出：False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 二分法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2+1
        while left < right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid
        return False
Solution().isPerfectSquare(81*81)

# 牛顿迭代法
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        x = num // 2
        while x * x >= num:
            if x * x == num:
                return True
            x = ((x * x) + num) // (2 * x)
        return False