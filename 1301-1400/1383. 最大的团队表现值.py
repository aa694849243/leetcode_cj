# -*- coding: utf-8 -*-
import heapq
from typing import List


# 公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i] 分
# 别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的 最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。
#
#  团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。
#
#
#
#  示例 1：
#
#  输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
# 输出：60
# 解释：
# 我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 per
# formance = (10 + 5) * min(4, 7) = 60 。
#
#
#  示例 2：
#
#  输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
# 输出：68
# 解释：
# 此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance =
# (2 + 10 + 5) * min(5, 4, 7) = 68 。
#
#
#  示例 3：
#
#  输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
# 输出：72
#
#
#
#
#  提示：
#
#
#  1 <= n <= 10^5
#  speed.length == n
#  efficiency.length == n
#  1 <= speed[i] <= 10^5
#  1 <= efficiency[i] <= 10^8
#  1 <= k <= n
#
#  Related Topics 贪心 数组 排序 堆（优先队列）
#  👍 86 👎 0


class Solution:
    class staff:
        def __init__(self, s, e):
            self.s = s
            self.e = e

        def __lt__(self, other):
            return self.s < other.s

    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        li = []
        for i in range(n):
            li.append(Solution.staff(speed[i], efficiency[i]))
        li.sort(key=lambda x: -x.e)  # 根据效率逆序排序
        h = []
        total = 0
        ans = 0
        for v in li:
            e, totals = v.e, total + v.s  # 每次拿出的都是当前最低的e
            ans = max(ans, e * totals)
            total+=v.s
            heapq.heappush(h,v) #堆为根据速度排序的小顶堆
            if len(h)==k:#堆里面的节点等于k了，则删掉一个最小速度的
                node=heapq.heappop(h)
                total-=node.s
        return ans % mod


Solution().maxPerformance(3, [2, 8, 2], [2, 7, 1], 2)
