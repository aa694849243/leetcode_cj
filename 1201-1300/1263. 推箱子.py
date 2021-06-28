# -*- coding: utf-8 -*-
import collections
import heapq
from typing import List


# 「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。
#
#  游戏地图用大小为 n * m 的网格 grid 表示，其中每个元素可以是墙、地板或者是箱子。
#
#  现在你将作为玩家参与游戏，按规则将箱子 'B' 移动到目标位置 'T' ：
#
#
#  玩家用字符 'S' 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
#  地板用字符 '.' 表示，意味着可以自由行走。
#  墙用字符 '#' 表示，意味着障碍物，不能通行。
#  箱子仅有一个，用字符 'B' 表示。相应地，网格上有一个目标位置 'T'。
#  玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
#  玩家无法越过箱子。
#
#
#  返回将箱子推到目标位置的最小 推动 次数，如果无法做到，请返回 -1。
#
#
#
#  示例 1：
#
#
#
#  输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#              ["#",".",".","B",".","#"],
#              ["#",".","#","#",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：3
# 解释：我们只需要返回推箱子的次数。
#
#  示例 2：
#
#  输入：grid = [["#","#","#","#","#","#"],
#              ["#","T","#","#","#","#"],
#              ["#",".",".","B",".","#"],
#              ["#","#","#","#",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：-1
#
#
#  示例 3：
#
#  输入：grid = [["#","#","#","#","#","#"],
#              ["#","T",".",".","#","#"],
#              ["#",".","#","B",".","#"],
#              ["#",".",".",".",".","#"],
#              ["#",".",".",".","S","#"],
#              ["#","#","#","#","#","#"]]
# 输出：5
# 解释：向下、向左、向左、向上再向上。
#
#
#  示例 4：
#
#  输入：grid = [["#","#","#","#","#","#","#"],
#              ["#","S","#",".","B","T","#"],
#              ["#","#","#","#","#","#","#"]]
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= grid.length <= 20
#  1 <= grid[i].length <= 20
#  grid 仅包含字符 '.', '#', 'S' , 'T', 以及 'B'。
#  grid 中 'S', 'B' 和 'T' 各只能出现一个。
#
#  Related Topics 广度优先搜索
#  👍 58 👎 0


# https://leetcode-cn.com/problems/minimum-moves-to-move-a-box-to-their-target-location/solution/1263-tui-xiang-zi-po-su-de-bfsbfsjiu-ke-yi-tong-gu/
# 1普通bfs
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        g = collections.defaultdict(list)
        R, C = len(grid), len(grid[0]),
        for r in range(R):
            for c in range(C):
                g[grid[r][c]].append(complex(r, c))
        dirs = (1, -1, 1j, -1j)
        pstart, bstart, end, floor = *g['S'], *g['B'], *g['T'], {*g['S'], *g['B'], *g['T'], *g['.']}

        def reachable(s, target, legal):
            if s == target:
                return True
            seen = {s}
            t = [s]
            while True:
                tree = []
                for node in t:
                    for dir in dirs:
                        nxt = node + dir
                        if nxt not in seen and nxt in legal:
                            if nxt == target:
                                return True
                            tree.append(nxt)
                            seen.add(nxt)
                if not tree:
                    break
                t = tree
            return False

        steps = 0
        t = [(pstart, bstart)]
        status = {(pstart, bstart)}  # 状态
        while True:
            tree = []
            for curplayer, curbox in t:
                for dir in dirs:
                    nxtplayer, nxtbox = curbox - dir, curbox + dir
                    if nxtbox in floor and (curbox, nxtbox) not in status and reachable(curplayer, nxtplayer, floor - {curbox}):
                        if nxtbox == end:
                            return steps + 1
                        tree.append((curbox, nxtbox))
                        status.add((curbox, nxtbox))
            if not tree:
                break
            steps += 1
            t = tree
        return -1


