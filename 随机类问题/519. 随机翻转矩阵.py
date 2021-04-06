'''
题中给出一个 n_rows 行 n_cols 列的二维矩阵，且所有值被初始化为 0。要求编写一个 flip 函数，均匀随机的将矩阵中的 0 变为 1，并返回该值的位置下标 [row_id,col_id]；同样编写一个 reset 函数，将所有的值都重新置为 0。尽量最少调用随机函数 Math.random()，并且优化时间和空间复杂度。

注意:

1 <= n_rows, n_cols <= 10000
0 <= row.id < n_rows 并且 0 <= col.id < n_cols
当矩阵中没有值为 0 时，不可以调用 flip 函数
调用 flip 和 reset 函数的次数加起来不会超过 1000 次
示例 1：

输入:
["Solution","flip","flip","flip","flip"]
[[2,3],[],[],[],[]]
输出: [null,[0,1],[1,2],[1,0],[1,1]]
示例 2：

输入:
["Solution","flip","flip","reset","flip"]
[[1,2],[],[],[],[]]
输出: [null,[0,0],[0,1],null,[0,0]]
输入语法解释：

输入包含两个列表：被调用的子程序和他们的参数。Solution 的构造函数有两个参数，分别为 n_rows 和 n_cols。flip 和 reset 没有参数，参数总会以列表形式给出，哪怕该列表为空'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(n_rows, n_cols)
# param_1 = obj.flip()
# obj.reset()
from typing import List

# 1映射为1维数组
# https://leetcode-cn.com/problems/random-flip-matrix/solution/sui-ji-fan-zhuan-ju-zhen-by-leetcode/
import random


class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.m = {}
        self.num = n_rows * n_cols - 1
        self.rows = n_rows
        self.cols = n_cols

    def flip(self) -> List[int]:
        n = random.randint(0, self.num)
        x = n // self.cols
        y = n % self.cols
        if n not in self.m:
            self.m[n] = self.num
            self.num -= 1
            return [x, y]
        else:
            n_ = self.m[n]
            while n_ in self.m:
                n_ = self.m[n_]
            self.m[n_] = self.num
            self.num -= 1
            return [n_ // self.cols, n_ % self.cols]

    def reset(self) -> None:
        self.m = {}
        self.num = self.rows * self.cols - 1


# 分块
import collections


class Solution:
    def __init__(self, n_rows: int, n_cols: int):
        self.m = collections.defaultdict(lambda: [0] * n_cols)
        self.li = [n_cols] * n_rows
        self.num = n_rows * n_cols
        self.rows = n_rows
        self.cols = n_cols

    def flip(self) -> List[int]:
        n = random.randint(1, self.num)
        bucket = 0
        for i in range(len(self.li)):
            if bucket + self.li[i] < n:
                bucket += self.li[i]
            else:
                x = i
                self.li[i] -= 1
                y_ = n - bucket
                for j in range(len(self.m[x])):
                    if self.m[x][j] == 0:
                        y_ -= 1
                        if y_ == 0:
                            self.m[x][j] = 1
                            y = j
                            break
                break
        self.num -= 1
        return [x, y]

    def reset(self) -> None:
        self.m = collections.defaultdict(lambda: [0] * self.cols)
        self.li = [self.cols] * self.rows
        self.num = self.rows * self.cols


obj = Solution(4, 17)
a = obj.flip()
b = obj.flip()
obj.reset()
c = obj.flip()
d = obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()
obj.flip()