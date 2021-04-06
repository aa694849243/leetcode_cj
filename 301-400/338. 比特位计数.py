'''给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的 __builtin_popcount）来执行此操作。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 方法1 动态规划 + 最高有效位
# P(x+b)=P(x)+1 b=2^m x<b
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0] * (num + 1)
        b, i = 1, 0
        while b <= num:
            while i < b and i + b <= num:
                ans[i + b] = ans[i] + 1
                i += 1
            i = 0
            b <<= 1
        return ans
# 方法2 动态规划 + 最低有效位
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans=[0]*(num+1)
        for i in range(1,num+1):
            ans[i]=ans[i>>1]+i %2
        return ans
# 方法3 动态规划 最后设置位
# P(x)=P(x & (x-1))+1
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans=[0]*(num+1)
        for i in range(1,num+1):
            ans[i]=ans[(i&(i-1))]+1
        return ans
