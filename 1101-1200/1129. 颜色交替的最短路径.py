# -*- coding: utf-8 -*-
import collections
from typing import List


# 在一个有向图中，节点分别标记为 0, 1, ..., n-1。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。
#
#  red_edges 中的每一个 [i, j] 对表示从节点 i 到节点 j 的红色有向边。类似地，blue_edges 中的每一个 [i, j] 对表示从
# 节点 i 到节点 j 的蓝色有向边。
#
#  返回长度为 n 的数组 answer，其中 answer[X] 是从节点 0 到节点 X 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，
# 那么 answer[x] = -1。
#
#
#
#  示例 1：
#
#  输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# 输出：[0,1,-1]
#
#
#  示例 2：
#
#  输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# 输出：[0,1,-1]
#
#
#  示例 3：
#
#  输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# 输出：[0,-1,-1]
#
#
#  示例 4：
#
#  输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# 输出：[0,1,2]
#
#
#  示例 5：
#
#  输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# 输出：[0,1,1]
#
#
#
#
#  提示：
#
#
#  1 <= n <= 100
#  red_edges.length <= 400
#  blue_edges.length <= 400
#  red_edges[i].length == blue_edges[i].length == 2
#  0 <= red_edges[i][j], blue_edges[i][j] < n
#
#  Related Topics 广度优先搜索 图
#  👍 77 👎 0


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph_red = collections.defaultdict(list)
        graph_blue = collections.defaultdict(list)
        for i, j in red_edges:
            graph_red[i].append(j)
        for i, j in blue_edges:
            graph_blue[i].append(j)
        ans = [-1] * n
        red = [0] * n
        red[0] = 1
        blue = [0] * n
        t = [0]
        p = 0
        while True:
            tree = []
            if p % 2 == 0:  # red
                for node in t:
                    ans[node] = p if p < ans[node] or ans[node] == -1 else ans[node]
                    for nxt in graph_red[node]:
                        if ans[nxt] != -1 and blue[nxt] != 0:
                            continue
                        blue[nxt] = 1
                        tree.append(nxt)
            else:
                for node in t:
                    ans[node] = p if p < ans[node] or ans[node] == -1 else ans[node]
                    for nxt in graph_blue[node]:
                        if ans[nxt] != -1 and red[nxt] != 0:
                            continue
                        red[nxt] = 1
                        tree.append(nxt)
            if not tree:
                break
            p += 1
            t = tree
        ans2 = [-1] * n
        red = [0] * n
        blue = [0] * n
        blue[0] = 1
        t = [0]
        p = 0
        while True:
            tree = []
            if p % 2:  # blue
                for node in t:
                    ans2[node] = p if p < ans2[node] or ans2[node] == -1 else ans2[node]
                    for nxt in graph_red[node]:
                        if ans2[nxt] != -1 and red[nxt] != 0:
                            continue
                        red[nxt] = 1
                        tree.append(nxt)
            else:
                for node in t:
                    ans2[node] = p if p < ans2[node] or ans2[node] == -1 else ans2[node]
                    for nxt in graph_blue[node]:
                        if ans2[nxt] != -1 and blue[nxt] != 0:
                            continue
                        blue[nxt] = 1
                        tree.append(nxt)
            if not tree:
                break
            p += 1
            t = tree
        newans=[]
        for i,j in zip(ans,ans2):
            if i!=-1 and j!=-1:
                newans.append(min(i,j))
            elif i==-1:
                newans.append(j)
            else:
                newans.append(i)

        return newans


Solution().shortestAlternatingPaths(5, [[3,2],[4,1],[1,4],[2,4]],[[2,3],[0,4],[4,3],[4,4],[4,0],[1,0]])
