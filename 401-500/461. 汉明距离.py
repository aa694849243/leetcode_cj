'''两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。

给出两个整数 x 和 y，计算它们之间的汉明距离。

注意：
0 ≤ x, y < 231.

示例:

输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1移位
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        while x or y:
            if x & 1 != y & 1:
                ans += 1
            x >>= 1
            y >>= 1

        return ans


# 2异或
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x ^ y).count('1')


# 3布赖恩·克尼根算法
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = x ^ y
        ans = 0
        while a:
            ans += 1
            a = a & (a - 1)
        return ans


Solution().hammingDistance(4, 1)
