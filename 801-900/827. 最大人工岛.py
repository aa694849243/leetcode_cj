'''在二维地图上， 0代表海洋， 1代表陆地，我们最多只能将一格 0 海洋变成 1变成陆地。

进行填海之后，地图上最大的岛屿面积是多少？（上、下、左、右四个方向相连的 1 可形成岛屿）

示例 1:

输入: [[1, 0], [0, 1]]
输出: 3
解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
示例 2:

输入: [[1, 1], [1, 0]]
输出: 4
解释: 将一格0变成1，岛屿的面积扩大为 4。
示例 3:

输入: [[1, 1], [1, 1]]
输出: 4
解释: 没有0可以让我们变成1，面积依然为 4。
说明:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/making-a-large-island
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        size = collections.defaultdict(lambda: 1)
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a == b:
                return
            f[b] = a
            size[a] += size[b]

        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    size[i*C+j]
                    if j - 1 >= 0 and grid[i][j - 1] == 1:
                        union(i * C + j - 1, i * C + j)
                    if i - 1 >= 0 and grid[i - 1][j] == 1:
                        union((i - 1) * C + j, i * C + j)
        ans = max(size.values()) if size else 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    m = set()
                    x = 0
                    for r_, c_ in dirs:
                        new_r, new_c = i + r_, j + c_
                        if 0 <= new_c < C and 0 <= new_r < R and grid[new_r][new_c] == 1:
                            m.add(find(new_r * C + new_c))
                    for a in m:
                        x += size[a]
                    ans = max(x + 1, ans)
        return ans


Solution().largestIsland([[0, 0], [0, 0]])
