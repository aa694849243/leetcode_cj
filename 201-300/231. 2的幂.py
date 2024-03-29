'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:

输入: 1
输出: true
解释: 20 = 1
示例 2:

输入: 16
输出: true
解释: 24 = 16
示例 3:

输入: 218
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<1:
            return False
        x = 1
        while x < n:
            x <<= 1
        if x==n:
            return True
        else:
            return False


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        x = 1
        while x < n:
            x <<= 1
        if x == n:
            return True
        else:
            return False
class Solution(object):
    def isPowerOfTwo(self, n):
        if n == 0:
            return False
        return n & (-n) == n

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/power-of-two/solution/2de-mi-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
Solution().isPowerOfTwo(1)
