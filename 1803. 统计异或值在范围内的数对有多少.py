# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-08-31 0:10 
# ide： PyCharm
# 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
#
#  漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[
# j]) <= high 。
#
#
#
#  示例 1：
#
#  输入：nums = [1,4,2,7], low = 2, high = 6
# 输出：6
# 解释：所有漂亮数对 (i, j) 列出如下：
#     - (0, 1): nums[0] XOR nums[1] = 5
#     - (0, 2): nums[0] XOR nums[2] = 3
#     - (0, 3): nums[0] XOR nums[3] = 6
#     - (1, 2): nums[1] XOR nums[2] = 6
#     - (1, 3): nums[1] XOR nums[3] = 3
#     - (2, 3): nums[2] XOR nums[3] = 5
#
#
#  示例 2：
#
#  输入：nums = [9,8,4,2,1], low = 5, high = 14
# 输出：8
# 解释：所有漂亮数对 (i, j) 列出如下：
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
#     - (0, 3): nums[0] XOR nums[3] = 11
#     - (0, 4): nums[0] XOR nums[4] = 8
#     - (1, 2): nums[1] XOR nums[2] = 12
#     - (1, 3): nums[1] XOR nums[3] = 10
#     - (1, 4): nums[1] XOR nums[4] = 9
#     - (2, 3): nums[2] XOR nums[3] = 6
#     - (2, 4): nums[2] XOR nums[4] = 5
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 10⁴
#  1 <= nums[i] <= 2 * 10⁴
#  1 <= low <= high <= 2 * 10⁴
#
#
#  Related Topics 位运算 字典树 数组 👍 51 👎 0
from typing import List

# 二进制字典树 二进制前缀树
# leetcode submit region begin(Prohibit modification and deletion)
class BitTrie:
    L = 14  # 可以表示15位的二进制数，可偏移14位表示15位数，root节点为空节点

    def __init__(self):
        self.left = None
        self.right = None
        self.cnt = 0

    def insert(self, val):
        node = self
        for off in range(BitTrie.L, -1, -1):
            node.cnt += 1  # 每插入一个值，整个路径上所有节点数目计数+1
            if (val >> off) & 1:
                if node.right is None:
                    node.right = BitTrie()
                node = node.right
            else:
                if node.left is None:
                    node.left = BitTrie()
                node = node.left
        node.cnt += 1  # 叶子节点的计数+1


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def get_xor_num(val, off, prefix, trie: BitTrie):  # val查询的值，off偏移量，prefix前缀，trie二进制数
            if off == 0:
                if low <= prefix <= high:
                    return trie.cnt
            ma = ((prefix + 1) << off) - 1  # prefix取值后最大的值
            mi = prefix << off  # prefix取值后最小的值
            if ma < low or mi > high:
                return 0
            elif low <= mi <= ma <= high:
                return trie.cnt
            p_val = (val >> (off - 1)) & 1  # 当前值的二进制位,一开始偏移14位，可表示15位的二进制数，与前缀树对齐
            res = 0
            if trie.left is not None:
                res += get_xor_num(val, off - 1, (prefix << 1) + (p_val ^ 0), trie.left)
            if trie.right is not None:
                res += get_xor_num(val, off - 1, (prefix << 1) + (p_val ^ 1), trie.right)
            return res

        t = BitTrie()
        ans = 0
        for num in nums:
            ans += get_xor_num(num, 15, 0, t)
            t.insert(num)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countPairs([1, 4, 2, 7], 2, 6))
t = Trie()
t.insert(7)
...
