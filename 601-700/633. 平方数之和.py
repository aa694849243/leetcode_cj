'''给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。

 

示例 1：

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5
示例 2：

输入：c = 3
输出：false
示例 3：

输入：c = 4
输出：true
示例 4：

输入：c = 2
输出：true
示例 5：

输入：c = 1
输出：true
 

提示：

0 <= c <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-square-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

import math


# 1枚举，两端
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(c ** 0.5)
        while l <= r:
            if l ** 2 + r ** 2 == c:
                return True
            elif l ** 2 + r ** 2 > c:
                r -= 1
            else:
                l += 1
        return False


# 2

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(c ** 0.5)
        for a in range(r + 1):
            b_2 = c - a ** 2
            if b_2 == int(b_2 ** 0.5) ** 2:
                return True
        return False


# 3二分
# 应该先枚举a保证c-a**2>=0，这样避免使用开根号的方式
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        def bis(l, r, target):
            while l < r:
                mid = (l + r) // 2
                if mid ** 2 == target:
                    return True
                elif mid ** 2 < target:
                    l = mid + 1
                else:
                    r = mid
            return False

        r = int(c ** 0.5)
        for a in range(r + 1):
            b_2 = c - a ** 2
            if bis(0, b_2 + 1, b_2):
                return True
        return False


# 4费马平方和定理
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 3:
            return True
        i = 2
        while i ** 2 <= c:
            if c % i == 0:
                count = 0
                while c % i == 0:
                    c //= i
                    count += 1
                if i % 4 == 3 and count % 2 != 0:
                    return False
            i += 1
        return c % 4 != 3


Solution().judgeSquareSum(5726)
