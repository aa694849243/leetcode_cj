'''有 n 个网络节点，标记为 1 到 n。

给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点，vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

 

示例 1：



输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
示例 2：

输入：times = [[1,2,1]], n = 2, k = 1
输出：1
示例 3：

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1
 

提示：

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/network-delay-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections
import heapq


# 题目可以转换为求单源节点到其他节点最短路径，再找到最长那一根，那么可以使用经典的Dijkstra算法
# 首先制作边表，再准备一个候选堆，堆里面存储元组，元组的第一个元素储存源节点到目标节点的最短路径长度
# 每次从候选堆里面弹出一个节点，该节点的长度一定是最小的，我们访问它，并将该节点的邻接节点入堆，直到所有点都访问完毕或者候选堆里面没有元素可以访问了
#
# 作者：tooooo_the_moon
# 链接：https://leetcode-cn.com/problems/network-delay-time/solution/dijkstrasuan-fa-by-tooooo_the_moon-m55l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 1最小生成树 Dijstra 迪杰斯特拉 时间复杂度O(E*logV)
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        out_edges = collections.defaultdict(list)

        for vi, vj, w in times:
            out_edges[vi].append((vj, w))  # 制作边表
        cand = [(0, k, k)]  # 利用堆做一个候选边的优先队列,首先将根节点入堆
        mst = [None] * n  # 最小生成树表
        cnt = 0
        ans = 0
        while cnt < n and cand:
            w, vi, vj = heapq.heappop(cand)
            if mst[vj - 1]:  # 如果邻接点已经访问过则不再考虑
                continue
            mst[vj - 1] = ((vi, vj), w)
            ans = max(ans, w)
            cnt += 1
            for u, w_ in out_edges[vj]:
                if not mst[u - 1]:
                    heapq.heappush(cand, (w_ + w, vj, u))
        return ans if cnt == n else -1


# 2DFS
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = {node: float('inf') for node in range(1, n + 1)}
        out_edges = collections.defaultdict(list)
        for vi, vj, w in times:
            out_edges[vi].append((vj, w))  # 制作边表

        def dfs(vi, elapsed):
            if elapsed >= dist[vi]:
                return
            dist[vi] = elapsed
            for vj, w in out_edges[vi]:
                dfs(vj, w + elapsed)

        dfs(k, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1


Solution().networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1)
