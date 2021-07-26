# -*- coding: utf-8 -*-
# 我们得到了一副藏宝图，藏宝图显示，在一个迷宫中存在着未被世人发现的宝藏。
#
#  迷宫是一个二维矩阵，用一个字符串数组表示。它标识了唯一的入口（用 'S' 表示），和唯一的宝藏地点（用 'T' 表示）。但是，宝藏被一些隐蔽的机关保护了起
# 来。在地图上有若干个机关点（用 'M' 表示），只有所有机关均被触发，才可以拿到宝藏。
#
#  要保持机关的触发，需要把一个重石放在上面。迷宫中有若干个石堆（用 'O' 表示），每个石堆都有无限个足够触发机关的重石。但是由于石头太重，我们一次只能搬一
# 个石头到指定地点。
#
#  迷宫中同样有一些墙壁（用 '#' 表示），我们不能走入墙壁。剩余的都是可随意通行的点（用 '.' 表示）。石堆、机关、起点和终点（无论是否能拿到宝藏）也是
# 可以通行的。
#
#  我们每步可以选择向上/向下/向左/向右移动一格，并且不能移出迷宫。搬起石头和放下石头不算步数。那么，从起点开始，我们最少需要多少步才能最后拿到宝藏呢？如果
# 无法拿到宝藏，返回 -1 。
#
#  示例 1：
#
#
#  输入： ["S#O", "M..", "M.T"]
#
#  输出：16
#
#  解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3,
# 我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。
#
#
#
#  示例 2：
#
#
#  输入： ["S#O", "M.#", "M.T"]
#
#  输出：-1
#
#  解释：我们无法搬到石头触发机关
#
#
#  示例 3：
#
#
#  输入： ["S#O", "M.T", "M.."]
#
#  输出：17
#
#  解释：注意终点也是可以通行的。
#
#
#  限制：
#
#
#  1 <= maze.length <= 100
#  1 <= maze[i].length <= 100
#  maze[i].length == maze[j].length
#  S 和 T 有且只有一个
#  0 <= M的数量 <= 16
#  0 <= O的数量 <= 40，题目保证当迷宫中存在 M 时，一定存在至少一个 O 。
#
#  Related Topics 位运算 广度优先搜索 数组 动态规划 状态压缩 矩阵
#  👍 160 👎 0
from queue import Queue
from typing import List


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        R, C = len(maze), len(maze[0])

        def cal(r, c):  # 计算r,c点到其他点的最短距离
            q = Queue()
            dist = [[float('inf')] * C for _ in range(R)]
            dist[r][c] = 0
            q.put((r, c))
            while q.qsize():
                r, c = q.get()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and dist[nr][nc] == float('inf') and maze[nr][nc] != '#':
                        dist[nr][nc] = dist[r][c] + 1
                        q.put((nr, nc))
            return dist

        sr, sc = -1, -1
        tr, tc = -1, -1
        stones, buttons = [], []
        for r in range(R):
            for c in range(C):
                if maze[r][c] == 'S':
                    sr, sc = r, c
                elif maze[r][c] == 'T':
                    tr, tc = r, c
                elif maze[r][c] == 'O':
                    stones.append((r, c))
                elif maze[r][c] == 'M':
                    buttons.append((r, c))
        n = len(buttons)
        starttopos = cal(sr, sc)  # 起点到其他点的距离
        if n == 0:
            return starttopos[tr][tc] if starttopos[tr][tc] != float('inf') else -1
        dist = [[float('inf')] * (n + 2) for _ in range(n)]  # dist[i][n]代表到起点的距离, dist[i][n+1]代表到终点的距离
        mdists = []  # 储存每个机关到其他地方的距离矩阵
        for i, (r, c) in enumerate(buttons):
            mdist = cal(r, c)
            mdists.append(mdist)
            # dist[i][n]=mdist[sr][sc]
            dist[i][n + 1] = mdist[tr][tc]  # 储存到终点的距离
        ns = len(stones)
        for i, (r, c) in enumerate(buttons):
            for j, (sx, sy) in enumerate(stones):  # 石头作为中转站，起点-石头-机关
                dist[i][n] = min(dist[i][n], mdists[i][sx][sy] + starttopos[sx][sy])
                for k, (nr, nc) in enumerate(buttons):  # 每个石头作为中转站，机关-石头-机关
                    if k == i:
                        continue
                    d = min(dist[i][k], mdists[i][sx][sy] + mdists[k][sx][sy])
                    dist[i][k] = d
                    dist[k][i] = d
        for i, (r, c) in enumerate(buttons):
            if dist[i][n] == float('inf') or dist[i][n + 1] == float('inf'):
                return -1  # 因为图都是连通的，所以如果某个机关无法到达到达起点或者无法到达终点说明这个机关与起点或终点不连通，也即与其他机关不连通，则直接返回-1
        dp = [[float('inf')] * n for _ in range(1 << n)]
        for i, (r, c) in enumerate(buttons):  # 初始状态
            dp[1 << i][i] = dist[i][n]
        for mask in range(1, 1 << n):
            for i in range(n):
                if mask & (1 << i):
                    for j in range(n):
                        if mask & (1 << j) == 0:
                            dp[mask | (1 << j)][j] = min(dp[mask | (1 << j)][j], dp[mask][i] + dist[i][j])
        # 最后从机关到达终点
        ans = float('inf')
        fmask = (1 << n) - 1
        for i in range(n):
            ans = min(ans, dp[fmask][i] + dist[i][n + 1])
        return ans if ans != float('inf') else -1


