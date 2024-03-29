# -*- coding: utf-8 -*-
# 欢迎各位来到「力扣嘉年华」，接下来将为各位介绍在活动中广受好评的弹珠游戏。
#
# `N*M` 大小的弹珠盘的初始状态信息记录于一维字符串型数组 `plate` 中，数组中的每个元素为仅由 `"O"`、`"W"`、`"E"`、`"."` 组
# 成的字符串。其中：
# - `"O"` 表示弹珠洞（弹珠到达后会落入洞中，并停止前进）；
# - `"W"` 表示逆时针转向器（弹珠经过时方向将逆时针旋转 90 度）；
# - `"E"` 表示顺时针转向器（弹珠经过时方向将顺时针旋转 90 度）；
# - `"."` 表示空白区域（弹珠可通行）。
#
# 游戏规则要求仅能在边缘位置的 **空白区域** 处（弹珠盘的四角除外）沿 **与边缘垂直** 的方向打入弹珠，并且打入后的每颗弹珠最多能 **前进** `
# num` 步。请返回符合上述要求且可以使弹珠最终入洞的所有打入位置。你可以 **按任意顺序** 返回答案。
#
# **注意：**
# - 若弹珠已到达弹珠盘边缘并且仍沿着出界方向继续前进，则将直接出界。
#
# **示例 1：**
#
# > 输入：
# > `num = 4`
# > `plate = ["..E.",".EOW","..W."]`
# >
# > 输出：`[[2,1]]`
# >
# > 解释：
# > 在 `[2,1]` 处打入弹珠，弹珠前进 1 步后遇到转向器，前进方向顺时针旋转 90 度，再前进 1 步进入洞中。
# > ![b054955158a99167b8d51da0e22a54da.gif](https://pic.leetcode-cn.com/16303926
# 49-BoQncz-b054955158a99167b8d51da0e22a54da.gif)
#
# **示例 2：**
#
# > 输入：
# > `num = 5`
# > `plate = [".....","..E..",".WO..","....."]`
# >
# > 输出：`[[0,1],[1,0],[2,4],[3,2]]`
# >
# > 解释：
# > 在 `[0,1]` 处打入弹珠，弹珠前进 2 步，遇到转向器后前进方向逆时针旋转 90 度，再前进 1 步进入洞中。
# > 在 `[1,0]` 处打入弹珠，弹珠前进 2 步，遇到转向器后前进方向顺时针旋转 90 度，再前进 1 步进入洞中。
# > 在 `[2,4]` 处打入弹珠，弹珠前进 2 步后进入洞中。
# > 在 `[3,2]` 处打入弹珠，弹珠前进 1 步后进入洞中。
# > ![b44e9963239ae368badf3d00b7563087.gif](https://pic.leetcode-cn.com/16303926
# 25-rckbdy-b44e9963239ae368badf3d00b7563087.gif)
#
# **示例 3：**
#
# > 输入：
# > `num = 3`
# > `plate = [".....","....O","....O","....."]`
# >
# > 输出：`[]`
# >
# > 解释：
# > 由于弹珠被击中后只能前进 3 步，且不能在弹珠洞和弹珠盘四角打入弹珠，故不存在能让弹珠入洞的打入位置。
#
# **提示：**
# - `1 <= num <= 10^6`
# - `1 <= plate.length, plate[i].length <= 1000`
# - `plate[i][j]` 仅包含 `"O"`、`"W"`、`"E"`、`"."`
#
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 记忆化搜索 数组 动态规划 矩阵
#  👍 11 👎 0

from typing import List
from functools import lru_cache


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def ballGame(self, num: int, plate: List[str]) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        R, C = len(plate), len(plate[0])

        @lru_cache(None)
        def check(r, c, dir, step):
            visted.add((r, c, dir))
            if plate[r][c] == 'O':
                return True
            if plate[r][c] == 'W':
                dir = (dir - 1) % 4
            elif plate[r][c] == 'E':
                dir = (dir + 1) % 4
            nr, nc = r + dirs[dir][0], c + dirs[dir][1]
            if 0 <= nr < R and 0 <= nc < C and step + 1 <= num and (nr, nc, dir) not in visted:
                return check(nr, nc, dir, step + 1)
            return False

        res = []
        for i in range(1, C - 1):
            visted = set()
            if plate[0][i] == '.' and check(0, i, 1, 0):
                res.append([0, i])
            visted = set()
            if plate[R - 1][i] == '.' and check(R - 1, i, 3, 0):
                res.append([R - 1, i])
        for i in range(1, R - 1):
            visted = set()
            if plate[i][0] == '.' and check(i, 0, 0, 0):
                res.append([i, 0])
            visted = set()
            if plate[i][C - 1] == '.' and check(i, C - 1, 2, 0):
                res.append([i, C - 1])
        return sorted(res)


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().ballGame(
    1,
    ["...", ".O."]
))
