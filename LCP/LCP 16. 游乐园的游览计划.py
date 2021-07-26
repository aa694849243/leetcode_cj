# -*- coding: utf-8 -*-
import collections
import itertools
from typing import List


# 又到了一年一度的春游时间，小吴计划去游乐场游玩 1 天，游乐场总共有 N 个游乐项目，编号从 0 到 N-1。小吴给每个游乐项目定义了一个非负整数值 val
# ue[i] 表示自己的喜爱值。两个游乐项目之间会有双向路径相连，整个游乐场总共有 M 条双向路径，保存在二维数组 edges中。 小吴计划选择一个游乐项目 A
# 作为这一天游玩的重点项目。上午小吴准备游玩重点项目 A 以及与项目 A 相邻的两个项目 B、C （项目A、B与C要求是不同的项目，且项目B与项目C要求相邻），并
# 返回 A ，即存在一条 A-B-C-A 的路径。 下午，小吴决定再游玩重点项目 A以及与A相邻的两个项目 B'、C'，（项目A、B'与C'要求是不同的项目，且项
# 目B'与项目C'要求相邻），并返回 A ，即存在一条 A-B'-C'-A 的路径。下午游玩项目 B'、C' 可与上午游玩项目B、C存在重复项目。 小吴希望提前安
# 排好游玩路径，使得喜爱值之和最大。请你返回满足游玩路径选取条件的最大喜爱值之和，如果没有这样的路径，返回 0。 注意：一天中重复游玩同一个项目并不能重复增加喜爱
# 值了。例如：上下午游玩路径分别是 A-B-C-A与A-C-D-A 那么只能获得 value[A] + value[B] + value[C] + value[D
# ] 的总和。
#
#  示例 1：
#
#
#  输入：edges = [[0,1],[1,2],[0,2]], value = [1,2,3]
#
#  输出：6
#
#  解释：喜爱值之和最高的方案之一是 0->1->2->0 与 0->2->1->0 。重复游玩同一点不重复计入喜爱值，返回1+2+3=6
#
#
#  示例 2：
#
#
#  输入：edges = [[0,2],[2,1]], value = [1,2,5]
#
#  输出：0
#
#  解释：无满足要求的游玩路径，返回 0
#
#
#  示例 3：
#
#
#  输入：edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,3],[2,4],[2,5],[3,4],[3,5],[4,5]
# ], value = [7,8,6,8,9,7]
#
#  输出：39
#
#  解释：喜爱值之和最高的方案之一是 3->0->1->3 与 3->4->5->3 。喜爱值最高为 7+8+8+9+7=39
#
#
#  限制：
#
#
#  3 <= value.length <= 10000
#  1 <= edges.length <= 10000
#  0 <= edges[i][0],edges[i][1] < value.length
#  0 <= value[i] <= 10000
#  edges中没有重复的边
#  edges[i][0] != edges[i][1]
#
#  Related Topics 图 几何 数学
#  👍 17 👎 0


# 这里有个很有意思的地方，就是假如某个点有多个最大三角形，但题解只考虑了一个。假设有超过两个不共线的最大三角形，那么随机选两个组合直接可以作为答案。假设只有两个最大三角形且共线，比如 acb和acd为两个相同的最大三角形，由于共线ac，所以b=d，我们只考虑acb为最大三角形，那么需要考虑的情况为 1cb不分开的情况:考虑acb+axy(x,y为可以与a组成三角形的任意点) 以及2cb分开为两个三角形的情况：acd(此为有ac边的最大三角形）+abz(z为可以与ab组成三角形的任意点)。整理一下就是求max(acb+axy,acd+abz)=a+b+c+max(x+y,d+z)，同样地，我们将acd作为最大三角形考虑，最终求的是a+d+c+max(x+y,b+z)，因为b=d，所以两个式子是相同的，也就是说当存在共线的最大三角形时，我们考虑任意一个都能得到正确的结果

