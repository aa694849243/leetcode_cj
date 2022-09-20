# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-09-04 1:33 
# ide： PyCharm
# 给你两个整数 m 和 k ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 MK 平均值 。
#
#  MK 平均值 按照如下步骤计算：
#
#
#  如果数据流中的整数少于 m 个，MK 平均值 为 -1 ，否则将数据流中最后 m 个元素拷贝到一个独立的容器中。
#  从这个容器中删除最小的 k 个数和最大的 k 个数。
#  计算剩余元素的平均值，并 向下取整到最近的整数 。
#
#
#  请你实现 MKAverage 类：
#
#
#  MKAverage(int m, int k) 用一个空的数据流和两个整数 m 和 k 初始化 MKAverage 对象。
#  void addElement(int num) 往数据流中插入一个新的元素 num 。
#  int calculateMKAverage() 对当前的数据流计算并返回 MK 平均数 ，结果需 向下取整到最近的整数 。
#
#
#
#
#  示例 1：
#
#
# 输入：
# ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement",
# "calculateMKAverage", "addElement", "addElement", "addElement",
# "calculateMKAverage"]
# [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
# 输出：
# [null, null, null, -1, null, 3, null, null, null, 5]
#
# 解释：
# MKAverage obj = new MKAverage(3, 1);
# obj.addElement(3);        // 当前元素为 [3]
# obj.addElement(1);        // 当前元素为 [3,1]
# obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
# obj.addElement(10);       // 当前元素为 [3,1,10]
# obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
#                           // 删除最小以及最大的 1 个元素后，容器为 [3]
#                           // [3] 的平均值等于 3/1 = 3 ，故返回 3
# obj.addElement(5);        // 当前元素为 [3,1,10,5]
# obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
# obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
# obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
#                           // 删除最小以及最大的 1 个元素后，容器为 [5]
#                           // [5] 的平均值等于 5/1 = 5 ，故返回 5
#
#
#
#
#  提示：
#
#
#  3 <= m <= 10⁵
#  1 <= k*2 < m
#  1 <= num <= 10⁵
#  addElement 与 calculateMKAverage 总操作次数不超过 10⁵ 次。
#
#
#  Related Topics 设计 队列 数据流 有序集合 堆（优先队列） 👍 30 👎 0

from collections import deque
from typing import List
import heapq

# leetcode submit region begin(Prohibit modification and deletion)
from sortedcontainers import SortedList


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.history = deque()
        self.sorted_lst = SortedList([])
        self.l_sum = 0
        self.r_sum = 0
        self.sum = 0

    def addElement(self, num: int) -> None:
        self.history.append(num)
        self.sum += num
        if len(self.history) <= self.m:
            if len(self.history) == self.m:
                self.sorted_lst = SortedList(self.history)
                self.l_sum = sum(self.sorted_lst[:self.k])
                self.r_sum = sum(self.sorted_lst[-self.k:])
        else:
            # self.sorted_lst.add(num)
            his_pop = self.history.popleft()
            self.sum -= his_pop
            pos = self.sorted_lst.bisect_left(his_pop)
            if pos < self.k:
                self.l_sum -= his_pop
                self.sorted_lst.remove(his_pop)
                self.sorted_lst.add(num)
                p_ = self.sorted_lst.bisect_left(num)
                if p_ < self.k:
                    self.l_sum += num
                elif p_ >= self.m - self.k:
                    self.r_sum += num
                    self.r_sum -= self.sorted_lst[-self.k - 1]
                    self.l_sum += self.sorted_lst[self.k - 1]
                else:
                    self.l_sum += self.sorted_lst[self.k - 1]
            elif pos >= self.m - self.k:
                self.r_sum -= his_pop
                self.sorted_lst.remove(his_pop)
                self.sorted_lst.add(num)
                p_ = self.sorted_lst.bisect_left(num)
                if p_ < self.k:
                    self.l_sum += num
                    self.l_sum -= self.sorted_lst[self.k]
                    self.r_sum += self.sorted_lst[-self.k]
                elif p_ >= self.m - self.k:
                    self.r_sum += num
                else:
                    self.r_sum += self.sorted_lst[-self.k]
            else:
                self.sorted_lst.remove(his_pop)
                self.sorted_lst.add(num)
                p_ = self.sorted_lst.bisect_left(num)
                if p_ < self.k:
                    self.l_sum += num
                    self.l_sum -= self.sorted_lst[self.k]
                elif p_ >= self.m - self.k:
                    self.r_sum += num
                    self.r_sum -= self.sorted_lst[-self.k - 1]
                else:
                    pass
    def calculateMKAverage(self) -> int:
        if len(self.history) != self.m:
            return -1
        return int((self.sum - self.l_sum - self.r_sum) / (self.m - 2 * self.k))


# Your MKAverage object will be instantiated and called as such:
obj = MKAverage(3, 1)
obj.addElement(5)
obj.addElement(6)
print(obj.calculateMKAverage())
obj.addElement(8)
print(obj.calculateMKAverage())
obj.addElement(4)
obj.addElement(2)
obj.addElement(1)
print(obj.calculateMKAverage())
# leetcode submit region end(Prohibit modification and deletion)
