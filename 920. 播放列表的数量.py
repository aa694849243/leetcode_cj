# 你的音乐播放器里有 N 首不同的歌，在旅途中，你的旅伴想要听 L 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：
#
#
#  每首歌至少播放一次。
#  一首歌只有在其他 K 首歌播放完之后才能再次播放。
#
#
#  返回可以满足要求的播放列表的数量。由于答案可能非常大，请返回它模 10^9 + 7 的结果。
#
#
#
#  示例 1：
#
#  输入：N = 3, L = 3, K = 1
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].
#
#
#  示例 2：
#
#  输入：N = 2, L = 3, K = 0
# 输出：6
# 解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]
#
#
#  示例 3：
#
#  输入：N = 2, L = 3, K = 1
# 输出：2
# 解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]
#
#
#
#
#  提示：
#
#
#  0 <= K < N <= L <= 100
#
#  Related Topics 动态规划
#  👍 73 👎 0

# 动态规划
import functools


class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dp(i, j):  # i代表长度，j代表歌曲数量
            if i == 0:
                return +(j == 0)

            ans = dp(i - 1, j - 1) * (N - j + 1)
            ans += dp(i - 1, j) * max((j - K), 0)
            return ans % mod

        return dp(L, N)


# 模拟列表k间隔排列
# 二维dp滚动数组写法
import math


class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        m = {}
        mod = 10 ** 9 + 7

        def dp(i, j):  # maxi=L-N,maxj=N-K+1
            if j <= 2:  # j==2说明N-K+1=2 ,N-K=1,刚好可以满足，如果N=K的话，两个同样的字母最多间隔为K-1，不满足条件
                return 1
            if i == 0: #如果N=L的话说明只有一种排列，没有其他的可以塞了
                return 1
            if (i, j) in m:
                return m[i, j]
            m[i, j] = (j - 1) * dp(i - 1, j) + dp(i, j - 1)
            m[i, j] %= mod
            return m[i, j]

        return math.factorial(N) * dp(L - N, N - K + 1) % mod


#
#3滚动数组dp
class Solution:
    def numMusicPlaylists(self, N: int, L: int, K: int) -> int:
        mod = 10 ** 9 + 7
        dp=[1]*(L-N+1)
        for j in range(2,N-K+1):
            for i in range(1,L-N+1):
                dp[i]=j*dp[i-1]+dp[i]
                dp[i]%=mod
        return dp[-1]*math.factorial(N)%mod


#
# class Solution(object):
#     def numMusicPlaylists(self, N, L, K):
#         # dp[S] at time P = <S, P> as discussed in article
#         dp = [1] * (L - N + 1)
#         for p in range(2, N - K + 1):
#             for i in range(1, L - N + 1):
#                 dp[i] += dp[i - 1] * p
#
#         # Multiply by N!
#         ans = dp[-1]
#         for k in range(2, N + 1):
#             ans *= k
#         return ans % (10 ** 9 + 7)


Solution().numMusicPlaylists(2, 4, 0)
