import collections
import functools
from typing import List


# @solution-sync:begin
# bfs单向树
# https://leetcode-cn.com/problems/count-subtrees-with-max-distance-between-cities/solution/python3-shu-xing-dp-by-simpleson/
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # 这里定义为函数，类似一个类，使后面初始化成具体数据结构
        Tree = lambda: collections.defaultdict(collections.Counter)

        def iter_tree(mat: Tree):
            for depth, dists in mat.items():
                for dist, count in dists.items():
                    yield depth, dist, count

        links = Tree()
        for u, v in edges:
            links[u][v] = 1
            links[v][u] = 1
        # 单向bfs树
        bfs = [1]
        for L in bfs:
            for R in links[L]:
                bfs.append(R)
                links[R].pop(L)

        @functools.lru_cache(None)
        def dfs(L):
            count = Tree()
            count[0][0] = 1
            if not links[L]:
                return count
            for R in links[L]:
                upd = Tree()
                # 以最大深度作为代表，左右两颗树相当于两个混沌状态，观察混沌状态中抽出的两个节点相加能否更新最大深度
                for depthR, distR, countR in iter_tree(dfs(R)):
                    for depthL, distL, countL in iter_tree(count):
                        upd[max(depthR + 1, depthL)][max(depthR + depthL + 1, distR, distL)] += countL * countR
                for d in upd:
                    count[d] += upd[d]
            return count

        total = collections.Counter()
        # 每个点都可以作为根节点试一次
        for node in range(1, n+1):
            for dist_cnt in dfs(node).values():
                total += dist_cnt
        return [total[d] for d in range(1, n)]


# @solution
print(Solution().countSubgraphsForEachDiameter(5, [[1, 5], [2, 3], [2, 4], [2, 5]]))
