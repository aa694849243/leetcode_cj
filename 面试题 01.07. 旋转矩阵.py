#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。请你设计一种算法，将图像旋转 90 度。
#
#  不占用额外内存空间能否做到？
#
#
#
#  示例 1:
#
#
# 给定 matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#
#
#  示例 2:
#
#
# 给定 matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],
#
# 原地旋转输入矩阵，使其变为:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
#
#
#  注意：本题与主站 48 题相同：https://leetcode-cn.com/problems/rotate-image/
#  Related Topics 数组 数学 矩阵
#  👍 177 👎 0

#模拟
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n // 2):
            step = n - 2 * i - 1
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i + step - (j - i)][i]
                matrix[i + step - (j - i)][i] = matrix[i + step][2 * i + step - j]
                matrix[i + step][2 * i + step - j] = matrix[j][i + step]
                matrix[j][i + step] = tmp
        return matrix
# 先根据横坐标翻转，再对角线翻转

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(n):
                matrix[i][j],matrix[n-1-i][j]=matrix[n-1-i][j],matrix[i][j]
        for i in range(n):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])
