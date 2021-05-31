import collections, heapq, itertools
from typing import List


# 你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。
#
#  你有一堆可以焊接在一起的钢筋 rods。举个例子，如果钢筋的长度为 1、2 和 3，则可以将它们焊接在一起形成长度为 6 的支架。
#
#  返回广告牌的最大可能安装高度。如果没法安装广告牌，请返回 0。
#
#
#
#  示例 1：
#
#  输入：[1,2,3,6]
# 输出：6
# 解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。
#
#
#  示例 2：
#
#  输入：[1,2,3,4,5,6]
# 输出：10
# 解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。
#
#  示例 3：
#
#  输入：[1,2]
# 输出：0
# 解释：没法安装广告牌，所以返回 0。
#
#
#
#  提示：
#
#
#  0 <= rods.length <= 20
#  1 <= rods[i] <= 1000
#  钢筋的长度总和最多为 5000
#
#  Related Topics 动态规划
#  👍 86 👎 0

# 动态规划 正向思维
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        m = {}

        def dp(i, score):
            if i == -1:  # 当不用任何一块广告牌时，分数最多为0，其他情况不可能，所以置为-inf
                return float('-inf') if score != 0 else 0
            if (i, score) in m:
                return m[i, score]
            m[i, score] = max(dp(i - 1, score - rods[i]) + rods[i], dp(i - 1, score), dp(i - 1, score + rods[i]))
            return m[i, score]

        return dp(len(rods) - 1, 0)


# 逆向思维
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        m = {}

        def dp(i, score):  # 代表区间[i:]的得分为score的最高的正数长度
            if i == (n := len(rods)):
                return 0 if score == 0 else float('-inf')
            if (i, score) in m:
                return m[i, score]
            # 区间拓展1，那么score+rods[i]-rods[i]==score，此时负数边加了rods[i]，同理score-rods[i]+rods[i]=score，此时正数边加了rods[i]，由于限制长度在负数边，那么限制长度不会改变
            m[i, score] = max(dp(i + 1, score + rods[i]) + rods[i], dp(i + 1, score), dp(i + 1, score - rods[i]))
            return m[i, score]

        return dp(0, 0)


# 3折半查找+区间合并  集合合并
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        def solve(li):
            m = {(0, 0)}
            for x in li:
                m |= ({(a + x, b) for a, b in m} | {(a, b + x) for a, b in m})
            score = {}
            for a, b in m:  # a段为正数长度，限制长度
                score[a - b] = max(score.get(a - b, 0), a)
            return score

        L = solve(rods[:len(rods) // 2])
        R = solve(rods[len(rods) // 2:])
        ans=0
        for l in L:
            if -l in R:
                ans=max(ans,L[l]+R[-l])
        return ans

Solution().tallestBillboard([1, 1])
