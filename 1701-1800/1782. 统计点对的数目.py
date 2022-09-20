# 给你一个无向图，无向图由整数 n ，表示图中节点的数目，和 edges 组成，其中 edges[i] = [ui, vi] 表示 ui 和 vi 之间有一条
# 无向边。同时给你一个代表查询的整数数组 queries 。
#
#  第 j 个查询的答案是满足如下条件的点对 (a, b) 的数目：
#
#
#  a < b
#  cnt 是与 a 或者 b 相连的边的数目，且 cnt 严格大于 queries[j] 。
#
#
#  请你返回一个数组 answers ，其中 answers.length == queries.length 且 answers[j] 是第 j 个查询的答
# 案。
#
#  请注意，图中可能会有 重复边 。
#
#
#
#  示例 1：
#
#
# 输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# 输出：[6,5]
# 解释：每个点对中，与至少一个点相连的边的数目如上图所示。
#
#
#  示例 2：
#
#
# 输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries =
#  [1,2,3,4,5]
# 输出：[10,10,9,8,6]
#
#
#
#
#  提示：
#
#
#  2 <= n <= 2 * 10⁴
#  1 <= edges.length <= 10⁵
#  1 <= ui, vi <= n
#  ui != vi
#  1 <= queries.length <= 20
#  0 <= queries[j] < edges.length
#
#
#  Related Topics 图 双指针 二分查找 👍 33 👎 0
import collections
from typing import List
import bisect
import itertools


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        g = [0] * n
        m_edges = collections.defaultdict(int)
        for u, v in edges:  # 存储每个点拥有的边数
            g[u - 1] += 1
            g[v - 1] += 1
            m_edges[tuple(sorted([u - 1, v - 1]))] += 1
        g_sorted = sorted(g)
        res = [0] * len(queries)
        for s, cnt in enumerate(g_sorted):
            for i, q in enumerate(queries):
                s_ = bisect.bisect_right(g_sorted, q - cnt, s + 1)
                res[i] += n - s_
        for k, v in m_edges.items():
            sum_ = g[k[0]] + g[k[1]]
            for i, q in enumerate(queries):
                if sum_ > q and sum_ - v <= q:
                    res[i] -= 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countPairs(4, [[1, 2], [2, 4], [1, 3], [2, 3], [2, 1]], [2, 3]))
