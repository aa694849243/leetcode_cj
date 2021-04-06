'''
编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。
示例:

现有矩阵 matrix 如下：

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
给定 target = 5，返回 true。

给定 target = 20，返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 方法1 按对角线进行二分搜索
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        h, v = len(matrix[0]), len(matrix)

        def biv(lo, hi, target):
            start = lo
            while lo < hi:
                mid = (lo + hi) // 2
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid
                else:
                    return True

        def bih(lo, hi, target):
            start = lo
            while lo < hi:
                mid = (lo + hi) // 2
                if matrix[start][mid] < target:
                    lo = mid + 1
                elif matrix[start][mid] > target:
                    hi = mid
                else:
                    return True

        for i in range(min(h, v)):
            if biv(i, v, target) or bih(i, h, target):
                return True
        return False


# 2 递归 分块
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        def rec(left, up, right, down):
            if left >= right or up >= down or up < 0 or left < 0:
                return False
            elif target > matrix[down-1][right-1] and target < matrix[up][left]:
                return False
            mid = (right + left) // 2
            x = up
            while up < down and matrix[up][mid] <= target:
                if matrix[up][mid] == target:
                    return True
                up += 1
            return rec(left, up, mid, down) or rec(mid + 1, x, right, up)

        return rec(0, 0, len(matrix[0]), len(matrix))
#特殊方法 找左下角或者右上角
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows,cols=len(matrix)-1,len(matrix[0])-1
        row,col=rows,0
        while row>=0 and col<=cols:
            if matrix[row][col]>target:
                row-=1
            elif matrix[row][col]==target:
                return True
            else:
                col+=1
        return False


a = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
Solution().searchMatrix(a, target)
