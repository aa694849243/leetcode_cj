#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 编写一种算法，若M × N矩阵中某个元素为0，则将其所在的行与列清零。
#
#
#
#  示例 1：
#
#  输入：
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# 输出：
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
#
#
#  示例 2：
#
#  输入：
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# 输出：
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
#
#  Related Topics 数组 哈希表 矩阵
#  👍 31 👎 0

#1两个变量
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        R, C = len(matrix), len(matrix[0])

        flagr0 = False
        flagc0 = False
        if matrix[0][0] == 0:
            flagr0 = True
            flagc0 = True
        for r in range(R):
            if matrix[r][0]==0:
                flagr0=True
                break
        for c in range(C):
            if matrix[0][c]==0:
                flagc0=True
                break
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
        for r in range(1, R):
            for c in range(1, C):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        for r in range(R):
            if flagr0:
                matrix[r][0]=0
        for c in range(C):
            if flagc0:
                matrix[0][c]=0

#2 1个变量

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        R, C = len(matrix), len(matrix[0])
        flgc0=False
        for i in range(R):
            if matrix[i][0]==0:
                flgc0=True
            for j in range(1,C):
                if matrix[i][j]==0:
                    matrix[0][j]=matrix[i][0]=0
        for i in range(R-1,-1,-1): #从后往前遍历，避免提前更新第0行
            for j in range(1,C):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
            matrix[i][0]=0 if flgc0 else matrix[i][0]

Solution().setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
