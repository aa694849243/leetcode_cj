# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-09-04 21:50 
# ide： PyCharm
# 给你一个 有向图 ，它含有 n 个节点和 m 条边。节点编号从 0 到 n - 1 。
#
#  给你一个字符串 colors ，其中 colors[i] 是小写英文字母，表示图中第 i 个节点的 颜色 （下标从 0 开始）。同时给你一个二维数组
# edges ，其中 edges[j] = [aj, bj] 表示从节点 aj 到节点 bj 有一条 有向边 。
#
#  图中一条有效 路径 是一个点序列 x1 -> x2 -> x3 -> ... -> xk ，对于所有 1 <= i < k ，从 xi 到 xi+1 在图
# 中有一条有向边。路径的 颜色值 是路径中 出现次数最多 颜色的节点数目。
#
#  请你返回给定图中有效路径里面的 最大颜色值 。如果图中含有环，请返回 -1 。
#
#
#
#  示例 1：
#
#
#
#  输入：colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# 输出：3
# 解释：路径 0 -> 2 -> 3 -> 4 含有 3 个颜色为 "a" 的节点（上图中的红色节点）。
#
#
#  示例 2：
#
#
#
#  输入：colors = "a", edges = [[0,0]]
# 输出：-1
# 解释：从 0 到 0 有一个环。
#
#
#
#
#  提示：
#
#
#  n == colors.length
#  m == edges.length
#  1 <= n <= 10⁵
#  0 <= m <= 10⁵
#  colors 只含有小写英文字母。
#  0 <= aj, bj < n
#
#
#  Related Topics 图 拓扑排序 记忆化搜索 哈希表 动态规划 计数 👍 34 👎 0
import collections


# 拓扑排序求环，无权重
# 链路顺序与拓扑排序一致
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        indg = [0] * (n := len(colors))
        for vi, vj in edges:
            g[vi].append(vj)
            indg[vj] += 1
        dq = collections.deque()
        for i in range(n):
            if indg[i] == 0:
                dq.append(i)
        dp = [[0] * 26 for _ in range(n)]
        found = 0
        while dq:
            found += 1
            vi = dq.popleft()
            dp[vi][ord(colors[vi]) - 97] += 1  # 延迟更新
            for nxt in g[vi]:
                for i in range(26):
                    dp[nxt][i] = max(dp[nxt][i], dp[vi][i])  # 每次拿到前面一步的最大值
                indg[nxt] -= 1
                if indg[nxt] == 0:
                    dq.append(nxt)
        if found < n:  # 拓扑排序检查环
            return -1
        return max(map(max, dp))

# leetcode submit region end(Prohibit modification and deletion)
