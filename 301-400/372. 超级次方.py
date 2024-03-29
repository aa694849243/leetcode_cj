'''你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。

示例 1:

输入: a = 2, b = [3]
输出: 8
示例 2:

输入: a = 2, b = [1,0]
输出: 1024

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-pow
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    base=1337

    def mypow(self,a, k):
        if k==0:
            return 1
        if k == 1:
            return a % self.base
        a %= self.base
        if k % 2 == 0:
            return self.mypow(a, k / 2) ** 2 % self.base
        else:
            return (a * self.mypow(a, (k - 1) / 2) ** 2) % self.base

    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        tmp=b.pop()
        part1=self.mypow(a,tmp)
        part2=self.mypow(self.superPow(a,b),10)
        return (part1 % self.base)*(part2 % self.base) %self.base


Solution().superPow(2, [1,0])
