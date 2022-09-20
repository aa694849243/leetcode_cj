'''有 n 个城市通过 m 个航班连接。每个航班都从城市 u 开始，以价格 w 抵达 v。

现在给定所有的城市和航班，以及出发城市 src 和目的地 dst，你的任务是找到从 src 到 dst 最多经过 k 站中转的最便宜的价格。 如果没有这样的路线，则输出 -1。

 

示例 1：

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200
解释:
城市航班图如下


从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。
示例 2：

输入:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500
解释:
城市航班图如下


从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。
 

提示：

n 范围是 [1, 100]，城市标签从 0 到 n - 1
航班数量范围是 [0, n * (n - 1) / 2]
每个航班的格式 (src, dst, price)
每个航班的价格范围是 [1, 10000]
k 范围是 [0, n - 1]
航班没有重复，且不存在自环

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cheapest-flights-within-k-stops
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections
import heapq


# 1 dijsktra
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        m = collections.defaultdict(list)
        for sr, ds, w in flights:
            m[sr].append((ds, w))
        q = [(0, 0, src, src)]
        while q:
            w, time, vi, vj = heapq.heappop(q)
            if time > K + 1:
                continue
            if vj == dst:
                return w
            for u, w_ in m[vj]:
                heapq.heappush(q, (w + w_, time + 1, vj, u))
        return -1


# 2bellman-ford 最短路径 spfa为优化版
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        distance = [[float('inf')] * (K + 2) for _ in range(n)]  # distance行表示点，列表示松弛次数，值代表最短距离
        for i in range(K + 2):
            distance[src][i] = 0  # 原点不管松弛几次距离本身都是0
        times = 1  # 松弛次数

        def relax(vi, vj, w, times):
            if distance[vj][times] > distance[vi][times - 1] + w:
                distance[vj][times] = distance[vi][times - 1] + w

        while times < K + 2:  # 我们这里把直连一个点设置为松弛1次，绕过一个点算松弛2次，绕过两个点算松弛3次，以此类推，可以绕过K个点，那么可以松弛K+1次
            for vi, vj, w in flights:
                if distance[vi][times - 1] != None:
                    relax(vi, vj, w, times)
            times += 1
        return distance[dst][K + 1] if distance[dst][K + 1] != float('inf') else -1


Solution().findCheapestPrice(4, [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]], 0, 3, 1)
