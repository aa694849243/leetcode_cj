# -*- coding: utf-8 -*-
from typing import List


# 给你一个大小为 m x n 的矩阵 mat 和一个整数阈值 threshold。
#
#  请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0 。
#
#
#  示例 1：
#
#
#
#
# 输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
# 输出：2
# 解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。
#
#
#  示例 2：
#
#
# 输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], thresh
# old = 1
# 输出：0
#
#
#  示例 3：
#
#
# 输入：mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
# 输出：3
#
#
#  示例 4：
#
#
# 输入：mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold =
#  40184
# 输出：2
#
#
#
#
#  提示：
#
#
#  1 <= m, n <= 300
#  m == mat.length
#  n == mat[i].length
#  0 <= mat[i][j] <= 10000
#  0 <= threshold <= 10^5
#
#  Related Topics 数组 二分查找
#  👍 64 👎 0

# 二维前缀和
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        R, C = len(mat), len(mat[0])
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1] + mat[r - 1][c - 1]

        def area(leng):
            ans = float('inf')
            for i in range(leng, R + 1):
                for j in range(leng, C + 1):
                    a = dp[i][j] - dp[i - leng][j] - dp[i][j - leng] + dp[i - leng][j - leng]
                    ans = min(a, ans)
            return ans

        l, r = 1, min(R, C) + 1
        while l < r:
            mid = (l + r) // 2
            if area(mid) <= threshold:
                l = mid + 1
            else:
                r = mid
        return l - 1


# 枚举优化
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        R, C = len(mat), len(mat[0])
        dp = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(1, R + 1):
            for c in range(1, C + 1):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1] - dp[r - 1][c - 1] + mat[r - 1][c - 1]

        def area(i, j, leng):
            a = dp[i + leng][j + leng] - dp[i][j + leng] - dp[i + leng][j] + dp[i][j]
            return a

        ans = 0
        for r in range(R + 1):
            for c in range(C + 1):
                for leng in range(ans, min(R, C) + 1):
                    if r + leng > R or c + leng > C:
                        break
                    if area(r, c, leng) <= threshold: #类似决策单调性，尽量延展leng，延长到>阈值，换一个点看看能不能同样长度<阈值
                        ans += 1
                    else:
                        break
        return ans-1


Solution().maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)
