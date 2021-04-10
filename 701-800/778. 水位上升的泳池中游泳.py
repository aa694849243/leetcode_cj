'''在一个 N x N 的坐标方格 grid 中，每一个方格的值 grid[i][j] 表示在位置 (i,j) 的平台高度。

现在开始下雨了。当时间为 t 时，此时雨水导致水池中任意位置的水位为 t 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 (0，0) 出发。最少耗时多久你才能到达坐标方格的右下平台 (N-1, N-1)？

 

示例 1:

输入: [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。

等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置
示例2:

输入: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的
 

提示:

2 <= N <= 50.
grid[i][j] 是 [0, ..., N*N - 1] 的排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swim-in-rising-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import itertools


# 1二分+深度优先搜索
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        r = max(itertools.chain(*grid)) + 1
        l = min(itertools.chain(*grid))
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(num, i, j):
            if grid[i][j] > num:
                return False
            m.add((i, j))
            if (i, j) == (R - 1, C - 1):
                return True
            for r, c in [(i + dir[x][0], j + dir[x][1]) for x in range(4)]:
                if 0 <= r < R and 0 <= c < C and grid[r][c] <= num and (r, c) not in m:
                    if dfs(num, r, c):
                        return True

        while l < r:
            m = set()
            mid = (l + r) // 2
            if not dfs(mid, 0, 0):
                l = mid + 1
            else:
                r = mid
        return l


# 2bfs+二分
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        r = max(itertools.chain(*grid)) + 1
        l = min(itertools.chain(*grid))
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(num):
            if grid[0][0] > num:
                return False
            t = [(0, 0)]
            while True:
                tree = []
                for i, j in t:
                    for r, c in [(i + dir[x][0], j + dir[x][1]) for x in range(4)]:
                        if (r, c) not in m and 0 <= r < R and 0 <= c < C and grid[r][c] <= num:
                            if (r, c) == (R - 1, C - 1):
                                return True
                            m.add((r, c))
                            tree.append((r, c))
                if not tree:
                    break
                t = tree
            return False

        while l < r:
            mid = (l + r) // 2
            m = {(0, 0)}
            if not bfs(mid):
                l = mid + 1
            else:
                r = mid
        return l


# 3bfs+堆
import heapq


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0
        a = []
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = {(0, 0)}
        heapq.heappush(a, (grid[0][0], 0, 0))
        while a:
            w, i, j = heapq.heappop(a)
            ans = max(ans, w)
            if (i, j) == (R - 1, C - 1):
                return ans
            m.add((i, j))
            for r, c in [(i + dir[x][0], j + dir[x][1]) for x in range(4)]:
                if (r, c) not in m and 0 <= r < R and 0 <= c < C:
                    heapq.heappush(a, (grid[r][c], r, c))


# 3并查集
import collections


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        m = collections.defaultdict(int)
        f = {}
        for i in range(R):
            for j in range(C):
                m[grid[i][j]] = (i, j)

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(y)] = find(x)

        for time in range(R * C):
            i, j = m[time]
            for r, c in ((i + dir[x][0], j + dir[x][1]) for x in range(4)):
                if 0 <= r < R and 0 <= c < C and grid[r][c] < time:
                    union(i * C + j, r * C + c)
            if find(0) == find(R * C - 1):
                return time


# 5dijkstra
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        out_edges = collections.defaultdict(list)
        for i in range(R):
            for j in range(C):
                for r, c in ((i + dir[x][0], j + dir[x][1]) for x in range(4)):
                    if 0 <= r < R and 0 <= c < C:
                        out_edges[(i, j)].append((grid[r][c], r, c))
        q = []
        ans = 0
        heapq.heappush(q, (grid[0][0], 0, 0))
        m = set()
        while q:
            w, i, j = heapq.heappop(q)
            ans = max(w, ans)
            m.add((i, j))
            if (i, j) == (R - 1, C - 1):
                return ans
            for cost, r, c in out_edges[(i, j)]:
                if (r, c) not in m:
                    heapq.heappush(q, (cost, r, c))


Solution().swimInWater([[0, 2], [1, 3]])
