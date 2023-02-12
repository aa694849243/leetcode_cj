# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-10 23:44 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.f = {}
        self.sizes = collections.defaultdict(lambda: 1)
        self.ma = 0

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        self.ma = max(self.ma, 1)
        return self.f[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        a, b = sorted([a, b])
        if a != b:
            self.f[b] = a
            self.sizes[a] += self.sizes[b]
            self.ma = max(self.ma, self.sizes[a])


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = UnionFind()
        visted = set()
        nums = list(set(nums))
        for num in nums:
            uf.find(num)
            if num + 1 in visted:
                uf.union(num, num + 1)
            if num - 1 in visted:
                uf.union(num - 1, num)
            visted.add(num)
        return uf.ma

# leetcode submit region end(Prohibit modification and deletion)

