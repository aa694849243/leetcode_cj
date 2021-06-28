# -*- coding: utf-8 -*-
import collections
from typing import List


# 这里有一幅服务器分布图，服务器的位置标识在 m * n 的整数矩阵网格 grid 中，1 表示单元格上有服务器，0 表示没有。
#
#  如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。
#
#  请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。
#
#
#
#  示例 1：
#
#
#
#  输入：grid = [[1,0],[0,1]]
# 输出：0
# 解释：没有一台服务器能与其他服务器进行通信。
#
#  示例 2：
#
#
#
#  输入：grid = [[1,0],[1,1]]
# 输出：3
# 解释：所有这些服务器都至少可以与一台别的服务器进行通信。
#
#
#  示例 3：
#
#
#
#  输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# 输出：4
# 解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m <= 250
#  1 <= n <= 250
#  grid[i][j] == 0 or 1
#
#  Related Topics 图 数组
#  👍 37 👎 0


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        mr = collections.defaultdict(int)
        mc = collections.defaultdict(int)
        for i,row in enumerate(grid):
            mr[i]=sum(row)
        for i,col in enumerate(zip(*grid)):
            mc[i]=sum(col)
        ans=0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1 and  (mr[r]>1 or mc[c]>1):
                    ans+=1
        return ans
