# 给你一个数组 routes ，表示一系列公交线路，其中每个 routes[i] 表示一条公交线路，第 i 辆公交车将会在上面循环行驶。
#
#
#  例如，路线 routes[0] = [1, 5, 7] 表示第 0 辆公交车会一直按序列 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1
# -> ... 这样的车站路线行驶。
#
#
#  现在从 source 车站出发（初始时不在公交车上），要前往 target 车站。 期间仅可乘坐公交车。
#
#  求出 最少乘坐的公交车数量 。如果不可能到达终点车站，返回 -1 。
#
#
#
#  示例 1：
#
#
# 输入：routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# 输出：2
# 解释：最优策略是先乘坐第一辆公交车到达车站 7 , 然后换乘第二辆公交车到车站 6 。
#
#
#  示例 2：
#
#
# 输入：routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= routes.length <= 500.
#  1 <= routes[i].length <= 105
#  routes[i] 中的所有值 互不相同
#  sum(routes[i].length) <= 105
#  0 <= routes[i][j] < 106
#  0 <= source, target < 106
#
#  Related Topics 广度优先搜索
#  👍 119 👎 0


from typing import List
import collections


# 1caojie
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = collections.defaultdict(set)
        routes = list(map(set, routes))
        for i, node in enumerate(routes):
            for j in range(i + 1, len(routes)):
                if node & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)

        sr, tr = set(), set()
        for i, node in enumerate(routes):
            if source in node:
                sr.add(i)
            if target in node:
                tr.add(i)
        step = 1
        seen = set()
        while True:
            tree = set()
            for i in sr:
                if i in tr:
                    return step
                if i in seen:
                    continue
                seen.add(i)
                tree |= graph[i]
            if not tree:
                break
            sr = tree
            step += 1
        return -1


# 2队列方法
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        graph = collections.defaultdict(set)
        routes = list(map(set, routes))
        for i, node in enumerate(routes):
            for j in range(i + 1, len(routes)):
                if node & routes[j]:
                    graph[i].add(j)
                    graph[j].add(i)

        sr, tr = set(), set()
        for i, node in enumerate(routes):
            if source in node:
                sr.add(i)
            if target in node:
                tr.add(i)
        q = collections.deque([[node, 1] for node in sr])
        while q:
            a, depth = q.popleft()
            if a in tr:
                return depth
            sr.add(a)
            for nxt in graph[a]:
                q.append((nxt, depth + 1))
        return -1


Solution().numBusesToDestination(routes=[[1, 2, 7], [3, 6, 7]], source=1, target=6)
