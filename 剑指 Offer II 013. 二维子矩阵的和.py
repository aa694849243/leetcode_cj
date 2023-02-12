# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-06 21:07 
# ide： PyCharm
# 二维前缀和
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.sums = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                self.sums[r + 1][c + 1] = self.sums[r][c + 1] + self.sums[r + 1][c] - self.sums[r][c] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2 + 1][col2 + 1] - self.sums[row2 + 1][col1] - self.sums[row1][col2 + 1] + self.sums[row1][col1]

