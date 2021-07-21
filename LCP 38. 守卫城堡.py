# -*- coding: utf-8 -*-
import collections
from typing import List


# 城堡守卫游戏的胜利条件为使恶魔无法从出生点到达城堡。游戏地图可视作 `2*N` 的方格图，记作字符串数组 `grid`，其中：
# - `"."` 表示恶魔可随意通行的平地；
# - `"#"` 表示恶魔不可通过的障碍物，玩家可通过在 **平地** 上设置障碍物，即将 `"."` 变为 `"#"` 以阻挡恶魔前进；
# - `"S"` 表示恶魔出生点，将有大量的恶魔该点生成，恶魔可向上/向下/向左/向右移动，且无法移动至地图外；
# - `"P"` 表示瞬移点，移动到 `"P"` 点的恶魔可被传送至任意一个 `"P"` 点，也可选择不传送；
# - `"C"` 表示城堡。
#
# 然而在游戏中用于建造障碍物的金钱是有限的，请返回玩家最少需要放置几个障碍物才能获得胜利。若无论怎样放置障碍物均无法获胜，请返回 `-1`。
#
# **注意：**
# - 地图上可能有一个或多个出生点
# - 地图上有且只有一个城堡
#
# **示例 1**
# >输入：`grid = ["S.C.P#P.", ".....#.S"]`
# >
# >输出：`3`
# >
# >解释：至少需要放置三个障碍物
# ![image.png](https://pic.leetcode-cn.com/1614828255-uuNdNJ-image.png)
#
#
# **示例 2：**
# >输入：`grid = ["SP#P..P#PC#.S", "..#P..P####.#"]`
# >
# >输出：`-1`
# >
# >解释：无论怎样修筑障碍物，均无法阻挡最左侧出生的恶魔到达城堡位置
# ![image.png](https://pic.leetcode-cn.com/1614828208-oFlpVs-image.png)
#
# **示例 3：**
# >输入：`grid = ["SP#.C.#PS", "P.#...#.P"]`
# >
# >输出：`0`
# >
# >解释：无需放置障碍物即可获得胜利
# ![image.png](https://pic.leetcode-cn.com/1614828242-oveClu-image.png)
#
# **示例 4：**
# >输入：`grid = ["CP.#.P.", "...S..S"]`
# >
# >输出：`4`
# >
# >解释：至少需要放置 4 个障碍物，示意图为放置方法之一
# ![image.png](https://pic.leetcode-cn.com/1614828218-sIAYkb-image.png)
#
#
# **提示：**
# - `grid.length == 2`
# - `2 <= grid[0].length == grid[1].length <= 10^4`
# - `grid[i][j]` 仅包含字符 `"."`、`"#"`、`"C"`、`"P"`、`"S"`
#  Related Topics 数组 动态规划 矩阵
#  👍 3 👎 0

# 最大流 最小割
class Solution:
    def guardCastle(self, grid: List[str]) -> int:
        C = len(grid[0])
        n = 2 * C  # 计算总节点数量，因为后面需要拆节点，将一个节点变成入点和出点，所以最终的总节点数其实是4*C
        cap = collections.defaultdict(int)  # 定义两个节点的流量
        f = {}
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        inf = 20010

        def cal(i, j):  # 将2维数据转为1维
            if (i, j) in f:
                return f[i, j]
            return i * C + j

        g = collections.defaultdict(list)  # 边表的图
        devil = -2  # 定义超级恶魔节点
        gate = -1  # 定义超级传送门节点
        for r in range(2):  # 构建边表
            for c in range(C):
                if grid[r][c] == '#':
                    continue
                num = cal(r, c)
                g[num].append(num + n)  # 所有的非#节点都给他增加一条边，也就是节点入口->节点出口，其实并不是所有节点都需要这么做，我这么写纯粹是为了方便
                if grid[r][c] == '.':
                    cap[num, num + n] = 1  # 设置节点间的流量，如果是.号，那么流量是1，
                elif grid[r][c] == 'P':  # 遇到传送门的情况
                    cap[num, num + n] = inf  # 节点入口->出口流量设置为inf
                    cap[num + n, gate] = inf  # 节点出口->超级传送门，流量同样设置为inf
                    cap[gate, num] = inf  # 超级传送门->节点入口，流量为inf
                    g[num + n].append(gate)  # 给节点出口和超级传送门加一条边
                    g[gate].append(num)  # 超级传送门也和节点入口加一条边
                elif grid[r][c] == 'S':  # 遇到恶魔节点
                    cap[num, num + n] = inf
                    cap[num + n, devil] = inf  # 传送到超级恶魔节点
                    cap[devil, num] = inf
                    g[num + n].append(devil)  # 因为超级恶魔节点是终点，所以不用传送回来
                elif grid[r][c] == 'C':  # 起始节点，为了统一，我也将起始节点拆为入口和出口了
                    src = num
                    cap[num, num + n] = inf
                for dr, dc in dirs:  # 遍历四个方向
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < 2 and 0 <= nc < C and grid[nr][nc] != '#':
                        nnum = cal(nr, nc)  # 邻接节点的入口数字
                        cap[num + n, nnum] = inf  # 上一个节点的出口->该节点的入口，流量同样设置为1
                        g[num + n].append(nnum)

        def bfs():  # bfs是为了观察起始点能否到达超级恶魔节点，如果可以到达，说明还要继续割边
            dist = collections.defaultdict(lambda: -1)  # 定义一个层次的列表，防止某一节点重复遍历，并定义各节点的层次
            q = collections.deque([src])
            dist[src] = 0
            while q:  # 简单的bfs
                node = q.popleft()
                for nxt in g[node]:
                    if dist[nxt] == -1 and cap[node, nxt] > 0:
                        dist[nxt] = dist[node] + 1
                        if nxt == devil:
                            return dist
                        q.append(nxt)
            return dist

        def dfs(node, flow):  # 利用dfs进行最大流量计算，最大流量就是最小割边
            if node == -2:  # 到达终点，此次最大流量计算完成
                return flow
            delta = flow  # 原流量
            for nxt in g[node]:
                if dist[nxt] == dist[node] + 1 and cap[node, nxt] > 0:  # 只有下一层次的节点才能进行遍历
                    a = dfs(nxt, min(delta, cap[node, nxt]))  # 该节点出去的可以割掉的流量
                    if a:
                        cap[node, nxt] -= a  # 正向流量减少
                        cap[nxt, node] += a  # 逆向流量增加，这一步必不可少，不懂的可以用这个例子debug一下，["CP....", "##.S.P"]，正确结果是3，不加逆向边的话结果会是2
                        if cap[nxt, node] > 0:  # 因为逆向流量增加了，nxt节点就新增加了一条边
                            g[nxt].append(node)
                        delta -= a
                        if delta == 0:  # 没流量可以割了就提前结束吧
                            return flow
            return flow - delta  # 总流量-剩下的流量=割掉的流量

        ans = 0
        while ans < inf:
            dist = bfs()  # 返回一个新的层次列表
            if dist[devil] == -1:  # 如果仍然可达最终节点，说明还要继续割，反之就不用割了
                break
            ans += dfs(src, inf)
        return ans if ans < inf else -1  # 如果最后计算的最大流为inf，说明已经触碰到了设置的屏障，也就是没有办法阻止到达最终节点了


