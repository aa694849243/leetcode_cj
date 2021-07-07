# -*- coding: utf-8 -*-
from typing import List


# 给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。
#
#  请你统计并返回 grid 中 负数 的数目。
#
#
#
#  示例 1：
#
#
# 输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
# 输出：8
# 解释：矩阵中共有 8 个负数。
#
#
#  示例 2：
#
#
# 输入：grid = [[3,2],[1,0]]
# 输出：0
#
#
#  示例 3：
#
#
# 输入：grid = [[1,-1],[-1,-1]]
# 输出：3
#
#
#  示例 4：
#
#
# 输入：grid = [[-1]]
# 输出：1
#
#
#
#
#  提示：
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 100
#  -100 <= grid[i][j] <= 100
#
#
#
#
#  进阶：你可以设计一个时间复杂度为 O(n + m) 的解决方案吗？
#
#
#  Related Topics 数组 二分查找 矩阵
#  👍 70 👎 0


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])

        def bis_r(li, l, r):
            while l < r:
                mid = (l + r) // 2
                if li[mid] < 0:
                    r = mid
                else:
                    l = mid + 1
            return l
        self.ans=0
        def solve(lo,hi,l,r):
            if lo>=hi:
                return
            mid=(lo+hi)//2
            posmid=bis_r(grid[mid],l,r)
            self.ans+=C-posmid
            solve(lo,mid,posmid,r)
            solve(mid+1,hi,l,posmid+1)
        solve(0,R,0,C)
        return self.ans
Solution().countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]])
            
