# -*- coding: utf-8 -*-
import collections
from typing import List


# 秋游中的小力和小扣设计了一个追逐游戏。他们选了秋日市集景区中的 N 个景点，景点编号为 1~N。此外，他们还选择了 N 条小路，满足任意两个景点之间都可以通
# 过小路互相到达，且不存在两条连接景点相同的小路。整个游戏场景可视作一个无向连通图，记作二维数组 `edges`，数组中以 `[a,b]` 形式表示景点 a 与景
# 点 b 之间有一条小路连通。
#
# 小力和小扣只能沿景点间的小路移动。小力的目标是在最快时间内追到小扣，小扣的目标是尽可能延后被小力追到的时间。游戏开始前，两人分别站在两个不同的景点 `sta
# rtA` 和 `startB`。每一回合，小力先行动，小扣观察到小力的行动后再行动。小力和小扣在每回合可选择以下行动之一：
# - 移动至相邻景点
# - 留在原地
#
# 如果小力追到小扣（即两人于某一时刻出现在同一位置），则游戏结束。若小力可以追到小扣，请返回最少需要多少回合；若小力无法追到小扣，请返回 -1。
#
# 注意：小力和小扣一定会采取最优移动策略。
#
# **示例 1：**
# >输入：`edges = [[1,2],[2,3],[3,4],[4,1],[2,5],[5,6]], startA = 3, startB = 5`
# >
# >输出：`3`
# >
# >解释：
# >![image.png](https://pic.leetcode-cn.com/1597991318-goeHHr-image.png){:height
# ="250px"}
# >
# >第一回合，小力移动至 2 号点，小扣观察到小力的行动后移动至 6 号点；
# >第二回合，小力移动至 5 号点，小扣无法移动，留在原地；
# >第三回合，小力移动至 6 号点，小力追到小扣。返回 3。
#
#
# **示例 2：**
# >输入：`edges = [[1,2],[2,3],[3,4],[4,1]], startA = 1, startB = 3`
# >
# >输出：`-1`
# >
# >解释：
# >![image.png](https://pic.leetcode-cn.com/1597991157-QfeakF-image.png){:height
# ="250px"}
# >
# >小力如果不动，则小扣也不动；否则小扣移动到小力的对角线位置。这样小力无法追到小扣。
#
# **提示：**
# - `edges` 的长度等于图中节点个数
# - `3 <= edges.length <= 10^5`
# - `1 <= edges[i][0], edges[i][1] <= edges.length 且 edges[i][0] != edges[i][1]`
#
# - `1 <= startA, startB <= edges.length 且 startA != startB`
#
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序
#  👍 15 👎 0
# tarjan找环
# 如果没有大于三个点的环，就说明一定可以抓到，那么b要尽量跑到a最晚到达的位置，且时间相差需要大于1，如果时间相差<=1,说明那个位置至少是同一时刻到达，那么有两种情况，一种是被抓前a与b相隔较远，那么b在原处不动就好了，一种是被抓前与靠近a的方向，那么b会提前被抓
class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        from queue import Queue
        g = collections.defaultdict(set)
        for i, j in edges:
            g[i].add(j)
            g[j].add(i)
        n = len(edges)

        def cal(st):
            res = [-1] * (n + 1)
            q = Queue()
            q.put(st)
            res[st] = 0
            while q.qsize():
                node = q.get()
                for nxt in g[node]:
                    if res[nxt] == -1:
                        res[nxt] = res[node] + 1
                        q.put(nxt)
            return res

        la, lb = cal(startA), cal(startB)
        if la[startB] == 1:
            return 1
        res = 0
        for i, j in zip(la, lb):
            if i - j > 1:
                res = max(res, i)

        dfn = [-1] * (1 + n)
        low = [-1] * (1 + n)
        nbrig = set()

        def dfs(parent, node, timestamp):
            dfn[node] = timestamp
            low[node] = timestamp
            for child in g[node]:
                if child == parent:
                    continue
                if low[child] == -1:
                    low[node] = min(low[node], dfs(node, child, timestamp + 1))
                else:
                    low[node] = min(low[node], low[child])
            if node != 1 and low[node] > dfn[parent]:  # 设1为根节点
                e = sorted([parent, node])
                nbrig.add(tuple(e))
            return low[node]

        dfs(-1, 1, 0)
        if n - len(nbrig) <= 3:
            return res
        points = set()
        for i, j in edges:
            if tuple(sorted([i, j])) not in nbrig:
                points |= {i, j}
        for p in points:
            if la[p] - lb[p] > 1:
                return -1
        return res


# 复写

class Solution:
    def chaseGame(self, edges: List[List[int]], startA: int, startB: int) -> int:
        from queue import Queue
        g = collections.defaultdict(set)
        edges_ = set()
        for i, j in edges:
            edges_.add(tuple(sorted([i, j])))
            g[i].add(j)
            g[j].add(i)
        n = len(edges)

        def cal(st):
            res = [-1] * (n + 1)
            q = Queue()
            q.put(st)
            res[st]=0
            while q.qsize():
                node = q.get()
                for nxt in g[node]:
                    if res[nxt] == -1:
                        res[nxt] = res[node] + 1
                        q.put(nxt)
            return res

        la, lb = cal(startA), cal(startB)
        if la[startB] == 1:
            return 1
        res = 0
        for i, j in zip(la, lb):
            if i - j > 1:
                res = max(i, res)
        dfn, low = [-1] * (n + 1), [-1] * (n + 1)
        nbrig = set()

        def dfs(parent, node, time):
            low[node], dfn[node] = time, time
            for child in g[node]:
                if child==parent:
                    continue
                if low[child] == -1:
                    low[node] = min(low[node], dfs(node, child, time + 1))
                else:
                    low[node] = min(low[node], low[child])
            if node != 1 and low[node] > dfn[parent]:
                nbrig.add(tuple(sorted([parent, node])))
            return low[node]

        dfs(-1, 1, 0)
        if n - len(nbrig) <= 3:
            return res
        points = set()
        for i, j in edges_ - nbrig:
            points |= {i, j}
        for i in points:
            if la[i] - lb[i] > 1:
                return -1
        return res


Solution().chaseGame(edges=[[1, 2], [2, 3], [3, 4], [4, 1], [2, 5], [5, 6]], startA=5, startB=3)