# 动态规划
# https://leetcode-cn.com/problems/7rLGCR/solution/lcp-38-shou-wei-cheng-bao-by-zerotrac2-kgv2/
class Solution:
    def guardCastle(self, grid: List[str]) -> int:
        C = len(grid[0])
        inf = 20010
        m1 = {'.': 0, 'S': 1, 'C': 2, 'P': 2, '#': 3}  # 设置映射表，分别让传送门代表恶魔或让传送门代表城堡，思路是阻止恶魔靠近传送门（此时城堡和传送门连通），或阻止传送门靠近城堡（此时传送门和恶魔连通）
        m2 = {'.': 0, 'S': 1, 'C': 2, 'P': 1, '#': 3}

        def _update(t1, t2, f, extra):  # 更新状态t1,t2分别代表当前列上下两行的chr，f为上一步的状态以及对应的需要加石头次数，注意f里全部的状态是能阻止恶魔靠近城堡的状态
            nf = collections.defaultdict(lambda: inf)  # 新的状态字典
            if (t1, t2) in {(1, 2), (2, 1)}:  # 当t1,t2互为恶魔城堡，那么直接返回空字典，代表无论如何都无法阻止恶魔靠近城堡了
                return {}
            for (s1, s2) in f:
                nt1, nt2 = t1, t2  # 临时变量储存t1,t2的值，因为根据上一步的状态t1,t2可能改变
                if {(s1, nt1), (s2, nt2), (s1, s2)} & {(1, 2), (2, 1)}:  # 如果存在恶魔和城堡相邻的情况，那么就不用考虑了
                    continue
                if nt1 == 0:  # 当nt1为空地，说明可以被左边一格传染
                    nt1 = s1 if s1 != 3 else nt1
                if nt2 == 0:
                    nt2 = s2 if s2 != 3 else nt2
                nt1 = nt2 if nt1 == 0 and nt2 != 3 else nt1  # nt1和nt2可以互相传染
                nt2 = nt1 if nt2 == 0 and nt1 != 3 else nt2
                if (nt1, nt2) in {(1, 2), (2, 1)}:  # 如果经过传染后上下互为恶魔城堡，那么跳过
                    continue
                nf[nt1, nt2] = min(f[s1, s2] + extra, nf[nt1, nt2])  # 根据情况补石头
            return dict(nf)

        def merge(li):
            ans = {}
            for t in li:
                ans.update(t)
            return ans

        def solve(m):
            f = {(0, 0): 0}
            for i in range(C):
                t1, t2 = m[grid[0][i]], m[grid[1][i]]
                f1 = _update(t1, t2, f, 0)  # 不补石头
                f2 = _update(3, t2, f, 1) if t1 == 0 else {}  # 补1颗
                f3 = _update(t1, 3, f, 1) if t2 == 0 else {}
                f4 = _update(3, 3, f, 2) if t1 == 0 and t2 == 0 else {}  # 补两颗
                f = merge([f1, f2, f3, f4])  # 合并字典
            return min(f.values()) if f else inf #返回最终状态里的最小值

        ans = min(solve(m1), solve(m2))
        return ans if ans < inf else -1


Solution().guardCastle(["CP.#.P.", "...S..S"])
# Solution().guardCastle(["CP....", "##.S.P"])
