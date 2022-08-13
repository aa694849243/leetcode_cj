import functools
import math


# https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments/solution/da-xiao-wei-k-de-bu-zhong-die-xian-duan-de-shu-mu-/
class Solution:
    # 从n个点中选2k，但k个线段存在k-1个公共点，所以总点数为n-k+1
    def numberOfSets(self, n: int, k: int) -> int:
        return math.comb(n + k - 1, 2 * k) % (10 ** 9 + 7)


class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod = 10 ** 9 + 7

        # 初始状态dp(0,0,0)即什么都没有的状态=1，dp(i,0,0)=1，即从任何一个点开始，什么都没有的状态都为1
        @functools.lru_cache(None)
        def dp(i, j, flag):
            if j < 0:  # dp(i,0,0)=1
                return 0
            if i == 0:
                return +(j == 0 and flag == 0)
            if flag == 0:
                return (dp(i - 1, j, 0) + dp(i - 1, j, 1)) % mod
            else:
                return (dp(i - 1, j - 1, 0) + dp(i - 1, j - 1, 1) + dp(i - 1, j, 1)) % mod

        return (dp(n - 1, k, 0) + dp(n - 1, k, 1)) % mod