# A*搜索
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        g = collections.defaultdict(list)
        R, C = len(grid), len(grid[0]),
        for r in range(R):
            for c in range(C):
                g[grid[r][c]].append(complex(r, c))
        dirs = (1, -1, 1j, -1j)
        pstart, bstart, end, floor = *g['S'], *g['B'], *g['T'], {*g['S'], *g['B'], *g['T'], *g['.']}

        def bestfirst(start, target, legal):
            if start == target:
                return True
            ptime = 1  # 时间戳，先进堆的先考虑
            t = [(abs(start - target), ptime, start)]
            seen = {start}
            while t:
                _, __, curpos = heapq.heappop(t)
                for dir in dirs:
                    nxt = curpos + dir
                    if nxt in legal and nxt not in seen:
                        if nxt == target:
                            return True
                        seen.add(nxt)
                        heapq.heappush(t, (abs(nxt - target), ptime, nxt))  # ptime防止复数比较
                        ptime += 1
            return False

        def f(s, t, steps):
            return abs((s - t).real) + abs((s - t).imag) + steps

        steps = 0
        time = 1  # 防止负数比较
        astarpq = [(f(bstart, end, 0), steps, time, pstart, bstart)]
        status = {(pstart, bstart)}
        while astarpq:
            _, steps, __, curplayer, curbox = heapq.heappop(astarpq)
            for dir in dirs:
                nxtplayer, nxtbox = curbox - dir, curbox + dir
                if nxtbox in floor and (nxtplayer, nxtbox) not in status and bestfirst(curplayer, nxtplayer, floor - {curbox}):
                    if nxtbox == end:
                        return steps + 1
                    status.add((nxtplayer, nxtbox))
                    heapq.heappush(astarpq, (f(nxtbox, end, steps + 1), steps + 1, time, nxtplayer, nxtbox))
                    time += 1
        return -1


# 3tarjan+A*
class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        g = collections.defaultdict(list)
        R, C = len(grid), len(grid[0]),
        for r in range(R):
            for c in range(C):
                g[grid[r][c]].append(complex(r, c))
        dirs = (1, -1, 1j, -1j)
        pstart, bstart, end, floor = *g['S'], *g['B'], *g['T'], {*g['S'], *g['B'], *g['T'], *g['.']}

        def f(s, t, steps):
            return abs((s - t).real) + abs((s - t).imag) + steps

        low = dict.fromkeys(floor, 0)
        dfn = low.copy()
        timestamp = 0
        index = {}

        def tarjan(cur, parent):  # 计算全部点的时间戳
            nonlocal timestamp
            timestamp += 1
            dfn[cur] = low[cur] = timestamp
            index[timestamp] = cur  # 时间戳索引着第一个该时间访问的节点
            for dir in dirs:
                nxt = cur + dir
                if nxt != parent and nxt in floor:
                    if not low[nxt]:  # 没有访问过
                        tarjan(nxt, cur)
                    low[cur] = min(low[cur], low[nxt])

        tarjan(bstart, -1)  # 全部节点都在第一象限，-1作为初始节点的父节点没问题
        # 割点两侧转换为不同的连通分量,割点，割点左边，割点右边转换为三个连通分量
        for cur in floor:  # 如果low[cur]==dfn[cur]说明该节点只有一条通路，该节点如果有子节点，那么该节点一定是割点
            connect = [cur]
            while dfn[connect[-1]] != low[connect[-1]]:  # 非单向通路
                connect.append(index[low[connect[-1]]])
            for node in connect:
                low[node] = low[connect[-1]]
        steps = 0
        time = 1
        status = {(pstart, bstart)}
        astarpq = [(f(bstart, end, 0), steps, time, pstart, bstart)]
        while astarpq:
            _, steps, __, curplayer, curbox = heapq.heappop(astarpq)
            for dir in dirs:
                nxtplayer, nxtbox = curbox - dir, curbox + dir
                if nxtbox in floor and nxtplayer in floor and (curbox, nxtbox) not in status and low[curplayer] == low[
                    nxtplayer]:  # 保证属于curplayer和nxtplayer属于同一连通分量
                    if nxtbox == end:
                        return steps + 1
                    status.add((curbox, nxtbox))
                    heapq.heappush(astarpq, (f(nxtbox, end, steps + 1), steps + 1, time, curbox, nxtbox))
                    time += 1
        return -1


Solution().minPushBox(grid = [["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"], ["#",".",".",".",".",".",".",".",".",".",".",".","#","#","#","#","#","#","#","#"], ["#",".",".",".","#","#",".","#","#","#","#",".","#","#","#",".","#","#","T","#"], ["#",".",".",".",".",".",".","#",".","#",".",".","#","#","#",".","#","#",".","#"], ["#",".",".",".","#",".",".",".",".",".",".",".","#","#","#",".","#","#",".","#"], ["#",".","#",".",".",".",".",".",".",".",".",".","#","#","#",".","#","#",".","#"], ["#",".","#",".","#","#","#","#","#","#","#",".","#","#","#",".","#","#",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","S",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".","B",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","#",".",".","#"], ["#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#","#"]])