# 每条边为什么保留3个最大三角形呢？设最大三角形为axb，边分别为 ax 和 bx，假如出现这么一种情况 ax:[axb,axc,axd] 和 bx:[bxa,bxc,bxd] ,如果只保留两个那么axd或bxd无法考虑，最大的两个三角形变成了axc和bxc(axb不属于ab分开的情况，为了简便就不讨论它了)，只能a,b,c,x四个点的和，如果多考虑axd或bxd则结果为a,b,c,d,x五个点的和
class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        from sortedcontainers import SortedList
        m = collections.defaultdict(list)  # 储存每个点所连三角形
        maxtri = collections.defaultdict(list)  # 储存每个点所连最大三角形
        me = collections.defaultdict(lambda: SortedList(key=lambda x: -x[3]))  # 储存每条边所连top3三角形
        g = collections.defaultdict(set)  # 图,储存每个点的邻接点
        for i, j in edges:
            i, j = sorted([i, j])
            g[i].add(j)
        n = len(value)

        # def gettop3(i, j, trinfo):
        #     me[i, j].add(trinfo)
        #     me[i, j] = SortedList(me[i, j][:3], key=lambda x: -x[3])

        def cal(t1, t2):
            all_points = set(t1[:3] + t2[:3])
            return sum(value[i] for i in all_points)

        for i in range(n):
            for j in g[i]:
                for k in g[i] & g[j]:
                    trinfo = [i, j, k, sum(value[x] for x in [i, j, k])]
                    for node in [i, j, k]:
                        if not maxtri[node] or trinfo[-1] > maxtri[node][-1]:
                            maxtri[node] = trinfo
                        m[node].append([i, j, k])
                    for e1, e2 in [(i, j), (i, k), (j, k)]:
                        me[e1, e2].add(trinfo)
                        if len(me[e1, e2]) > 3:
                            me[e1, e2].pop()

        res = 0
        for node in range(n):
            if not m[node]:
                continue
            i, j, k, w = maxtri[node]
            res = max(w, res)  # 只有一个三角形的情况
            for info in m[node]:  # 最大三角形作为一个三角形讨论
                res = max(res, cal([i, j, k], info))
            li = [i, j, k]
            li.remove(node)
            e1, e2 = list(itertools.product([node], li))
            e1, e2 = tuple(sorted(e1)), tuple(sorted(e2))
            for info1 in me[e1]:
                for info2 in me[e2]:
                    res = max(res, cal(info1, info2))
        return res


# 复写

class Solution:
    def maxWeight(self, edges: List[List[int]], value: List[int]) -> int:
        from sortedcontainers import SortedList
        g = collections.defaultdict(set)
        maxnode = collections.defaultdict(list)
        m = collections.defaultdict(list)
        me = collections.defaultdict(lambda: SortedList(key=lambda x: -x[3]))
        for i, j in edges:
            i, j = sorted([i, j])
            g[i].add(j)
        n = len(value)
        for i in range(n):
            for j in g[i]:
                for k in g[i] & g[j]:
                    trinfo = [i, j, k, sum(value[x] for x in [i, j, k])]
                    for node in [i, j, k]:
                        if not maxnode[node] or trinfo[-1] > maxnode[node][-1]:
                            maxnode[node] = trinfo
                        m[node].append([i,j,k])
                    for e1,e2 in [(i,j),(i,k),(j,k)]:
                        me[e1,e2].add(trinfo)
                        if len(me[e1,e2])>3:
                            me[e1,e2].pop()
        res=0
        def cal(info1,info2):
            points=set(info1+info2)
            return sum(value[i] for i in points)
        for node in range(n):
            if not maxnode[node]:
                continue
            i,j,k,w=maxnode[node]
            res=max(res,w)
            for info in m[node]:
                res=max(res,cal([i,j,k],info))
            li=[i,j,k]
            li.remove(node)
            e1,e2=list(itertools.product([node],li))
            e1,e2=tuple(sorted(e1)),tuple(sorted(e2))
            for info1 in me[e1]:
                for info2 in me[e2]:
                    res=max(res,cal(info1[:3],info2[:3]))
        return res

Solution().maxWeight([[2, 9], [4, 9], [0, 6], [0, 1], [3, 5], [1, 2], [5, 9], [2, 5], [6, 9], [7, 8], [0, 7], [1, 4], [6, 8], [8, 9], [1, 9], [6, 7], [1, 6], [2, 4], [0, 8], [4, 5], [1, 3], [0, 9], [0, 5], [3, 6], [1, 7], [4, 7], [5, 8], [0, 4], [0, 2], [3, 9]], [9327, 1424, 8248, 1216, 6629, 5729, 6388, 8371, 6345, 8])
