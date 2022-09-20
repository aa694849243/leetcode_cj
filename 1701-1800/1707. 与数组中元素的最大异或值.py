import collections, heapq, itertools
# 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。
#
#  第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j]
# XOR xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。
#
#  返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个
# 查询的答案。
#
#
#
#  示例 1：
#
#  输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# 输出：[3,3,7]
# 解释：
# 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
#
#
#  示例 2：
#
#  输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# 输出：[15,-1,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length, queries.length <= 10⁵
#  queries[i].length == 2
#  0 <= nums[j], xi, mi <= 10⁹
#
#
#  Related Topics 位运算 字典树 数组 👍 132 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/maximum-xor-with-an-element-from-array/solution/yu-shu-zu-zhong-yuan-su-de-zui-da-yi-huo-7erc/
# 二进制前缀树
class Trie:
    L = 30

    def __init__(self):
        self.left = None
        self.right = None

    def insert(self, val):
        node = self
        for off in range(Trie.L, -1, -1):
            if (val >> off) & 1:
                if node.right is None:
                    node.right = Trie()
                node = node.right
            else:
                if node.left is None:
                    node.left = Trie()
                node = node.left

    def get_max_xor(self, val):
        ans, node = 0, self
        for off in range(Trie.L, -1, -1):
            bit = (val >> off) & 1
            check = False
            if bit ^ 1 and node.right is not None:
                node = node.right
                check = True
            elif bit ^ 0 and node.left is not None:
                node = node.left
                check = True
            elif bit ^ 1:  # bit==0往左走
                node = node.left
            elif bit ^ 0:  # bit==1往右走 node = node.right
                node = node.right
            ans = (ans << 1) | check
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        nums.sort()
        queries = sorted([(val, lim, i) for i, (val, lim) in enumerate(queries)], key=lambda x: x[1])
        ans = [0] * len(queries)
        p = 0
        trie = Trie()
        for val, lim, idx in queries:
            while p < len(nums) and nums[p] <= lim:
                trie.insert(nums[p])
                p += 1
            if p == 0:
                ans[idx] = -1
            else:
                ans[idx] = trie.get_max_xor(val)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Trie2:
    L = 30

    def __init__(self):
        self.left = None
        self.right = None
        self.mi = float('inf')

    def insert(self, val):
        node = self
        node.mi = min(node.mi, val)
        for off in range(Trie2.L, -1, -1):
            if (val >> off) & 1:
                if node.right is None:
                    node.right = Trie2()
                node = node.right
            else:
                if node.left is None:
                    node.left = Trie2()
                node = node.left
            node.mi = min(node.mi, val)

    def get_max_xor(self, val, lim):
        if lim < self.mi:
            return -1
        ans, node = 0, self
        for off in range(Trie2.L, -1, -1):
            bit = (val >> off) & 1
            check = False
            if bit ^ 1:  # bit==0
                if node.right is not None and node.right.mi <= lim:
                    node = node.right
                    check = True
                else:
                    node = node.left
            elif bit ^ 0:  # bit==1
                if node.left is not None and node.left.mi <= lim:
                    node = node.left
                    check = True
                else:
                    node = node.right
            ans = (ans << 1) | check
        return ans


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie2 = Trie2()
        for num in nums:
            trie2.insert(num)
        ans = []
        for val, lim in queries:
            ans.append(trie2.get_max_xor(val, lim))
        return ans


Solution().maximizeXor([5, 2, 4, 6, 6, 3], [[12, 4], [8, 1], [6, 3]])
from typing import List
