'''
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例:

输入: 13
输出: 6
解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-digit-one
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 数学
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n < 1:
            return 0
        lenth = len(str(n))
        count = 0
        x = 1
        for i in range(lenth):
            x *= 10
            count += (n // x*(x//10) + min(x // 10, max(n % x - x//10 + 1, 0)))
        return count


Solution().countDigitOne(110)
