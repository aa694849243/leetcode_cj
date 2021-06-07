# -*- coding: utf-8 -*-
import collections
from typing import List


# 在一个 106 x 106 的网格中，每个网格上方格的坐标为 (x, y) 。
#
#  现在从源方格 source = [sx, sy] 开始出发，意图赶往目标方格 target = [tx, ty] 。数组 blocked 是封锁的方格列表
# ，其中每个 blocked[i] = [xi, yi] 表示坐标为 (xi, yi) 的方格是禁止通行的。
#
#  每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 不 在给出的封锁列表 blocked 上。同时，不允许走出网格。
#
#  只有在可以通过一系列的移动从源方格 source 到达目标方格 target 时才返回 true。否则，返回 false。
#
#
#
#  示例 1：
#
#
# 输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
# 输出：false
# 解释：
# 从源方格无法到达目标方格，因为我们无法在网格中移动。
# 无法向北或者向东移动是因为方格禁止通行。
# 无法向南或者向西移动是因为不能走出网格。
#
#  示例 2：
#
#
# 输入：blocked = [], source = [0,0], target = [999999,999999]
# 输出：true
# 解释：
# 因为没有方格被封锁，所以一定可以到达目标方格。
#
#
#
#
#  提示：
#
#
#  0 <= blocked.length <= 200
#  blocked[i].length == 2
#  0 <= xi, yi < 106
#  source.length == target.length == 2
#  0 <= sx, sy, tx, ty < 106
#  source != target
#  题目数据保证 source 和 target 不在封锁列表内
#
#  Related Topics 广度优先搜索
#  👍 49 👎 0

# https://leetcode-cn.com/problems/escape-a-large-maze/solution/bfsjia-ti-qian-tui-chu-by-black_six-xt3v/
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = list(map(tuple, blocked))
        n = len(blocked)
        limit = n * (n - 1) // 2

        def bfs(source, tar):
            m = collections.deque([source])
            visted = {source}
            while m:
                r, c = m.popleft()
                for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= nr < 10 ** 6 and 0 <= nc < 10 ** 6 and (nr, nc) not in blocked and (nr, nc) not in visted:
                        if (nr, nc) == tar:
                            return True
                        visted.add((nr, nc))
                        if len(visted) > limit:
                            return True
                        m.append((nr, nc))
            return False

        return bfs(tuple(source), tuple(target)) and bfs(tuple(target), tuple(source))