# 复写
class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        dirs = [(0, 1,), (0, -1), (1, 0), (-1, 0)]
        R, C = len(maze), len(maze[0])

        def cal(r, c):
            dist = [[float('inf')] * C for _ in range(R)]
            q = Queue()
            q.put((r, c))
            dist[r][c] = 0
            while q.qsize():
                r, c = q.get()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and maze[nr][nc] != '#' and dist[nr][nc] == float('inf'):
                        q.put((nr, nc))
                        dist[nr][nc] = dist[r][c] + 1
            return dist
        sr,sc,tr,tc=-1,-1,-1,-1
        stones,buttons=[],[]
        for r in range(R):
            for c in range(C):
                a=maze[r][c]
                if a=='S':
                    sr,sc=r,c
                elif a=='T':
                    tr,tc=r,c
                elif a=='O':
                    stones.append((r,c))
                elif a=='M':
                    buttons.append((r,c))
        starttopos=cal(sr,sc)
        n=len(buttons)
        if not n:
            return starttopos[tr][tc] if starttopos[tr][tc]!=float('inf') else -1
        mdists=[]
        dist=[[float('inf')]*(n+2) for _ in range(n)]
        for i,(r,c) in enumerate(buttons):
            mdist=cal(r,c)
            mdists.append(mdist)
            dist[i][n+1]=mdist[tr][tc]
        for i,(r,c) in enumerate(buttons):
            for j,(sx,sy) in enumerate(stones):
                dist[i][n]=min(dist[i][n],mdists[i][sx][sy]+starttopos[sx][sy])
                for k,(nr,nc) in enumerate(buttons):
                    if k==i:
                        continue
                    a=min(mdists[i][sx][sy]+mdists[k][sx][sy],dist[i][k])
                    dist[i][k],dist[k][i]=a,a
        for i in range(n):
            if dist[i][n]==float('inf') or dist[i][n+1]==float('inf'):
                return -1
        dp=[[float('inf')]*n for _ in range(1<<n)]
        for i in range(n):
            dp[1<<i][i]=dist[i][n]
        for mask in range(1,1<<n):
            for i in range(n):
                if mask&(1<<i):
                    for j in range(n):
                        if mask &(1<<j)==0:
                            dp[mask|(1<<j)][j]=min(dp[mask|(1<<j)][j],dp[mask][i]+dist[i][j])
        fmask=(1<<n)-1
        ans=float('inf')
        for i in range(n):
            ans=min(ans,dp[fmask][i]+dist[i][n+1])
        return ans if ans!=float('inf') else -1



Solution().minimalSteps(["S#O", "M..", "M.T"])
