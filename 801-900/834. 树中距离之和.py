# 给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。
#
#  第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。
#
#  返回一个表示节点 i 与其他所有节点距离之和的列表 ans。
#
#  示例 1:
#
#
# 输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# 输出: [8,12,6,10,10,10]
# 解释:
# 如下为给定的树的示意图：
#   0
#  / \
# 1   2
#    /|\
#   3 4 5
#
# 我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# 也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。
#
#
#  说明: 1 <= N <= 10000
#  Related Topics 树 深度优先搜索
#  👍 272 👎 0


# 1树形动态规划 树形dp
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        ans = [0] * N
        dp = [0] * N
        sz = [0] * N
        graph = [[] for _ in range(N)]
        for node,nei in edges:
            graph[nei].append(node)
            graph[node].append(nei)

        def dfs(node, father):
            sz[node] = 1
            for nei in graph[node]:
                if nei == father:
                    continue
                dp[node] += dfs(nei, node) + sz[nei]
                sz[node] += sz[nei]
            return dp[node]

        def dfs2(node, father):
            ans[node] = dp[node]
            for nei in graph[node]:
                if nei == father:
                    continue
                dp_origin_node, sz_origin_node, dp_origin_nei, sz_origin_nei = dp[node], sz[node], dp[nei], sz[nei]
                dp[node] -= dp[nei] + sz[nei]
                sz[node] -= sz[nei]
                dp[nei] += dp[node] + sz[node]
                sz[nei] += sz[node]
                dfs2(nei, node)
                dp[node], sz[node], dp[nei], sz[nei] = dp_origin_node, sz_origin_node, dp_origin_nei, sz_origin_nei

        dfs(0, -1)
        dfs2(0, -1)
        return ans
Solution().sumOfDistancesInTree(6,[[0,1],[0,2],[2,3],[2,4],[2,5]])