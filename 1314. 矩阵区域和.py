# -*- coding: utf-8 -*-
from typing import List


# 给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 ma
# t[r][c] 的和：
#
#
#  i - k <= r <= i + k,
#  j - k <= c <= j + k 且
#  (r, c) 在矩阵内。
#
#
#
#
#  示例 1：
#
#
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# 输出：[[12,21,16],[27,45,33],[24,39,28]]
#
#
#  示例 2：
#
#
# 输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
# 输出：[[45,45,45],[45,45,45],[45,45,45]]
#
#
#
#
#  提示：
#
#
#  m == mat.length
#  n == mat[i].length
#  1 <= m, n, k <= 100
#  1 <= mat[i][j] <= 100
#
#  Related Topics 数组 矩阵 前缀和
#  👍 86 👎 0

# 二维前缀和
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(mat), len(mat[0])
        prefix=[[0]*(C+1) for _ in range(R+1)]
        for r in range(1,R+1):
            for c in range(1,C+1):
                prefix[r][c]=prefix[r][c-1]+prefix[r-1][c]-prefix[r-1][c-1]+mat[r-1][c-1]
        ans=[[0]*C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                rma,cma=min(i+1+k,R),min(j+1+k,C)
                rmi,cmi=max(i+1-k,1),max(j+1-k,1)
                ans[i][j]=prefix[rma][cma]-prefix[rmi-1][cma]-prefix[rma][cmi-1]+prefix[rmi-1][cmi-1]
        return ans
Solution().matrixBlockSum(mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2)