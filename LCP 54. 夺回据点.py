# -*- coding: utf-8 -*-
# 欢迎各位勇者来到力扣城，本次试炼主题为「夺回据点」。
#
# 魔物了占领若干据点，这些据点被若干条道路相连接，`roads[i] = [x, y]` 表示编号 `x`、`y` 的两个据点通过一条道路连接。
#
# 现在勇者要将按照以下原则将这些据点逐一夺回：
#
# - 在开始的时候，勇者可以花费资源先夺回一些据点，初始夺回第 `j` 个据点所需消耗的资源数量为 `cost[j]`
#
# - 接下来，勇者在不消耗资源情况下，每次可以夺回**一个**和「已夺回据点」相连接的魔物据点，并对其进行夺回
#
# > 注：为了防止魔物暴动，勇者在每一次夺回据点后（包括花费资源夺回据点后），需要保证剩余的所有魔物据点之间是相连通的（不经过「已夺回据点」）。
#
# 请返回勇者夺回所有据点需要消耗的最少资源数量。
#
# **注意：**
# - 输入保证初始所有据点都是连通的，且不存在重边和自环
#
# **示例 1：**
#
# > 输入：
# > `cost = [1,2,3,4,5,6]`
# > `roads = [[0,1],[0,2],[1,3],[2,3],[1,2],[2,4],[2,5]]`
# >
# > 输出：`6`
# >
# > 解释：
# > 勇者消耗资源 `6` 夺回据点 `0` 和 `4`，魔物据点 `1、2、3、5` 相连通；
# > 第一次夺回据点 `1`，魔物据点 `2、3、5` 相连通；
# > 第二次夺回据点 `3`，魔物据点 `2、5` 相连通；
# > 第三次夺回据点 `2`，剩余魔物据点 `5`；
# > 第四次夺回据点 `5`，无剩余魔物据点；
# > 因此最少需要消耗资源为 `6`，可占领所有据点。
# > ![image.png](https://pic.leetcode-cn.com/1648706944-KJstUN-image.png){:
# height=170px}
#
# **示例 2：**
#
# > 输入：
# > `cost = [3,2,1,4]`
# > `roads = [[0,2],[2,3],[3,1]]`
# >
# > 输出：`2`
# >
# > 解释：
# > 勇者消耗资源 `2` 夺回据点 `1`，魔物据点 `0、2、3` 相连通；
# > 第一次夺回据点 `3`，魔物据点 `2、0` 相连通；
# > 第二次夺回据点 `2`，剩余魔物据点 `0`；
# > 第三次夺回据点 `0`，无剩余魔物据点；
# > 因此最少需要消耗资源为 `2`，可占领所有据点。
# > ![image.png](https://pic.leetcode-cn.com/1648707186-LJRwzU-image.png){:
# height=60px}
#
# **提示：**
# - `1 <= roads.length, cost.length <= 10^5`
# - `0 <= roads[i][0], roads[i][1] < cost.length`
# - `1 <= cost[i] <= 10^9`
#
#  Related Topics 图 数组 双连通分量
#  👍 8 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import collections
from collections import defaultdict


# https://leetcode.cn/problems/s5kipK/solution/by-gittauros-aaa2/
class Solution:
    def minimumCost(self, cost: List[int], roads: List[List[int]]) -> int:
        # 利用tarjan求无向图点双连通分量
        n = len(cost)
        dcc = []
        dfn = [0] * n
        low = [0] * n
        g = collections.defaultdict(set)
        for u, v in roads:
            g[u].add(v)
            g[v].add(u)
        stack = []
        cuts = set()
        timestamp = 1
        root = 0

        def tarjan3(cur):
            nonlocal timestamp
            dfn[cur] = low[cur] = timestamp
            timestamp += 1
            child_num = 0
            stack.append(cur)
            for child in g[cur]:
                if dfn[child] == 0:
                    tarjan3(child)
                    low[cur] = min(low[cur], low[child])
                    if low[child] >= dfn[cur]:
                        child_num += 1
                        if cur != root or child_num > 1:
                            cuts.add(cur)
                        dcc.append([])
                        t = stack.pop()
                        dcc[-1].append(t)
                        while t != child:
                            t = stack.pop()
                            dcc[-1].append(t)
                        dcc[-1].append(cur)
                else:
                    low[cur] = min(low[cur], dfn[child])
            if cur == root and child_num == 0:
                dcc.append([cur])

        tarjan3(0)  # dcc存储的是点双连通分量
        if len(dcc) == 1:
            return min(cost)
        leaf = []
        for dc in dcc:
            cut_cnt = 0
            mi = float('inf')
            for node in dc:
                if node in cuts:
                    cut_cnt += 1
                else:  # 割点只能最后占，占据割点后会对整张图进行分割，所以只有单割点的点双连通分量可以作为叶子节点
                    mi = min(mi, cost[node])
            if cut_cnt == 1:  # 当割点只有一个，那么该点双连通分量可以作为叶子节点
                leaf.append(mi)
        leaf.sort()
        return sum(leaf[:-1])  # 最后一个叶子节点不用提前占


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimumCost(
    [9, 2, 3, 4, 5, 6, 7],
    [[1, 2], [1, 3], [2, 3], [3, 6], [6, 0], [0, 3], [4, 2], [2, 5], [4, 5]]
))
