# 给出 graph 为有 N 个节点（编号为 0, 1, 2, ..., N-1）的无向连通图。
#
#  graph.length = N，且只有节点 i 和 j 连通时，j != i 在列表 graph[i] 中恰好出现一次。
#
#  返回能够访问所有节点的最短路径的长度。你可以在任一节点开始和停止，也可以多次重访节点，并且可以重用边。
#
#
#
#
#
#
#  示例 1：
#
#  输入：[[1,2,3],[0],[0],[0]]
# 输出：4
# 解释：一个可能的路径为 [1,0,2,0,3]
#
#  示例 2：
#
#  输入：[[1],[0,2,4],[1,3,4],[2],[1,2]]
# 输出：4
# 解释：一个可能的路径为 [0,1,4,2,3]
#
#
#
#
#  提示：
#
#
#  1 <= graph.length <= 12
#  0 <= graph[i].length < graph.length
#
#  Related Topics 广度优先搜索 动态规划
#  👍 123 👎 0


from typing import List

# 1状态压缩+深度优先遍历
import collections


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph or not graph[0]:
            return 0
        m = collections.defaultdict(lambda: float('inf'))
        n = len(graph)
        q = collections.deque()
        for move in range(n):
            m[(1 << move, move)] = 0
            q.append((1 << move, move))
        while q:
            cover, node = q.popleft()
            d = m[cover, node]
        for nei in graph[node]:
            cover2, d_ = cover | 1 << nei, d + 1
            if cover2 == (1 << n) - 1:
                return d_
            if d_ < m[cover2, nei]:
                q.append((cover2, nei))
                m[cover2, nei] = d_


# 2bellman-ford 松弛 动态规划 判断有无负权回路 spfa为优化版
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if not graph or not graph[0]:
            return 0
        n = len(graph)
        dp = [[float('inf')] * n for _ in range(1 << n)]
        for i in range(n):
            dp[1 << i][i] = 0

        def relax(cover, v1, v2):
            if dp[cover][v1] == float('inf'):
                pass
            elif dp[cover | 1 << v2][v2] > dp[cover][v1] + 1:
                dp[cover | 1 << v2][v2] = dp[cover][v1] + 1
                return True
            return False

        cover = 0
        while cover < 1 << n:
            repeat = True
            while repeat:  # 每次都松弛到无法再松弛的程度
                repeat = False
                for node, d in enumerate(dp[cover]):
                    for nei in graph[node]:
                        # if relax(cover, node, nei): 原始版本
                        #     repeat = True
                        if relax(cover, node, nei) and cover == cover | 1 << nei: #如果更新到同一层的化，需要再检查这一层的情况是否可以再更新,此外函数在前可以先执行完函数
                            repeat = True
            cover += 1
        return min(dp[(1 << n) - 1])


Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]])
