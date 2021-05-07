# 两个玩家分别扮演猫（Cat）和老鼠（Mouse）在无向图上进行游戏，他们轮流行动。
#
#  该图按下述规则给出：graph[a] 是所有结点 b 的列表，使得 ab 是图的一条边。
#
#  老鼠从结点 1 开始并率先出发，猫从结点 2 开始且随后出发，在结点 0 处有一个洞。
#
#  在每个玩家的回合中，他们必须沿着与他们所在位置相吻合的图的一条边移动。例如，如果老鼠位于结点 1，那么它只能移动到 graph[1] 中的（任何）结点去。
#
#
#  此外，猫无法移动到洞（结点 0）里。
#
#  然后，游戏在出现以下三种情形之一时结束：
#
#
#  如果猫和老鼠占据相同的结点，猫获胜。
#  如果老鼠躲入洞里，老鼠获胜。
#  如果某一位置重复出现（即，玩家们的位置和移动顺序都与上一个回合相同），游戏平局。
#
#
#  给定 graph，并假设两个玩家都以最佳状态参与游戏，如果老鼠获胜，则返回 1；如果猫获胜，则返回 2；如果平局，则返回 0。
#
#
#
#
#
#
#  示例：
#
#  输入：[[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
# 输出：0
# 解释：
# 4---3---1
# |   |
# 2---5
#  \ /
#   0
#
#
#
#
#  提示：
#
#
#  3 <= graph.length <= 200
#  保证 graph[1] 非空。
#  保证 graph[2] 包含非零元素。
#
#  Related Topics 广度优先搜索 极小化极大
#  👍 83 👎 0

from typing import List
import collections


# 极大极小算法 博弈 深度优先搜索
# 寻找必胜策略，如果无法必胜，那么返回平局
# node--m.loc,cat.loc,turn
class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        mouse, cat, draw = 1, 2, 0
        pq = collections.deque([])  # 存储节点值和标记值
        colors = collections.defaultdict(int)  # 颜色
        n = len(graph)
        # for i in range(n):  # 将初始节点入队
        #     for j in range(n):
        #         for t in range(1, 3):
        #             if i == 0:
        #                 colors[i, j, t] = mouse
        #                 pq.append((i, j, t, mouse))
        #             elif i == j:
        #                 colors[i, j, t] = cat
        #                 pq.append((i, j, t, cat))
        for i in range(n):
            for t in range(1, 3):
                colors[0, i, t] = mouse
                pq.append((0, i, t, mouse))
                if i != 0:
                    colors[i, i, t] = cat
                    pq.append((i, i, t, cat))

        def parent(i, j, t):  # mouse,cat,turn 定义邻接节点
            if t == 1:  # 本回合是老鼠的回合，那么上回合是猫的回合
                for nxt_j in graph[j]:
                    if nxt_j:
                        yield i, nxt_j, 2
            elif t == 2:  # 本回合是猫的回合，那么上回合是老鼠回合
                for nxt_i in graph[i]:
                    yield nxt_i, j, 1

        degree = collections.defaultdict(int)  # 定义每个节点总共的邻接点数量
        for i in range(n):
            for j in range(n):
                degree[i, j, 1] = len(graph[i])
                degree[i, j, 2] = len(graph[j]) - int(0 in graph[j])

        while pq:
            m_loc, c_loc, turn, color = pq.popleft()
            for nxt_m, nxt_c, nxt_turn in parent(m_loc, c_loc, turn):
                if not colors[nxt_m, nxt_c, nxt_turn]:  # 只对未染色的考虑，这是一个比染色速度的游戏，看哪一个先抢先染色到初始节点
                    if nxt_turn == color:
                        colors[nxt_m, nxt_c, nxt_turn] = color
                        pq.append((nxt_m, nxt_c, nxt_turn, color))
                    else:
                        degree[nxt_m, nxt_c, nxt_turn] -= 1
                        if degree[nxt_m, nxt_c, nxt_turn] == 0:  # 走投无路
                            colors[nxt_m, nxt_c, nxt_turn] = color
                            pq.append((nxt_m, nxt_c, nxt_turn, color))
        return colors[1, 2, 1]


# 黑箱操作
import functools
# https://leetcode-cn.com/problems/cat-and-mouse/solution/python-ji-yi-hua-sou-suo-by-alienjiren/

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        @functools.lru_cache(None)
        def dfs(m, c, t):  # t代表总步数
            if t > 2 * n: return 0
            if m == 0: return 1
            if m == c: return 2
            if t % 2:  # 奇数回合，老鼠动，处于主动状态，选择对自己有利的==1的状态
                if any(dfs(nxt_m, c, t + 1) == 1 for nxt_m in graph[m]):
                    return 1
                elif any(dfs(nxt_m, c, t + 1) == 0 for nxt_m in graph[m]):
                    return 0
                else:
                    return 2
            else:  # 偶数回合，猫动，猫处于主动状态，搜寻对自己有利的==2的状态
                if any(dfs(m, nxt_c, t + 1) == 2 for nxt_c in graph[c] if nxt_c!=0):
                    return 2
                elif any(dfs(m, nxt_c, t + 1) == 0 for nxt_c in graph[c] if nxt_c!=0):
                    return 0
                else:
                    return 1

        return dfs(1, 2, 1)


Solution().catMouseGame([[2, 3], [3, 4], [0, 4], [0, 1], [1, 2]])
