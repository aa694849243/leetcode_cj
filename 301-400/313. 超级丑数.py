'''编写一段程序来查找第 n 个超级丑数。

超级丑数是指其所有质因数都是长度为 k 的质数列表 primes 中的正整数。

示例:

输入: n = 12, primes = [2,7,13,19]
输出: 32
解释: 给定长度为 4 的质数列表 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
说明:

1 是任何给定 primes 的超级丑数。
 给定 primes 中的数字以升序排列。
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000 。
第 n 个超级丑数确保在 32 位有符整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

# 堆
import heapq


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        s = {1, }
        h = [1]
        heapq.heapify(h)
        count = 0
        ans = []
        while count < n:
            x = heapq.heappop(h)
            for i in primes:
                if i * x not in s:
                    s |= {i * x}
                    heapq.heappush(h, i * x)
            ans.append(x)
            count += 1
        return ans[-1]


# 动态规划 多指针 列表指针
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        lpointer = [0] * len(primes)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            m = min([dp[lpointer[k]] * primes[k] for k in range(len(primes))])
            dp[i] = m
            for k in range(len(primes)):
                if dp[lpointer[k]] * primes[k] == m:
                    lpointer[k] += 1

        return dp[-1]


n = 12;
primes = [2, 7, 13, 19]
Solution().nthSuperUglyNumber(n, primes)
