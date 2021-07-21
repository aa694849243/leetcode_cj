#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
#  
#
# 示例 1：
#
# 输入：m = 2, n = 3, k = 1
# 输出：3
# 示例 2：
#
# 输入：m = 3, n = 1, k = 0
# 输出：1
# 提示：
#
# 1 <= n,m <= 100
# 0 <= k <= 20
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 根据扩散方向只需要只需要关注左上两个方向的格子
# 1bfs
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        def cal(num):
            x = 0
            while num:
                x += num % 10
                num //= 10
            return x

        q = Queue()
        q.put((0, 0))
        visted = {(0, 0)}
        while not q.empty():
            r, c = q.get()
            for nr, nc in [(r + 1, c), (r, c + 1)]:
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visted and cal(nr) + cal(nc) <= k:
                    visted.add((nr, nc))
                    q.put((nr, nc))
        return len(visted)


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def cal(num):
            x = 0
            while num:
                x += num % 10
                num //= 10
            return x

        res = {(0, 0)}
        for r in range(m):
            for c in range(n):
                if ((r - 1, c) in res or (r, c - 1) in res) and cal(r)+cal(c)<=k:
                    res.add((r,c))
        return len(res)


Solution().movingCount(m=2, n=3, k=1)
