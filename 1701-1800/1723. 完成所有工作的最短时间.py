# 给你一个整数数组 jobs ，其中 jobs[i] 是完成第 i 项工作要花费的时间。
#
#  请你将这些工作分配给 k 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 工作时间 是完成分配给他们的所有工作花费时间的总和。请你
# 设计一套最佳的工作分配方案，使工人的 最大工作时间 得以 最小化 。
#
#  返回分配方案中尽可能 最小 的 最大工作时间 。
#
#
#
#  示例 1：
#
#
# 输入：jobs = [3,2,3], k = 3
# 输出：3
# 解释：给每位工人分配一项工作，最大工作时间是 3 。
#
#
#  示例 2：
#
#
# 输入：jobs = [1,2,4,7,8], k = 2
# 输出：11
# 解释：按下述方式分配工作：
# 1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
# 2 号工人：4、7（工作时间 = 4 + 7 = 11）
# 最大工作时间是 11 。
#
#
#
#  提示：
#
#
#  1 <= k <= jobs.length <= 12
#  1 <= jobs[i] <= 107
#
#  Related Topics 递归 回溯算法
#  👍 192 👎 0

from typing import List


# 回溯+二分+剪枝
# 1大的优先分配，2如果一个已经达到limit了但是分配不成功即放弃，3如果一个分配前为0分配i后仍不成功，那么i也不必分配给后面的人了
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)

        def check(limit, ji, w):
            if ji >= n:
                return True
            for wi in range(k):
                if w[wi] + jobs[ji] <= limit:
                    w[wi] += jobs[ji]
                    if check(limit, ji + 1, w):
                        return True
                    w[wi] -= jobs[ji]
                    if w[wi] == 0 or w[wi] + jobs[ji] == limit:
                        break
            return False

        l, r = jobs[0], sum(jobs) + 1
        while l < r:
            mid = (l + r) // 2
            if not check(mid, 0, [0] * k):
                l = mid + 1
            else:
                r = mid
        return l


# 2状态压缩+动态规划
import functools


class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)

        def cal(num):
            ans = 0
            for i in range(n):
                if num & (1 << i):
                    ans += jobs[i]
            return ans

        # def dp(i, j):  # i为使用人数，j为状态
        #     if (i, j) in m:
        #         return m[i, j]
        #     ans = min(max(dp(i - 1, x), m2[j ^ x]) for x in range(j)))
        #     m[i, j] = ans
        #     return ans
        dp = [[0] * (1 << n) for _ in range(k)]
        m2 = [0] * (1 << n)
        for i in range(1 << n):
            m2[i] = cal(i)
        for i in range(1 << n):
            dp[0][i] = m2[i]
        for i in range(1, k):
            for j in range(1, 1 << n):
                dp[i][j] = min(max(dp[i - 1][x], m2[j ^ x]) for x in range(j))
        return dp[-1][(1 << n) - 1]


Solution().minimumTimeRequired([1, 2, 4, 7, 8], 2)
