import collections, heapq, itertools
from typing import List


# n 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。
#
#  如果一块石头的 同行或者同列 上有其他石头存在，那么就可以移除这块石头。
#
#  给你一个长度为 n 的数组 stones ，其中 stones[i] = [xi, yi] 表示第 i 块石头的位置，返回 可以移除的石子 的最大数量。
#
#
#
#
#  示例 1：
#
#
# 输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
# 输出：5
# 解释：一种移除 5 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
# 2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
# 3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
# 4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
# 5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
# 石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
#
#  示例 2：
#
#
# 输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
# 输出：3
# 解释：一种移除 3 块石头的方法如下所示：
# 1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
# 2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
# 3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
# 石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
#
#  示例 3：
#
#
# 输入：stones = [[0,0]]
# 输出：0
# 解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。
#
#
#
#  提示：
#
#
#  1 <= stones.length <= 1000
#  0 <= xi, yi <= 104
#  不会有两块石头放在同一个坐标点上
#
#  Related Topics 深度优先搜索 并查集
#  👍 211 👎 0


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        R, C = 10001, 10001
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

        mr, mc = {}, {}
        for r, c in stones:
            if r in mr:
                union(mr[r], r * C + c)
            else:
                mr[r] = r * C + c
            if c in mc:
                union(mc[c], r * C + c)
            else:
                mc[c]=r*C+c
        ans = 0
        for r, c in stones:
            a = r * C + c
            if f.get(a) == a:
                ans += size[a] - 1
        return ans


Solution().removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])
