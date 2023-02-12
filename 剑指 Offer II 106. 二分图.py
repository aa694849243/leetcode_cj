# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 20:09 
# ide： PyCharm
import collections

# 染色法，二分图
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = {}

        def dfs(i, color):
            if i in colors and colors[i] != color:
                return False
            colors[i] = color
            for nxt in graph[i]:
                if nxt not in colors:
                    colors[nxt] = 1 - color
                    if not dfs(nxt, 1 - color):
                        return False
                elif colors[nxt] == color:
                    return False
            return True

        return all(dfs(i, 0) for i in range(len(graph)) if i not in colors)
# leetcode submit region end(Prohibit modification and deletion)
