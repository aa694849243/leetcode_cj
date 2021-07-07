# -*- coding: utf-8 -*-
import heapq
from typing import List


# 给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：
#
#
#  你挑选 任意 一块披萨。
#  Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
#  Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
#  重复上述过程直到没有披萨剩下。
#
#
#  每一块披萨的大小按顺时针方向由循环数组 slices 表示。
#
#  请你返回你可以获得的披萨大小总和的最大值。
#
#
#
#  示例 1：
#
#
#
#  输入：slices = [1,2,3,4,5,6]
# 输出：10
# 解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小
# 为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。
#
#
#  示例 2：
#
#
#
#  输入：slices = [8,9,8,6,1,1]
# 输出：16
# 解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。
#
#
#  示例 3：
#
#  输入：slices = [4,1,2,5,8,3,1,9,7]
# 输出：21
#
#
#  示例 4：
#
#  输入：slices = [3,1,2]
# 输出：3
#
#
#
#
#  提示：
#
#
#  1 <= slices.length <= 500
#  slices.length % 3 == 0
#  1 <= slices[i] <= 1000
#
#  Related Topics 贪心 数组 动态规划 堆（优先队列）
#  👍 84 👎 0

# 1动态规划
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        def cal(li):
            n = len(li) + 1
            chose = n // 3
            dp = [[0] * (chose + 1) for _ in range(n)]  # n已经+1了
            for i in range(1, n):
                for j in range(1, chose + 1):
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 2][j - 1] if i - 2 >= 0 else 0) + li[i - 1])
            return dp[-1][-1]

        ans1 = cal(slices[:-1])
        ans2 = cal(slices[1:])
        return max(ans1, ans2)


# 贪心+数组模拟双向链表
# 每次弹出最大的，并将两侧与该值的差值加入堆
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        li = []
        n = len(slices)
        for i, val in enumerate(slices):
            heapq.heappush(li, (-val, i))  # 每次弹出最大的
        valid = [True] * n
        llink = [n - 1 if i == 0 else i - 1 for i in range(n)]
        rlink = [0 if i == n - 1 else i + 1 for i in range(n)]
        ans = 0
        for _ in range(n // 3):
            while True:
                val, pos = heapq.heappop(li)
                val *= -1
                if valid[pos]:
                    ans += val
                    break
            lnode_pos, rnode_pos = llink[pos], rlink[pos]
            n_val = slices[lnode_pos] + slices[rnode_pos] - val
            slices[pos]=n_val
            heapq.heappush(li, (-n_val, pos))
            valid[lnode_pos], valid[rnode_pos] = False, False
            rlink[llink[lnode_pos]]=pos
            llink[rlink[rnode_pos]]=pos
            llink[pos]=llink[lnode_pos]
            rlink[pos]=rlink[rnode_pos]
        return ans

Solution().maxSizeSlices([3,4,4,7,10,5,7,2,2])
