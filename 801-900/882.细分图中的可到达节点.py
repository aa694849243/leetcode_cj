# 给你一个无向图（原始图），图中有 n 个节点，编号从 0 到 n - 1 。你决定将图中的每条边细分为一条节点链，每条边之间的新节点数各不相同。
#
#  图用由边组成的二维数组 edges 表示，其中 edges[i] = [ui, vi, cnti] 表示原始图中节点 ui 和 vi 之间存在一条边，cn
# ti 是将边细分后的新节点总数。注意，cnti == 0 表示边不可细分。
#
#  要细分边 [ui, vi] ，需要将其替换为 (cnti + 1) 条新边，和 cnti 个新节点。新节点为 x1, x2, ..., xcnti ，新边
# 为 [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi] 。
#
#  现在得到一个新的 细分图 ，请你计算从节点 0 出发，可以到达多少个节点？节点 是否可以到达的判断条件 为：如果节点间距离是 maxMoves 或更少，则
# 视为可以到达；否则，不可到达。
#
#  给你原始图和 maxMoves ，返回新的细分图中从节点 0 出发 可到达的节点数 。
#
#
#
#  示例 1：
#
#
# 输入：edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
# 输出：13
# 解释：边的细分情况如上图所示。
# 可以到达的节点已经用黄色标注出来。
#
#
#  示例 2：
#
#
# 输入：edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
# 输出：23
#
#
#  示例 3：
#
#
# 输入：edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
# 输出：1
# 解释：节点 0 与图的其余部分没有连通，所以只有节点 0 可以到达。
#
#
#
#
#  提示：
#
#
#  0 <= edges.length <= min(n * (n - 1) / 2, 104)
#  edges[i].length == 3
#  0 <= ui < vi < n
#  图中 不存在平行边
#  0 <= cnti <= 104
#  0 <= maxMoves <= 109
#  1 <= n <= 3000
#
#  Related Topics 堆 广度优先搜索
#  👍 32 👎 0

# dijsktra 边的利用效率
import collections
import heapq

from typing import List


class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        pq = []
        graph = collections.defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w
        heapq.heappush(pq, (0, 0))
        dist = [float('inf')] * n
        dist[0] = 0
        used = {}
        ans = 0
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            ans += 1
            for nei, weight in graph[node].items():
                v = min(weight, maxMoves - d)  # 每条边的利用效能
                used[node, nei] = v
                d2 = d + weight + 1
                if d2 < min(dist[nei], maxMoves + 1):
                    dist[nei]=d2
                    heapq.heappush(pq, (d2, nei))
        a = sum(min(used.get((u, v), 0) + used.get((v, u), 0), w) for u, v, w in edges)
        return ans + a


Solution().reachableNodes([[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4)