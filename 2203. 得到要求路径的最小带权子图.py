# -*- coding: utf-8 -*-
# 给你一个整数 n ，它表示一个 带权有向 图的节点数，节点编号为 0 到 n - 1 。
#
#  同时给你一个二维整数数组 edges ，其中 edges[i] = [fromi, toi, weighti] ，表示从 fromi 到 toi 有一条边
# 权为 weighti 的 有向 边。
#
#  最后，给你三个 互不相同 的整数 src1 ，src2 和 dest ，表示图中三个不同的点。
#
#  请你从图中选出一个 边权和最小 的子图，使得从 src1 和 src2 出发，在这个子图中，都 可以 到达 dest 。如果这样的子图不存在，请返回 -1
#  。
#
#  子图 中的点和边都应该属于原图的一部分。子图的边权和定义为它所包含的所有边的权值之和。
#
#
#
#  示例 1：
#
#
#
#
# 输入：n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,
# 4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
# 输出：9
# 解释：
# 上图为输入的图。
# 蓝色边为最优子图之一。
# 注意，子图 [[1,0,3],[0,5,6]] 也能得到最优解，但无法在满足所有限制的前提下，得到更优解。
#
#
#  示例 2：
#
#
#
#
# 输入：n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
# 输出：-1
# 解释：
# 上图为输入的图。
# 可以看到，不存在从节点 1 到节点 2 的路径，所以不存在任何子图满足所有限制。
#
#
#
#
#  提示：
#
#
#  3 <= n <= 10⁵
#  0 <= edges.length <= 10⁵
#  edges[i].length == 3
#  0 <= fromi, toi, src1, src2, dest <= n - 1
#  fromi != toi
#  src1 ，src2 和 dest 两两不同。
#  1 <= weight[i] <= 10⁵
#
#
#  Related Topics 图 最短路
#  👍 45 👎 0
import collections
from typing import List
import heapq
import collections


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        set_edges = collections.defaultdict(lambda: float('inf'))
        for i, j, k in edges:
            set_edges[i, j] = min(set_edges[i, j], k)
        m = collections.defaultdict(list)
        rev_m = collections.defaultdict(list)
        for (i, j) in set_edges:
            m[i].append([j, set_edges[i, j]])
            rev_m[j].append([i, set_edges[i, j]])

        def dijkstra(src, m):
            heap = [(0, src)]
            dist = [float('inf')] * n
            while heap:
                d, i = heapq.heappop(heap)
                if dist[i] < d:
                    continue
                dist[i] = d
                for j, k in m[i]:
                    heapq.heappush(heap, (d + k, j))
            return dist

        dist_sr1 = dijkstra(src1, m)
        dist_sr2 = dijkstra(src2, m)
        dist_m = dijkstra(dest, rev_m)
        ans = dist_sr1[dest] + dist_sr2[dest]
        for i in range(n):
            if dist_sr1[i] + dist_sr2[i] + dist_m[i] < ans:
                ans = dist_sr1[i] + dist_sr2[i] + dist_m[i]
        return ans if ans < float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimumWeight(6, [[0, 2, 10], [0, 4, 2], [1, 4, 2], [1, 3, 10], [3, 5, 10], [4, 5, 20], [2, 5, 10]], 0, 1, 5))
