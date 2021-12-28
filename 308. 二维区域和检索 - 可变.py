#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 给你一个二维矩阵 matrix ，你需要处理下面两种类型的若干次查询：
#
#
#  更新：更新 matrix 中某个单元的值。
#  求和：计算矩阵 matrix 中某一矩形区域元素的 和 ，该区域由 左上角 (row1, col1) 和 右下角 (row2, col2) 界定。
#
#
#  实现 NumMatrix 类：
#
#
#  NumMatrix(int[][] matrix) 用整数矩阵 matrix 初始化对象。
#  void update(int row, int col, int val) 更新 matrix[row][col] 的值到 val 。
#  int sumRegion(int row1, int col1, int row2, int col2) 返回矩阵 matrix 中指定矩形区域元素的
# 和 ，该区域由 左上角 (row1, col1) 和 右下角 (row2, col2) 界定。
#
#
#
#
#  示例：
#
#
# 输入
# ["NumMatrix", "sumRegion", "update", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0,
# 3, 0, 5]]], [2, 1, 4, 3], [3, 2, 2], [2, 1, 4, 3]]
# 输出
# [null, 8, null, 10]
#
# 解释
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2,
# 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // 返回 8 (即, 左侧红色矩形的和)
# numMatrix.update(3, 2, 2);       // 矩阵从左图变为右图
# numMatrix.sumRegion(2, 1, 4, 3); // 返回 10 (即，右侧红色矩形的和)
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 200
#  -105 <= matrix[i][j] <= 105
#  0 <= row < m
#  0 <= col < n
#  -105 <= val <= 105
#  0 <= row1 <= row2 < m
#  0 <= col1 <= col2 < n
#  最多调用104 次 sumRegion 和 update 方法
#
#  Related Topics 设计 树状数组 线段树 数组 矩阵
#  👍 63 👎 0
# 1 线段树
class ftree:
    def __init__(self, n):
        self.li = [0] * (n + 1)
        self.n = n

    @staticmethod
    def lowbit(num):
        return num & -num

    def update(self, i, diff):
        while i <= self.n:
            self.li[i] += diff
            i += self.lowbit(i)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.li[i]
            i -= self.lowbit(i)
        return res


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.R, self.C = len(matrix), len(matrix[0])
        n = self.R * self.C
        self.tree = ftree(n)
        self.matrix = matrix
        for r in range(self.R):
            for c in range(self.C):
                num = self.cal(r, c) + 1
                self.tree.update(num, matrix[r][c])

    def cal(self, r, c):
        return r * self.C + c

    def update(self, row: int, col: int, val: int) -> None:
        num = self.cal(row, col) + 1
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.tree.update(num, diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            num1 = self.cal(r, col1)
            num2 = self.cal(r, col2) + 1
            res += self.tree.query(num2) - self.tree.query(num1)
        return res


# 2线段树 单点更新 区间查找
class segtree:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.left, self.right = None, None
        self.treesum = 0


class NumMatrix:
    def streebuild(self, l, r):
        node = segtree(l, r)
        if l == r:
            return node
        node.left = self.streebuild(l, (l + r) // 2)
        node.right = self.streebuild((l + r) // 2 + 1, r)
        return node

    def streeupdate(self, node, id, diff):
        node.treesum += diff
        if node.l == node.r:
            return
        mid = (node.l + node.r) // 2
        if id > mid:
            self.streeupdate(node.right, id, diff)
        else:
            self.streeupdate(node.left, id, diff)

    def streequiry(self, node, ql, qr):
        l, r = node.l, node.r
        if ql > r or qr < l:
            return 0
        if ql <= l and qr >= r:
            return node.treesum
        return self.streequiry(node.left, ql, qr) + self.streequiry(node.right, ql, qr)

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.R, self.C = len(matrix), len(matrix[0])
        n = self.R * self.C
        self.st = self.streebuild(0, n - 1)
        for r in range(self.R):
            for c in range(self.C):
                id = self.cal(r, c)
                self.streeupdate(self.st, id, matrix[r][c])

    def cal(self, r, c):
        return r * self.C + c

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        self.streeupdate(self.st, self.cal(row, col), diff)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for r in range(row1, row2 + 1):
            id1, id2 = self.cal(r, col1), self.cal(r, col2)
            res += self.streequiry(self.st, id1, id2)
        return res
a = NumMatrix([[1]])
a.update(*[0, 0, -1])
a.sumRegion(*[0, 0, 0, 0])

a = NumMatrix([[2, 4], [-3, 5]])
a.update(*[0, 1, 3])
a.update(*[1, 1, -3])
a.update(*[0, 1, 1])
a.sumRegion(*[0, 0, 1, 1])

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
