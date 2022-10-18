# n 名运动员参与一场锦标赛，所有运动员站成一排，并根据 最开始的 站位从 1 到 n 编号（运动员 1 是这一排中的第一个运动员，运动员 2 是第二个运动员
# ，依此类推）。
#
#  锦标赛由多个回合组成（从回合 1 开始）。每一回合中，这一排从前往后数的第 i 名运动员需要与从后往前数的第 i 名运动员比拼，获胜者将会进入下一回合。如
# 果当前回合中运动员数目为奇数，那么中间那位运动员将轮空晋级下一回合。
#
#
#  例如，当前回合中，运动员 1, 2, 4, 6, 7 站成一排
#
#
#
#  运动员 1 需要和运动员 7 比拼
#  运动员 2 需要和运动员 6 比拼
#  运动员 4 轮空晋级下一回合
#
#
#
#
#  每回合结束后，获胜者将会基于最开始分配给他们的原始顺序（升序）重新排成一排。
#
#  编号为 firstPlayer 和 secondPlayer 的运动员是本场锦标赛中的最佳运动员。在他们开始比拼之前，完全可以战胜任何其他运动员。而任意两
# 个其他运动员进行比拼时，其中任意一个都有获胜的可能，因此你可以 裁定 谁是这一回合的获胜者。
#
#  给你三个整数 n、firstPlayer 和 secondPlayer 。返回一个由两个值组成的整数数组，分别表示两位最佳运动员在本场锦标赛中比拼的 最早
#  回合数和 最晚 回合数。
#
#
#
#  示例 1：
#
#  输入：n = 11, firstPlayer = 2, secondPlayer = 4
# 输出：[3,4]
# 解释：
# 一种能够产生最早回合数的情景是：
# 回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# 回合 2：2, 3, 4, 5, 6, 11
# 回合 3：2, 3, 4
# 一种能够产生最晚回合数的情景是：
# 回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# 回合 2：1, 2, 3, 4, 5, 6
# 回合 3：1, 2, 4
# 回合 4：2, 4
#
#
#  示例 2：
#
#  输入：n = 5, firstPlayer = 1, secondPlayer = 5
# 输出：[1,1]
# 解释：两名最佳运动员 1 和 5 将会在回合 1 进行比拼。
# 不存在使他们在其他回合进行比拼的可能。
#
#
#
#
#  提示：
#
#
#  2 <= n <= 28
#  1 <= firstPlayer < secondPlayer <= n
#
#
#  Related Topics 记忆化搜索 动态规划 👍 23 👎 0
import functools

# 对称性dp
# https://leetcode.cn/problems/the-earliest-and-latest-rounds-where-players-compete/solution/zui-jia-yun-dong-yuan-de-bi-pin-hui-he-b-lhuo/
# leetcode submit region begin(Prohibit modification and deletion)
# class Solution:
#     def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
#         @functools.lru_cache(None)
#         def dp(n, f, s):
#             if f + s == n + 1:
#                 return (1, 1)
#             if f + s > n + 1:
#                 return dp(n, n + 1 - s, n + 1 - f)
#             mid = (n + 1) // 2
#             earliest, largest = float('inf'), float('-inf')
#             if s <= mid:
#                 # s站中间或者站左边
#                 for i in range(f):
#                     for j in range(s - f):
#                         a, b = dp((n + 1) // 2, i + 1, i + j + 2)
#                         earliest = min(a, earliest)
#                         largest = max(b, largest)
#             else:
#                 s_ = n + 1 - s
#                 m_i_d = n - 2 * s_
#                 for i in range(f):
#                     for j in range(s_ - f):
#                         a, b = dp((n + 1) // 2, i + 1, i + 1 + j + (m_i_d + 1) // 2 + 1)
#                         earliest = min(a, earliest)
#                         largest = max(b, largest)
#             return (earliest + 1, largest + 1)
#
#         if firstPlayer > secondPlayer:
#             firstPlayer, secondPlayer = secondPlayer, firstPlayer
#         earliest, largest = dp(n, firstPlayer, secondPlayer)
#         dp.cache_clear()
#         return [earliest, largest]
from typing import List

# https://leetcode.cn/problems/the-earliest-and-latest-rounds-where-players-compete/solution/zhuang-ya-dfs-by-qin-qi-shu-hua-2-t3z5/
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        firstPlayer -= 1
        secondPlayer -= 1

        @functools.lru_cache(None)
        def f(state):  # 0代表存活
            l, r = 0, n - 1
            res = [float('inf'), float('-inf')]
            m = {state}
            while l < r:
                l_off = (n - 1 - l)
                r_off = (n - 1 - r)
                if state & (1 << l_off) == 0:
                    while state & (1 << r_off) != 0:
                        r -= 1
                        r_off = (n - 1 - r)
                    if l == r:
                        break
                    if l == firstPlayer and r == secondPlayer:
                        return [1, 1]
                    elif l in {firstPlayer, secondPlayer}: #l或r为最佳球员时单向压缩
                        m = {s | (1 << r_off) for s in m}
                    elif r in {secondPlayer, firstPlayer}:
                        m = {s | (1 << l_off) for s in m}
                    else:
                        m = {s | (1 << r_off) for s in m} | {s | (1 << l_off) for s in m}
                    r -= 1
                l += 1
            for k in m: #每个阶段遍历所有可能的情况
                tmp = f(k)
                res[0] = min(res[0], tmp[0] + 1)
                res[1] = max(res[1], tmp[1] + 1)
            return res

        if firstPlayer > secondPlayer:
            firstPlayer, secondPlayer = secondPlayer, firstPlayer
        return f(0)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().earliestAndLatest(4, 1, 2))
