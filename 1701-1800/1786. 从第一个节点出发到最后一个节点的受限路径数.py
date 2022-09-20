# 现有一个加权无向连通图。给你一个正整数 n ，表示图中有 n 个节点，并按从 1 到 n 给节点编号；另给你一个数组 edges ，其中每个 edges[
# i] = [ui, vi, weighti] 表示存在一条位于节点 ui 和 vi 之间的边，这条边的权重为 weighti 。
#
#  从节点 start 出发到节点 end 的路径是一个形如 [z0, z1, z2, ..., zk] 的节点序列，满足 z0 = start 、zk =
# end 且在所有符合 0 <= i <= k-1 的节点 zi 和 zi+1 之间存在一条边。
#
#  路径的距离定义为这条路径上所有边的权重总和。用 distanceToLastNode(x) 表示节点 n 和 x 之间路径的最短距离。受限路径 为满足
# distanceToLastNode(zi) > distanceToLastNode(zi+1) 的一条路径，其中 0 <= i <= k-1 。
#
#  返回从节点 1 出发到节点 n 的 受限路径数 。由于数字可能很大，请返回对 10⁹ + 7 取余 的结果。
#
#
#
#  示例 1：
#
#
# 输入：n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
# 输出：3
# 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。三条受限路径分别是：
# 1) 1 --> 2 --> 5
# 2) 1 --> 2 --> 3 --> 5
# 3) 1 --> 3 --> 5
#
#
#  示例 2：
#
#
# 输入：n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,
# 6,4]]
# 输出：1
# 解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。唯一一条受限路径是：1 --> 3 --> 7 。
#
#
#
#  提示：
#
#
#  1 <= n <= 2 * 10⁴
#  n - 1 <= edges.length <= 4 * 10⁴
#  edges[i].length == 3
#  1 <= ui, vi <= n
#  ui != vi
#  1 <= weighti <= 10⁵
#  任意两个节点之间至多存在一条边
#  任意两个节点之间至少存在一条路径
#
#
#  Related Topics 图 拓扑排序 动态规划 最短路 堆（优先队列） 👍 78 👎 0
import collections
import heapq

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for u, v, w in edges:
            g[u - 1].append((v - 1, w))
            g[v - 1].append((u - 1, w))
        dists = [float('inf')] * n
        q = [(0, n - 1)]
        mod = 10 ** 9 + 7
        cnt = [0] * n
        cnt[-1] = 1
        dists[-1] = 0 # 从终点开始，终点的距离为0
        while q:
            cur_dist, cur = heapq.heappop(q)
            if dists[cur] < cur_dist:
                continue
            for nxt, w in g[cur]:
                if dists[nxt] > cur_dist + w:
                    dists[nxt] = cur_dist + w
                    heapq.heappush(q, (cur_dist + w, nxt))
                if dists[nxt] > dists[cur]:
                    cnt[nxt] += cnt[cur]
                    cnt[nxt] %= mod
        return cnt[0]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countRestrictedPaths(5, [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))
# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-08-28 1:20 
# ide： PyCharm
