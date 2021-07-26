# -*- coding: utf-8 -*-
import functools
from typing import List


# 某解密游戏中，有一个 N\*M 的迷宫，迷宫地形会随时间变化而改变，迷宫出口一直位于 `(n-1,m-1)` 位置。迷宫变化规律记录于 `maze` 中，`
# maze[i]` 表示 `i` 时刻迷宫的地形状态，`"."` 表示可通行空地，`"#"` 表示陷阱。
#
# 地形图初始状态记作 `maze[0]`，此时小力位于起点 `(0,0)`。此后每一时刻可选择往上、下、左、右其一方向走一步，或者停留在原地。
#
# 小力背包有以下两个魔法卷轴（卷轴使用一次后消失）：
# + 临时消除术：将指定位置在下一个时刻变为空地；
# + 永久消除术：将指定位置永久变为空地。
#
# 请判断在迷宫变化结束前（含最后时刻），小力能否在不经过任意陷阱的情况下到达迷宫出口呢？
#
# **注意： 输入数据保证起点和终点在所有时刻均为空地。**
#
# **示例 1：**
# >输入：`maze = [[".#.","#.."],["...",".#."],[".##",".#."],["..#",".#."]]`
# >
# >输出：`true`
# >
# >解释：
# ![maze.gif](https://pic.leetcode-cn.com/1615892239-SCIjyf-maze.gif)
#
#
# **示例 2：**
# >输入：`maze = [[".#.","..."],["...","..."]]`
# >
# >输出：`false`
# >
# >解释：由于时间不够，小力无法到达终点逃出迷宫。
#
# **示例 3：**
# >输入：`maze = [["...","...","..."],[".##","###","##."],[".##","###","##."],[".##
# ","###","##."],[".##","###","##."],[".##","###","##."],[".##","###","##."]]`
# >
# >输出：`false`
# >
# >解释：由于道路不通，小力无法到达终点逃出迷宫。
#
# **提示：**
# - `1 <= maze.length <= 100`
# - `1 <= maze[i].length, maze[i][j].length <= 50`
# - `maze[i][j]` 仅包含 `"."`、`"#"` Related Topics 深度优先搜索 广度优先搜索 数组 动态规划 矩阵
#  👍 20 👎 0


class Solution:
    def escapeMaze(self, maze: List[List[str]]) -> bool:
        dtime = len(maze) - 1
        R, C = len(maze[0]), len(maze[0][0])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]

        @functools.lru_cache(None)
        def dp(r, c, tmp, perm, time):
            if time > dtime:
                return False
            if time == dtime:
                return (r, c) == (R - 1, C - 1)
            if (r, c) == (R - 1, C - 1):
                return True
            matrix = maze[time + 1]
            ans = False
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C:
                    if matrix[nr][nc] == '.':
                        ans = dp(nr, nc, tmp, perm=1 if perm == 1 else 0, time=time + 1)
                    if ans: #每一步都判断下，返回true了就直接终止，不要浪费时间
                        return True
                    if tmp:  # 临时符还没用
                        ans = dp(nr, nc, tmp - 1, perm=1 if perm == 1 else 0, time=time + 1)
                    if ans:
                        return True
                    if perm == 1:  # 对下一个地点使用永久符
                        ans = dp(nr, nc, tmp, 2, time + 1)
                    if ans:
                        return True
            if perm == 2 or maze[time + 1][r][c] == '.':  # 该处拥有永久魔法
                ans = dp(r, c, tmp, perm, time + 1)
            elif perm == 1 and maze[time + 1][r][c] == '#':  # 对该处使用永久魔法
                ans = dp(r, c, tmp, 2, time + 1)
            if ans:
                return True
            if tmp and maze[time+1][r][c] == '#':  # 对该处使用临时魔法
                ans = dp(r, c, tmp-1, perm=1 if perm == 1 else 0, time=time+1)
            return ans

        return dp(0,0,1,1,0)
Solution().escapeMaze([[".##..####",".#######."],["..######.","########."],[".#####.##",".#######."],[".######.#","####.###."],[".##.##..#",".#.#####."],[".###.####","##.#..##."],[".########","#######.."],[".#####.##","#.######."],[".########","###..#.#."],[".####.#.#","###..##.."],[".######.#","########."]])