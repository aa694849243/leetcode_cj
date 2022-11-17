# -*- coding: utf-8 -*-
# 给你一个 m x n 的二进制矩阵 grid ，每个格子要么为 0 （空）要么为 1 （被占据）。
#
#  给你邮票的尺寸为 stampHeight x stampWidth 。我们想将邮票贴进二进制矩阵中，且满足以下 限制 和 要求 ：
#
#
#  覆盖所有 空 格子。
#  不覆盖任何 被占据 的格子。
#  我们可以放入任意数目的邮票。
#  邮票可以相互有 重叠 部分。
#  邮票不允许 旋转 。
#  邮票必须完全在矩阵 内 。
#
#
#  如果在满足上述要求的前提下，可以放入邮票，请返回 true ，否则返回 false 。
#
#
#
#  示例 1：
#
#
#
#  输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight =
# 4, stampWidth = 3
# 输出：true
# 解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。
#
#
#  示例 2：
#
#
#
#  输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2,
# stampWidth = 2
# 输出：false
# 解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[r].length
#  1 <= m, n <= 10⁵
#  1 <= m * n <= 2 * 10⁵
#  grid[r][c] 要么是 0 ，要么是 1 。
#  1 <= stampHeight, stampWidth <= 10⁵
#
#
#  Related Topics 贪心 数组 矩阵 前缀和
#  👍 38 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# 二维前缀和 二维差分
class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        R, C = len(grid), len(grid[0])
        precum = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                precum[r + 1][c + 1] = precum[r][c + 1] + precum[r + 1][c] - precum[r][c] + grid[r][c]
        diff_grid = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                nr, nc = r + stampHeight, c + stampWidth
                if nr <= R and nc <= C and precum[nr][nc] - precum[nr][c] - precum[r][nc] + precum[r][c] == 0:  # 从(r,c)到(nr-1,nc-1)的矩形区域内全是0
                    diff_grid[r][c] += 1
                    diff_grid[r][nc] -= 1
                    diff_grid[nr][c] -= 1
                    diff_grid[nr][nc] += 1
        cnt, pre = [0] * (C + 1), [0] * (C + 1)
        for r in range(R):
            for c in range(C):
                cnt[c + 1] = cnt[c] + diff_grid[r][c] + pre[c + 1] - pre[c]  # 横排累加和+纵排累加,pre[c+1]-pre[c]为纵排累加
                if cnt[c + 1] == 0 and grid[r][c] == 0:
                    return False
            pre = cnt[:]
        return True


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().possibleToStamp([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]], 2, 2))
