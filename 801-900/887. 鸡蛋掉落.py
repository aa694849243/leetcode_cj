# 给你 k 枚相同的鸡蛋，并可以使用一栋从第 1 层到第 n 层共有 n 层楼的建筑。
#
#  已知存在楼层 f ，满足 0 <= f <= n ，任何从 高于 f 的楼层落下的鸡蛋都会碎，从 f 楼层或比它低的楼层落下的鸡蛋都不会破。
#
#  每次操作，你可以取一枚没有碎的鸡蛋并把它从任一楼层 x 扔下（满足 1 <= x <= n）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎
# ，则可以在之后的操作中 重复使用 这枚鸡蛋。
#
#  请你计算并返回要确定 f 确切的值 的 最小操作次数 是多少？
#
#
#  示例 1：
#
#
# 输入：k = 1, n = 2
# 输出：2
# 解释：
# 鸡蛋从 1 楼掉落。如果它碎了，肯定能得出 f = 0 。
# 否则，鸡蛋从 2 楼掉落。如果它碎了，肯定能得出 f = 1 。
# 如果它没碎，那么肯定能得出 f = 2 。
# 因此，在最坏的情况下我们需要移动 2 次以确定 f 是多少。
#
#
#  示例 2：
#
#
# 输入：k = 2, n = 6
# 输出：3
#
#
#  示例 3：
#
#
# 输入：k = 3, n = 14
# 输出：4
#
#
#
#
#  提示：
#
#
#  1 <= k <= 100
#  1 <= n <= 104
#
#  Related Topics 数学 二分查找 动态规划
#  👍 617 👎 0

# 二分+动态规划
import collections


class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        m = {}

        def dp(k, n):
            if k == 0 or n == 0:
                return 0
            elif k == 1:
                return n
            if (k, n) in m:
                return m[k, n]
            l, r = 1, n + 1
            while l < r:
                mid = (l + r) // 2
                f1 = dp(k - 1, mid - 1)
                f2 = dp(k, n - mid)
                if f1 < f2:
                    l = mid + 1
                else:
                    r = mid
            a = dp(k - 1, l - 1)
            b = dp(k, n - l)
            if a == b:  # l代表第一个f1>=f2的x值，如果是相等的那么l可能处于左端点，就不能去取n-1的数了
                ans = 1 + a
            elif a > b:
                ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (l, l - 1))
            m[k, n] = ans
            return ans

        return dp(k, n)


# 2 决策单调性

class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = list(range(n + 1))  # dp 代表k-1，x
        dp2 = [0] * (n + 1)  # dp2 代表k，x, 第一次可以都初始化为0 或与dp相同 因为第一次遍历到都是取max(dp,dp2)结果是一样的
        for k in range(2, k + 1):
            x = 1  # 固定k之后，随着m增大，最佳决策点只能不断右移
            for m in range(1, n + 1):
                while x < m and max(dp[x - 1], dp2[m - x]) >= max(dp[x], dp2[m - x - 1]):  # 找波谷点
                    x += 1
                dp2[m] = 1 + max(dp[x - 1], dp2[m - x])
            dp = dp2[:]
        return dp[-1]


# 3逆向思维
# 考虑f(t,k) 操作t次，k枚鸡蛋最高可以检测到多少层
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        f = [[0] * (k + 1) for _ in range(n + 1)]  # t不会大于n
        for i in range(k + 1):
            f[1][i] = 1
        if k == 1:
            return n
        elif n == 1:
            return 1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                if j == 1:
                    f[i][j] = i
                else:
                    f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
                if f[i][j] >= n:
                    return i


Solution().superEggDrop(k=1, n=1)
