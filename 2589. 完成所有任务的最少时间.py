# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-03-14 3:11 
# ide： PyCharm
# 标准懒惰树
class LazyTree:
    def __init__(self, n):
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)

    def update(self, o, l, r, L, R, num):
        if L <= l and r <= R and num == r - l + 1:
            self.tree[o] = r - l + 1
            self.lazy[o] = 1
            return
        if l > R or r < L:
            return
        mid = (l + r) // 2
        l_num = self.query(o * 2, l, mid, L, R)
        r_num = self.query(o * 2 + 1, mid + 1, r, L, R)
        need_right_num = num - l_num
        if need_right_num > r_num:
            self.update(o * 2 + 1, mid + 1, r, L, R, min(need_right_num, r - mid))
        need_left_num = num - self.query(o * 2 + 1, mid + 1, r, L, R)
        if need_left_num > l_num:
            self.update(o * 2, l, mid, L, R, min(need_left_num, mid - l + 1))
        self.tree[o] = self.tree[o * 2] + self.tree[o * 2 + 1]
        ...

    def spread(self, o, l, r):
        if l == r:
            self.lazy[o] = 1
            return
        if self.lazy[o]:
            mid = (l + r) // 2
            self.tree[o * 2] = mid - l + 1
            self.tree[o * 2 + 1] = r - mid
            if l != r:
                self.lazy[o * 2] = 1
                self.lazy[o * 2 + 1] = 1
            self.lazy[o] = 0

    def query(self, o, l, r, L, R):
        if L <= l and r <= R:
            return self.tree[o]
        if l > R or r < L:
            return 0
        mid = (l + r) // 2
        self.spread(o, l, r)
        return self.query(o * 2, l, mid, L, R) + self.query(o * 2 + 1, mid + 1, r, L, R)


class Solution:
    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1])
        u = tasks[-1][1]
        lazytree = LazyTree(u)
        for start, end, duration in tasks:
            if lazytree.query(1, 1, u, start, end) < duration:
                lazytree.update(1, 1, u, start, end, duration)
        return lazytree.tree[1]


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findMinimumTime([[1,8,1],[4,4,1],[2,3,2]])
)
