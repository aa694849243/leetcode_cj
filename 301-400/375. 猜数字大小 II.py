'''我们正在玩一个猜数游戏，游戏规则如下：

我从 1 到 n 之间选择一个数字，你来猜我选了哪个数字。

每次你猜错了，我都会告诉你，我选的数字比你的大了或者小了。

然而，当你猜了数字 x 并且猜错了的时候，你需要支付金额为 x 的现金。直到你猜到我选的数字，你才算赢得了这个游戏。

示例:

n = 10, 我选择了8.

第一轮: 你猜我选择的数字是5，我会告诉你，我的数字更大一些，然后你需要支付5块。
第二轮: 你猜是7，我告诉你，我的数字更大一些，你支付7块。
第三轮: 你猜是9，我告诉你，我的数字更小一些，你支付9块。

游戏结束。8 就是我选的数字。

你最终要支付 5 + 7 + 9 = 21 块钱。
给定 n ≥ 1，计算你至少需要拥有多少现金才能确保你能赢得这个游戏。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 这里的最优策略指的是考虑到所有策略都会遇到最坏结果，但有一个策略的最坏结果好于其他所有策略的最坏结果
# 1 极大极小化 极小极大化 递归
import functools


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(maxsize=None)
        def rec(i, j):
            if i >= j:
                return 0
            m = float('inf')
            for n in range((i + j) // 2, j + 1):  # 从（i+j）//2开始总体开销会更小
                m = min(m, n + max(rec(i, n - 1), rec(n + 1, j)))  # 从range((i + j) // 2, j + 1)范围取数，计算每种情况最大开销，最终选择其中的最小值
            return m

        return rec(1, n)


# 2 动态规划 复杂列表推导式
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * n for _ in range(n)]  # 对角线元素初始化为0
        for k in range(1, n):  # k代表i,j间隔
            for i in range(n - k):
                j = i + k  # 间隔逐渐扩大
                dp[i][j] = min(pivot + 1 + max(dp[i][pivot - 1] if pivot - 1 > i else 0, dp[pivot + 1][j] if pivot + 1 < j else 0) for pivot in range((i + j) // 2, j + 1))

        return dp[0][n - 1]


Solution().getMoneyAmount(5)
