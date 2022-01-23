#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 3. 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。
# 输入: [   [1,1,1],   [1,0,1],   [1,1,1] ] 输出: [   [1,0,1],   [0,0,0],   [1,0,1] ]
#
# 测试用例：
# 1行列：M, N
# 2矩阵
def func(matrix):
    R, C = len(matrix), len(matrix[0])
    mr = set()
    mc = set()
    for r in range(R):
        for c in range(C):
            if matrix[r][c] == 0:
                mr.add(r)
                mc.add(c)
    for r in range(R):
        if r in mr:
            matrix[r] = [0] * C
    for c in range(C):
        if c in mc:
            for r in range(R):
                matrix[r][c] = 0
    return matrix


matrix = [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
print(func(matrix))
