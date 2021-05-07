# 我们给出 S，一个源于 {'D', 'I'} 的长度为 n 的字符串 。（这些字母代表 “减少” 和 “增加”。）
# 有效排列 是对整数 {0, 1, ..., n} 的一个排列 P[0], P[1], ..., P[n]，使得对所有的 i：
#
#
#  如果 S[i] == 'D'，那么 P[i] > P[i+1]，以及；
#  如果 S[i] == 'I'，那么 P[i] < P[i+1]。
#
#
#  有多少个有效排列？因为答案可能很大，所以请返回你的答案模 10^9 + 7.
#
#
#
#  示例：
#
#  输入："DID"
# 输出：5
# 解释：
# (0, 1, 2, 3) 的五个有效排列是：
# (1, 0, 3, 2)
# (2, 0, 3, 1)
# (2, 1, 3, 0)
# (3, 0, 2, 1)
# (3, 1, 2, 0)
#
#
#
#
#  提示：
#
#
#  1 <= S.length <= 200
#  S 仅由集合 {'D', 'I'} 中的字符组成。
#
#
#
#  Related Topics 分治算法 动态规划
#  👍 92 👎 0

# 动态规划 k+1求k的动态规划
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        mod = 10 ** 9 + 7
        n = len(S)
        m = {(0, 0): 1}

        def dp(i, j):  # i表示第i个数字，j表示i之前小于第i处数字的个数，最多为i，如果超过那就是无效数字
            if (i, j) in m:
                return m[i, j]
            if not (0 <= j <= i):
                return 0
            ans = 0
            if S[i - 1] == 'D':  # 这种情况说明nums[i-1]>nums[i],小于nums[i]有j个，那么小于nums[i-1]会更多
                # ans = sum(dp(i - 1, k) for k in range(j, i))  # 最少为j，最多为i-1
                # dp(i,j)=dp(i-1,0)+dp(i-1,1)+...+dp(i-1,j-2)+dp(i-1,j-1)
                # dp(i,j-1)=dp(i-1,0)+dp(i-1,1)+...+dp(i-1,j-2)
                ans = dp(i - 1, j) + dp(i, j + 1)  # 化简情况
            elif S[i - 1] == 'I':  # nums[i-1]<nums[i],小于nums[i]有j个，那么小于nums[i-1]最多为j-1
                # ans = sum(dp(i - 1, k) for k in range(j))
                # dp(i,j)=dp(i-1,j)+dp(i-1,j+1)+...+dp(i-1,i-1)
                # dp(i,j+1)=dp(i-1,j+1)+...+dp(i-1,i-1)
                ans = dp(i - 1, j - 1) + dp(i, j - 1)
            ans %= mod
            m[i, j] = ans
            return ans

        return sum(dp(n, j) for j in range(n + 1)) % mod


# 2分治+费马小定理求逆元+动态规划 二项式
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        mod = 10 ** 9 + 7
        fac = [1, 1]
        N = len(S)
        for i in range(2, N + 1):
            fac.append(fac[-1] * i % mod)
        facinv = [pow(f, mod - 2, mod) for f in fac]

        def binom(n, k):
            return fac[n] * facinv[k] % mod * facinv[n - k] % mod

        m = {}

        def dp(i, j):  # i,j为字符串两端点索引
            if i >= j: return 1
            if (i, j) in m:
                return m[i, j]
            ans = 0
            if S[i] == 'I':  # 端点处可以为0
                ans += dp(i + 1, j)
            if S[j] == 'D':
                ans += dp(i, j - 1)
            n = j - i + 2
            for k in range(i + 1, j + 1):  # 0可以放在DI的缝里
                if S[k - 1:k + 1] == 'DI':
                    ans += binom(n - 1, k - i) * dp(i, k - 2) * dp(k + 1, j)  # 因为0的位置已经放好了，所以二项式数量为n-1
                    ans %= mod
            m[i, j] = ans
            return ans
        return dp(0,N-1)
