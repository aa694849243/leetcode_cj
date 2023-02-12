# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-09 23:42 
# ide： PyCharm
from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# 二进制前缀树
class BitTrie:
    def __init__(self):
        self.f = {}

    def insert(self, key: int) -> None:
        tree = self.f
        for i in range(31, -1, -1):
            c = key >> i & 1
            if c not in tree:
                tree[c] = {}
            tree = tree[c]

    def search(self, key: int) -> int:
        tree = self.f
        ans = 0
        for i in range(31, -1, -1):
            c = key >> i & 1
            if 1 - c in tree:
                ans += 1 << i
                tree = tree[1 - c]
            elif c in tree:
                tree = tree[c]
            else:
                break
        return ans


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        btrie = BitTrie()
        for num in nums:
            ans = max(ans, btrie.search(num))
            btrie.insert(num)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findMaximumXOR(
        [3, 10, 5, 25, 2, 8]
    )
)