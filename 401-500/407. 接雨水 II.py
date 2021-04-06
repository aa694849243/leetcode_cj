'''给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

 

示例：

给出如下 3x6 的高度图:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

返回 4 。


如上图所示，这是下雨前的高度图[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]] 的状态。

 



下雨后，雨水将会被存储在这些方块中。总的接雨水量是4。

 

提示：

1 <= m, n <= 110
0 <= heightMap[i][j] <= 20000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import heapq


# 小顶堆
# https://leetcode-cn.com/problems/trapping-rain-water-ii/solution/xiao-ding-dui-by-lucifertian/
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]: return 0
        visted = set()
        heap = []
        cols = len(heightMap[0])
        rows = len(heightMap)
        ans = 0
        i_max = float('-inf')
        for i in range(cols):  # 第一行和最后一行入堆
            heapq.heappush(heap, [heightMap[0][i], (0, i)])
            heapq.heappush(heap, [heightMap[rows - 1][i], (rows - 1, i)])
            visted.add((0, i))
            visted.add((rows - 1, i))
        for i in range(1, rows - 1):  # 第一列和最后一列入堆
            heapq.heappush(heap, [heightMap[i][0], (i, 0)])
            heapq.heappush(heap, [heightMap[i][cols - 1], (i, cols - 1)])
            visted.add((i, 0))
            visted.add((i, cols - 1))
        while heap:
            ix, coordinate = heapq.heappop(heap)
            i_max = max(ix, i_max)
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dir in dirs:
                if coordinate[0] + dir[0] < 0 or coordinate[0] + dir[0] >= rows or coordinate[1] + dir[1] < 0 or \
                        coordinate[1] + dir[1] >= cols or (coordinate[0] + dir[0], coordinate[1] + dir[1]) in visted:
                    continue
                visted.add((coordinate[0] + dir[0], coordinate[1] + dir[1]))
                if heightMap[coordinate[0] + dir[0]][coordinate[1] + dir[1]] < i_max:
                    ans += i_max - heightMap[coordinate[0] + dir[0]][coordinate[1] + dir[1]]
                heapq.heappush(heap, [heightMap[coordinate[0] + dir[0]][coordinate[1] + dir[1]],
                                      (coordinate[0] + dir[0], coordinate[1] + dir[1])])
        return ans


a = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
Solution().trapRainWater(a)
