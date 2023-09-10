# -*- coding: utf-8 -*-
# 现有一个含 n 个顶点的 双向 图，每个顶点按从 0 到 n - 1 标记。图中的边由二维整数数组 edges 表示，其中 edges[i] = [ui,
# vi] 表示顶点 ui 和 vi 之间存在一条边。每对顶点最多通过一条边连接，并且不存在与自身相连的顶点。
#
#  返回图中 最短 环的长度。如果不存在环，则返回 -1 。
#
#  环 是指以同一节点开始和结束，并且路径中的每条边仅使用一次。
#
#
#
#  示例 1：
#  输入：n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
# 输出：3
# 解释：长度最小的循环是：0 -> 1 -> 2 -> 0
#
#
#  示例 2：
#  输入：n = 4, edges = [[0,1],[0,2]]
# 输出：-1
# 解释：图中不存在循环
#
#
#
#
#  提示：
#
#
#  2 <= n <= 1000
#  1 <= edges.length <= 1000
#  edges[i].length == 2
#  0 <= ui, vi < n
#  ui != vi
#  不存在重复的边
#
#
#  Related Topics 广度优先搜索 图
#  👍 15 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = float('inf')
        for st in range(n):
            flag = False
            dis = [0] * n
            q = [(-1, st)]
            while 1:
                nxt_q = []
                for fa, u in q:
                    for nxt in g[u]:
                        if nxt != fa:
                            if dis[nxt]:
                                ans = min(ans, dis[u] + dis[nxt] + 1)
                            else:
                                dis[nxt] = dis[u] + 1
                                nxt_q.append((u, nxt))
                if not nxt_q:
                    break
                q = nxt_q
        return ans if ans!=float('inf') else -1


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findShortestCycle(
        6,
        [[4, 2], [5, 1], [5, 0], [0, 3], [5, 2], [1, 4], [1, 3], [3, 4]]    )
)
