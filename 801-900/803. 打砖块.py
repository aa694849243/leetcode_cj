'''有一个 m x n 的二元网格，其中 1 表示砖块，0 表示空白。砖块 稳定（不会掉落）的前提是：

一块砖直接连接到网格的顶部，或者
至少有一块相邻（4 个方向之一）砖块 稳定 不会掉落时
给你一个数组 hits ，这是需要依次消除砖块的位置。每当消除 hits[i] = (rowi, coli) 位置上的砖块时，对应位置的砖块（若存在）会消失，然后其他的砖块可能因为这一消除操作而掉落。一旦砖块掉落，它会立即从网格中消失（即，它不会落在其他稳定的砖块上）。

返回一个数组 result ，其中 result[i] 表示第 i 次消除操作对应掉落的砖块数目。

注意，消除可能指向是没有砖块的空白位置，如果发生这种情况，则没有砖块掉落。

 

示例 1：

输入：grid = [[1,0,0,0],[1,1,1,0]], hits = [[1,0]]
输出：[2]
解释：
网格开始为：
[[1,0,0,0]，
 [1,1,1,0]]
消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0]
 [0,1,1,0]]
两个加粗的砖不再稳定，因为它们不再与顶部相连，也不再与另一个稳定的砖相邻，因此它们将掉落。得到网格：
[[1,0,0,0],
 [0,0,0,0]]
因此，结果为 [2] 。
示例 2：

输入：grid = [[1,0,0,0],[1,1,0,0]], hits = [[1,1],[1,0]]
输出：[0,0]
解释：
网格开始为：
[[1,0,0,0],
 [1,1,0,0]]
消除 (1,1) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [1,0,0,0]]
剩下的砖都很稳定，所以不会掉落。网格保持不变：
[[1,0,0,0],
 [1,0,0,0]]
接下来消除 (1,0) 处加粗的砖块，得到网格：
[[1,0,0,0],
 [0,0,0,0]]
剩下的砖块仍然是稳定的，所以不会有砖块掉落。
因此，结果为 [0,0] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/bricks-falling-when-hit
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List

import collections
import copy


class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        orgin = 40001
        f = {}
        size = collections.defaultdict(lambda: 1)
        gcopy = copy.deepcopy(grid)

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

        for i, j in hits:
            grid[i][j] = 0
        R, C = len(grid), len(grid[0])
        for i in range(R):
            for j in range(C):
                if i == 0 and grid[i][j] == 1:
                    union(orgin, i * C + j)
                else:
                    if grid[i][j] == 1:
                        if grid[i - 1][j] == 1:
                            if find((i - 1) * C + j) == orgin:
                                union(orgin, i * C + j)
                            else:
                                union(i * C + j, (i - 1) * C + j)
                        if j - 1 >= 0 and grid[i][j - 1] == 1:
                            if find(i * C + j - 1) == orgin:
                                union(orgin, i * C + j)
                            else:
                                union(i * C + j, i * C + j - 1)
        dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = []

        for i, j in hits[::-1]:
            if gcopy[i][j] == 0:
                ans.append(0)
                continue
            grid[i][j] = 1
            a = size[orgin]
            if i == 0:
                union(orgin, i * C + j)
            for r_, c_ in dir:
                new_r, new_c = i + r_, j + c_
                if 0 <= new_r < R and 0 <= new_c < C and grid[new_r][new_c] == 1:
                    if find(new_r * C + new_c) == orgin:
                        union(new_r * C + new_c, i * C + j)
                    else:
                        union(i * C + j, new_r * C + new_c)
            b = size[40001]
            ans.append(max(0, b - a - 1))
        return ans[::-1]


print(Solution().hitBricks(grid=[[1, 0, 0, 0], [1, 1, 0, 0]], hits=[[1, 1], [1, 0]]))
...
