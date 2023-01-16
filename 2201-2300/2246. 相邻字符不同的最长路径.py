# -*- coding: utf-8 -*-
# 给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。用下标从 0 开始、长度为 n 的数组
#  parent 来表示这棵树，其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。
#
#  另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。
#
#  请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。
#
#
#
#  示例 1：
#
#
#
#
# 输入：parent = [-1,0,0,1,1,2], s = "abacbe"
# 输出：3
# 解释：任意一对相邻节点字符都不同的最长路径是：0 -> 1 -> 3 。该路径的长度是 3 ，所以返回 3 。
# 可以证明不存在满足上述条件且比 3 更长的路径。
#
#
#  示例 2：
#
#
#
#
# 输入：parent = [-1,0,0,0], s = "aabc"
# 输出：3
# 解释：任意一对相邻节点字符都不同的最长路径是：2 -> 0 -> 3 。该路径的长度为 3 ，所以返回 3 。
#
#
#
#
#  提示：
#
#
#  n == parent.length == s.length
#  1 <= n <= 10⁵
#  对所有 i >= 1 ，0 <= parent[i] <= n - 1 均成立
#  parent[0] == -1
#  parent 表示一棵有效的树
#  s 仅由小写英文字母组成
#
#
#  Related Topics 树 深度优先搜索 图 拓扑排序 数组 字符串
#  👍 38 👎 0
import collections
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        g = collections.defaultdict(list)
        for i in range(1, len(parent)):
            g[parent[i]].append(i)
        self.res = 1

        def dfs(u):
            if not g[u]:
                return 1
            legs = [0]
            for v in g[u]:
                length = dfs(v)
                if s[v] != s[u]:
                    legs.append(length)
            if len(legs) == 1:
                return 1
            else:
                a, b = heapq.nlargest(2, legs)
                self.res = max(self.res, a + b + 1)
                return max([a, b]) + 1

        dfs(0)
        return self.res

# leetcode submit region end(Prohibit modification and deletion)
