'''给定一个整数，写一个函数来判断它是否是 3 的幂次方。

示例 1:

输入: 27
输出: true
示例 2:

输入: 0
输出: false
示例 3:

输入: 9
输出: true
示例 4:

输入: 45
输出: false
进阶：
你能不使用循环或者递归来完成本题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 数学
import math
import sys


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False

        a = math.log10(n) / math.log10(3)  # 不能用log2

        return (a + sys.float_info.epsilon) % 1 <= 2 * sys.float_info.epsilon


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3 ** round(math.log(n, 3)) == n


# 整数限制 看题解
# https://leetcode-cn.com/problems/power-of-three/solution/3de-mi-by-leetcode/
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 3 ** 19 % n == 0


Solution().isPowerOfThree(3 ** 18)
