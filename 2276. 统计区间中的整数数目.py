# -*- coding: utf-8 -*-
# 给你区间的 空 集，请你设计并实现满足要求的数据结构：
#
#
#  新增：添加一个区间到这个区间集合中。
#  统计：计算出现在 至少一个 区间中的整数个数。
#
#
#  实现 CountIntervals 类：
#
#
#  CountIntervals() 使用区间的空集初始化对象
#  void add(int left, int right) 添加区间 [left, right] 到区间集合之中。
#  int count() 返回出现在 至少一个 区间中的整数个数。
#
#
#  注意：区间 [left, right] 表示满足 left <= x <= right 的所有整数 x 。
#
#
#
#  示例 1：
#
#
# 输入
# ["CountIntervals", "add", "add", "count", "add", "count"]
# [[], [2, 3], [7, 10], [], [5, 8], []]
# 输出
# [null, null, null, 6, null, 8]
#
# 解释
# CountIntervals countIntervals = new CountIntervals(); // 用一个区间空集初始化对象
# countIntervals.add(2, 3);  // 将 [2, 3] 添加到区间集合中
# countIntervals.add(7, 10); // 将 [7, 10] 添加到区间集合中
# countIntervals.count();    // 返回 6
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 7、8、9、10 出现在区间 [7, 10] 中
# countIntervals.add(5, 8);  // 将 [5, 8] 添加到区间集合中
# countIntervals.count();    // 返回 8
#                            // 整数 2 和 3 出现在区间 [2, 3] 中
#                            // 整数 5 和 6 出现在区间 [5, 8] 中
#                            // 整数 7 和 8 出现在区间 [5, 8] 和区间 [7, 10] 中
#                            // 整数 9 和 10 出现在区间 [7, 10] 中
#
#
#
#  提示：
#
#
#  1 <= left <= right <= 10⁹
#  最多调用 add 和 count 方法 总计 10⁵ 次
#  调用 count 方法至少一次
#
#
#  Related Topics 设计 线段树 有序集合
#  👍 41 👎 0
import collections

import sortedcontainers


# leetcode submit region begin(Prohibit modification and deletion)
# 线段树 阻止传播 动态开点
# class CountIntervals:
#
#     def __init__(self):
#         self.tree = collections.defaultdict(int)
#
#     def update(self, s, e, l=1, r=10 ** 9, id=1):
#         if s > r or e < l:
#             return
#         if self.tree[id] == r - l + 1:  # 阻挡之前的满区间后续更改
#             return
#         if s <= l <= r <= e:
#             self.tree[id] = r - l + 1
#             return
#         self.update(s, e, l, (l + r) // 2, id * 2)
#         self.update(s, e, (l + r) // 2 + 1, r, id * 2 + 1)
#         self.tree[id] = self.tree[id * 2] + self.tree[id * 2 + 1]
#
#     def add(self, left: int, right: int) -> None:
#         self.update(left, right)
#
#     def count(self) -> int:
#         return self.tree[1]


# 珂朵莉树
import sortedcontainers
class CountIntervals:

    def __init__(self):
        self.sdict = sortedcontainers.SortedDict()
        self.cnt = 0

    def add(self, left: int, right: int) -> None:
        idx = self.sdict.bisect_left(left)
        while idx < len(self.sdict) and self.sdict.peekitem(idx)[1] <= right:
            left = min(left, self.sdict.peekitem(idx)[1])
            right = max(right, self.sdict.peekitem(idx)[0])
            self.cnt -= self.sdict.peekitem(idx)[0] - self.sdict.peekitem(idx)[1] + 1
            self.sdict.popitem(idx)
        self.cnt += right - left + 1
        self.sdict[right] = left  # 左右倒置

    def count(self) -> int:
        return self.cnt


# Your CountIntervals object will be instantiated and called as such:

# leetcode submit region end(Prohibit modification and deletion)
obj = CountIntervals()
obj.add(2, 3)
obj.add(7, 10)
obj.add(5, 8)
param_2 = obj.count()
