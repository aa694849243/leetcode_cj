# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。
#
#
#
#  示例 1:
#
#
#
#
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
#
#
#  示例 2:
#
#
#
#
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
#
#
#
#
#  提示:
#
#
#  m == heightMap.length
#  n == heightMap[i].length
#  1 <= m, n <= 200
#  0 <= heightMap[i][j] <= 2 * 10⁴
#
#
#
#
#  Related Topics 广度优先搜索 数组 矩阵 堆（优先队列）
#  👍 686 👎 0
from typing import List
import heapq


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        R, C = len(heightMap), len(heightMap[0])
        visted = [[0] * C for _ in range(R)]
        hp = []
        for r in range(R):
            for c in range(C):
                if r == 0 or r == R - 1 or c == 0 or c == C - 1:
                    visted[r][c] = 1
                    heapq.heappush(hp, (heightMap[r][c], r, c))
        mx = -1
        ans = 0
        while hp:
            h, r, c = heapq.heappop(hp)
            mx = max(mx, h)
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C and not visted[nr][nc]:
                    heapq.heappush(hp, (heightMap[nr][nc], nr, nc))
                    ans += max(0, mx - heightMap[nr][nc])
                    visted[nr][nc] = 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().trapRainWater(
        [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]])
)
