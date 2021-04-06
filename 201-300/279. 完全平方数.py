'''
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-squares
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import math


# 动态规划 背包问题
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [math.inf] * (n + 1)
        dp[0] = 0
        suqare_num = [i ** 2 for i in range(1, int(math.sqrt(n)) + 1)]
        for i in range(1, n + 1):
            for j in suqare_num:
                if j > i:
                    break
                dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1]


# 递归 贪心 精妙递归
class Solution:
    def numSquares(self, n: int) -> int:
        square_num = set([i ** 2 for i in range(1, int(math.sqrt(n) + 1))])

        def rec(n, count):
            if count == 1:
                return n in square_num
            for j in square_num:
                if j > n:
                    break
                if rec(n - j, count - 1):
                    return True
            return False

        for i in range(1, n + 1):
            if rec(n, i):
                return i


# 多元树 bfs 宽度优先遍历
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        square_num = [i ** 2 for i in range(1, int(math.sqrt(n) + 1))]
        if n in square_num:
            return 1
        count = 1
        a = [n]
        while True:
            tree = []
            for x in a:
                for i in square_num:
                    if i > x:
                        break
                    if x - i in square_num:
                        return count + 1
                    tree.append(x - i)
            count += 1
            a = tree


# 数学 四平方和 三平方和
class Solution:
    def numSquares(self, n: int) -> int:
        if int(math.sqrt(n))**2==n:
            return 1
        while n & 3 == 0:
            n >>= 2
        if n&7==7:
            return 4
        square_nums=set([i**2 for i in range(1,int(math.sqrt(n)+1))])
        for i in square_nums:
            if n-i in square_nums:
                return 2
        return 3


Solution().numSquares(19)
