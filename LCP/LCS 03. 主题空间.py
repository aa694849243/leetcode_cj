# -*- coding: utf-8 -*-
import collections
from typing import List


# 「以扣会友」线下活动所在场地由若干主题空间与走廊组成，场地的地图记作由一维字符串型数组 `grid`，字符串中仅包含 `"0"～"5"` 这 6 个字符。地
# 图上每一个字符代表面积为 1 的区域，其中 `"0"` 表示走廊，其他字符表示主题空间。相同且连续（连续指上、下、左、右四个方向连接）的字符组成同一个主题空间。
#
#
# 假如整个 `grid` 区域的外侧均为走廊。请问，不与走廊直接相邻的主题空间的最大面积是多少？如果不存在这样的空间请返回 `0`。
#
# **示例 1:**
# >输入：`grid = ["110","231","221"]`
# >
# >输出：`1`
# >
# >解释：4 个主题空间中，只有 1 个不与走廊相邻，面积为 1。
# >![image.png](https://pic.leetcode-cn.com/1613708145-rscctN-image.png)
#
#
# **示例 2:**
# >输入：`grid = ["11111100000","21243101111","21224101221","11111101111"]`
# >
# >输出：`3`
# >
# >解释：8 个主题空间中，有 5 个不与走廊相邻，面积分别为 3、1、1、1、2，最大面积为 3。
# >![image.png](https://pic.leetcode-cn.com/1613707985-KJyiXJ-image.png)
#
#
# **提示：**
# - `1 <= grid.length <= 500`
# - `1 <= grid[i].length <= 500`
# - `grid[i][j]` 仅可能是 `"0"～"5"`
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 4 👎 0

#并查集 带数量
class Solution:
    def largestArea(self, grid: List[str]) -> int:
        f = {}
        size = collections.defaultdict(lambda: 1)

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            a = find(x)
            b = find(y)
            if a != b:
                f[b] = a
                size[a] += size[b]

        R, C = len(grid), len(grid[0])
        m = {}

        def cal(r, c):
            if (r, c) in m:
                return m[r, c]
            return C * r + c

        for r in range(R):
            for c in range(C):
                num = cal(r, c)
                if r == 0 or c == 0 or r == R - 1 or c == C - 1 or grid[r][c] == '0':
                    union(-1, num)
                nr, nc = r - 1, c
                if 0 <= nr < R and 0 <= nc < C and (grid[nr][nc] == grid[r][c] or grid[nr][nc] == '0' or grid[r][c]=='0'):
                    nnum = cal(nr, nc)
                    if find(nnum) == -1:
                        union(nnum, num)
                    else:
                        union(num, nnum)
                nr, nc = r, c - 1
                if 0 <= nr < R and 0 <= nc < C and (grid[nr][nc] == grid[r][c] or grid[nr][nc] == '0' or grid[r][c]=='0'):
                    nnum = cal(nr, nc)
                    if find(nnum) == -1:
                        union(nnum, num)
                    else:
                        union(num, nnum)
        ans = 0
        for x in range(R * C):
            if find(x) != -1:
                ans = max(ans, size[find(x)])
        return ans


Solution().largestArea(["000","010","000"])
