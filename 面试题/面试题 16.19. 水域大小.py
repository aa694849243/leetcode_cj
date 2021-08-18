#!/usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from typing import List


# 你有一个用于表示一片土地的整数矩阵land，该矩阵中每个点的值代表对应地点的海拔高度。若值为0则表示水域。由垂直、水平或对角连接的水域为池塘。池塘的大小是指
# 相连接的水域的个数。编写一个方法来计算矩阵中所有池塘的大小，返回值需要从小到大排序。
#  示例：
#  输入：
# [
#   [0,2,1,0],
#   [0,1,0,1],
#   [1,1,0,1],
#   [0,1,0,1]
# ]
# 输出： [1,2,4]
#
#  提示：
#
#  0 < len(land) <= 1000
#  0 < len(land[i]) <= 1000
#
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵
#  👍 69 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pondSizes(self, land: List[List[int]]) -> List[int]:
        f = {}

        # size = collections.defaultdict(lambda: 1)

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
                # size[a] += size[b]

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        R, C, = len(land), len(land[0])
        m = {}

        def cal(r, c):
            if (r, c) not in m:
                m[r, c] = r * C + c
            return m[r, c]

        for r in range(R):
            for c in range(C):
                if land[r][c] != 0:
                    continue
                num = cal(r, c)
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and land[nr][nc] == 0:
                        nnum = cal(nr, nc)
                        union(num, nnum)
        size = collections.defaultdict(int)
        for r in range(R):
            for c in range(C):
                if land[r][c] == 0:
                    num = cal(r, c)
                    size[find(num)] += 1
        return sorted(size.values())
