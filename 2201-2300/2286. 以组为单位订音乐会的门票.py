# -*- coding: utf-8 -*-
# 一个音乐会总共有 n 排座位，编号从 0 到 n - 1 ，每一排有 m 个座椅，编号为 0 到 m - 1 。你需要设计一个买票系统，针对以下情况进行座位
# 安排：
#
#
#  同一组的 k 位观众坐在 同一排座位，且座位连续 。
#  k 位观众中 每一位 都有座位坐，但他们 不一定 坐在一起。
#
#
#  由于观众非常挑剔，所以：
#
#
#  只有当一个组里所有成员座位的排数都 小于等于 maxRow ，这个组才能订座位。每一组的 maxRow 可能 不同 。
#  如果有多排座位可以选择，优先选择 最小 的排数。如果同一排中有多个座位可以坐，优先选择号码 最小 的。
#
#
#  请你实现 BookMyShow 类：
#
#
#  BookMyShow(int n, int m) ，初始化对象，n 是排数，m 是每一排的座位数。
#  int[] gather(int k, int maxRow) 返回长度为 2 的数组，表示 k 个成员中 第一个座位 的排数和座位编号，这 k 位成员必
# 须坐在 同一排座位，且座位连续 。换言之，返回最小可能的 r 和 c 满足第 r 排中 [c, c + k - 1] 的座位都是空的，且 r <=
# maxRow 。如果 无法 安排座位，返回 [] 。
#  boolean scatter(int k, int maxRow) 如果组里所有 k 个成员 不一定 要坐在一起的前提下，都能在第 0 排到第
# maxRow 排之间找到座位，那么请返回 true 。这种情况下，每个成员都优先找排数 最小 ，然后是座位编号最小的座位。如果不能安排所有 k 个成员的座位，请返回
# false 。
#
#
#
#
#  示例 1：
#
#
# 输入：
# ["BookMyShow", "gather", "gather", "scatter", "scatter"]
# [[2, 5], [4, 0], [2, 0], [5, 1], [5, 1]]
# 输出：
# [null, [0, 0], [], true, false]
#
# 解释：
# BookMyShow bms = new BookMyShow(2, 5); // 总共有 2 排，每排 5 个座位。
# bms.gather(4, 0); // 返回 [0, 0]
#                   // 这一组安排第 0 排 [0, 3] 的座位。
# bms.gather(2, 0); // 返回 []
#                   // 第 0 排只剩下 1 个座位。
#                   // 所以无法安排 2 个连续座位。
# bms.scatter(5, 1); // 返回 True
#                    // 这一组安排第 0 排第 4 个座位和第 1 排 [0, 3] 的座位。
# bms.scatter(5, 1); // 返回 False
#                    // 总共只剩下 2 个座位。
#
#
#
#
#  提示：
#
#
#  1 <= n <= 5 * 10⁴
#  1 <= m, k <= 10⁹
#  0 <= maxRow <= n - 1
#  gather 和 scatter 总 调用次数不超过 5 * 10⁴ 次。
#
#
#  Related Topics 设计 树状数组 线段树 二分查找
#  👍 24 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class BookMyShow:

    def __init__(self, n: int, m: int):
        self.mintree = [0] * (4 * n)
        self.sumtree = [0] * (4 * n)
        self.n = n
        self.m = m

    def update(self, o, s, e, l, r, val):
        if s > r or e < l:
            return
        if s <= l <= r <= e:
            self.mintree[o] += val
            self.sumtree[o] += val
            return
        mid = (l + r) // 2
        self.update(o * 2, s, e, l, mid, val)
        self.update(o * 2 + 1, s, e, mid + 1, r, val)
        self.sumtree[o] = self.sumtree[o * 2] + self.sumtree[o * 2 + 1]
        self.mintree[o] = min(self.mintree[o * 2], self.mintree[o * 2 + 1])

    def query_sum(self, o, s, e, l, r):
        if s > r or e < l:
            return 0
        if s <= l <= r <= e:
            return self.sumtree[o]
        mid = (l + r) // 2
        return self.query_sum(o * 2, s, e, l, mid) + self.query_sum(o * 2 + 1, s, e, mid + 1, r)

    def find_minidx_le_val(self, o, s, e, l, r, val):
        if s > r or e < l:
            return -1
        if self.mintree[o] > val:
            return -1
        if l == r:
            return l
        mid = (l + r) // 2
        m1 = self.find_minidx_le_val(o * 2, s, e, l, mid, val)
        if m1 != -1:
            return m1
        return self.find_minidx_le_val(o * 2 + 1, s, e, mid + 1, r, val)

    def gather(self, k: int, maxRow: int) -> List[int]:
        val = self.m - k
        idx = self.find_minidx_le_val(1, 0, maxRow, 0, self.n - 1, val)
        if idx != -1:
            c = self.query_sum(1, idx, idx, 0, self.n - 1)
            self.update(1, idx, idx, 0, self.n - 1, k)
            return [idx, c]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        sum_ = self.query_sum(1, 0, maxRow, 0, self.n - 1)
        if sum_ + k > self.m * (maxRow + 1):
            return False
        while k > 0:
            idx = self.find_minidx_le_val(1, 0, maxRow, 0, self.n - 1, self.m - 1)
            delta = self.m - self.query_sum(1, idx, idx, 0, self.n - 1)
            if delta <= k:
                self.update(1, idx, idx, 0, self.n - 1, delta)
            else:
                self.update(1, idx, idx, 0, self.n - 1, k)
            k -= delta
        return True


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)
# leetcode submit region end(Prohibit modification and deletion)
obj = BookMyShow(2, 6)
print(obj.scatter(2, 1))
print(obj.scatter(8, 0))
# obj.scatter(5, 1)
