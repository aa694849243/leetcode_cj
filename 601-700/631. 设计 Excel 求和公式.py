# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 你的任务是实现 Excel 的求和功能，具体的操作如下：
#
#  Excel(int H, char W): 这是一个构造函数，输入表明了 Excel 的高度和宽度。H 是一个正整数，范围从 1 到 26，代表高度。W
# 是一个字符，范围从 'A' 到 'Z'，宽度等于从 'A' 到 W 的字母个数。Excel 表格是一个高度 * 宽度的二维整数数组，数组中元素初始化为 0。第一
# 行下标从 1 开始，第一列下标从 'A' 开始。
#
#
#
#  void Set(int row, char column, int val): 设置 C(row, column) 中的值为 val。
#
#
#
#  int Get(int row, char column): 返回 C(row, column) 中的值。
#
#
#
#  int Sum(int row, char column, List of Strings : numbers): 这个函数会将计算的结果放入 C(
# row, column) 中，计算的结果等于在 numbers 中代表的所有元素之和，这个函数同时也会将这个结果返回。求和公式会一直计算更新结果直到这个公式被其他的值
# 或者公式覆盖。
#
#  numbers 是若干字符串的集合，每个字符串代表单个位置或一个区间。如果这个字符串表示单个位置，它的格式如下：ColRow，例如 "F7" 表示位置 (
# 7, F) 。如果这个字符串表示一个区间，它的格式如下：ColRow1:ColRow2。区间就是左上角为 ColRow1 右下角为 ColRow2 的长方形。
#
#
#
#
#  注意: 你可以认为不会出现循环求和的定义，比如说：mat[1]['A'] == sum(1, "B") 和 mat[1]['B'] == sum(1,
# "A").
#
#
#
#  示例 1:
#
#
# 输入:
# ["Excel", "set", "sum", "set", "get"]
# [[3, "C"], [1, "A", 2], [3, "C", ["A1", "A1:B2"]], [2, "B", 2], [3, "C"]]
# 输出:
# [null, null, 4, null, 6]
#
# 解释:
# Excel excel = new Excel(3, "C");
#  // 构造一个 3*3 的二维数组，初始化全是 0。
#  //   A B C
#  // 1 0 0 0
#  // 2 0 0 0
#  // 3 0 0 0
# excel.set(1, "A", 2);
#  // 设置 C(1,"A") 为 2。
#  //   A B C
#  // 1 2 0 0
#  // 2 0 0 0
#  // 3 0 0 0
# excel.sum(3, "C", ["A1", "A1:B2"]); // return 4
#  // 将 C(3,"C") 的值设为 C(1,"A") 单点以及左上角为 C(1,"A") 右下角为 C(2,"B") 的长方形两者之和。返回值 4。
#  // 1 2 0 0
#  // 2 0 0 0
#  // 3 0 0 4
# excel.set(2, "B", 2);
# // 将 C(2,"B") 设为 2。 注意 C(3, "C") 的值也同时改变。
#  //   A B C
#  // 1 2 0 0
#  // 2 0 2 0
#  // 3 0 0 6
# excel.get(3, "C"); // 返回 6
#
#
#
#  提示:
#
#
#  1 <= height <= 26
#  'A' <= width <= 'Z'
#  1 <= row <= height
#  'A' <= column <= width
#  -100 <= val <= 100
#  1 <= numbers.length <= 5
#  numbers[i] 的格式为 "ColRow" 或 "ColRow1:ColRow2".
#  set, get, and sum 操作数不超过 100 次
#
#
#
#
#
#
#
#
#  Related Topics 图 设计 拓扑排序 👍 27 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Cell:
    def __init__(self, val, dependencies=dict()):
        self.val = val
        self.dependencies = dependencies


class Excel:

    def __init__(self, height: int, width: str):
        self.R, self.C = height, ord(width) - ord('A') + 1
        self.matrix = [[Cell(0) for _ in range(self.C)] for _ in range(self.R)]

    def set(self, row: int, column: str, val: int) -> None:
        r, c = row - 1, ord(column) - ord('A')
        self.matrix[r][c] = Cell(val)
        stack = []
        self.update(r, c, stack)
        self.cal(stack)

    def update(self, r, c, stack):
        for i in range(self.R):
            for j in range(self.C):
                cell = self.matrix[i][j]
                if (r, c) in cell.dependencies:
                    self.update(i, j, stack)
        stack.append((r, c))

    def cal(self, stack):
        stack.pop()
        while stack:
            r, c = stack.pop()
            ins = self.matrix[r][c]
            sum_ = 0
            for dr, dc in ins.dependencies:
                sum_ += ins.dependencies[dr, dc] * self.matrix[dr][dc].val
            self.matrix[r][c].val = sum_

    def get(self, row: int, column: str) -> int:
        return self.matrix[row - 1][ord(column) - ord('A')].val

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        r, c = row - 1, ord(column) - ord('A')
        sum_ = 0
        self.matrix[r][c].dependencies = dict()
        for chr in numbers:
            if ':' in chr:
                index = chr.index(':')
                chr1, chr2 = chr[:index], chr[index + 1:]
                r1, c1 = int(chr1[1:]) - 1, ord(chr1[0]) - ord('A')
                r2, c2 = int(chr2[1:]) - 1, ord(chr2[0]) - ord('A')
                for i in range(r1, r2 + 1):
                    for j in range(c1, c2 + 1):
                        sum_ += self.matrix[i][j].val
                        if (i, j) not in self.matrix[r][c].dependencies:
                            self.matrix[r][c].dependencies[i, j] = 0
                        self.matrix[r][c].dependencies[i, j] += 1
            else:
                r1, c1 = int(chr[1:]) - 1, ord(chr[0]) - ord('A')
                sum_ += self.matrix[r1][c1].val
                if (r1, c1) not in self.matrix[r][c].dependencies:
                    self.matrix[r][c].dependencies[r1, c1] = 0
                self.matrix[r][c].dependencies[r1, c1] += 1
        self.matrix[r][c].val = sum_
        stack = []
        self.update(r, c, stack)
        self.cal(stack)
        return self.matrix[r][c].val


a = Excel(*[5, "E"])
a.sum(*[2, "B", ["A1", "A1"]])
a.set(*[1, "A", 2])
a.sum(*[3, "C", ["B2", "A1:B2"]])
