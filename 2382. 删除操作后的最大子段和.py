# -*- coding: utf-8 -*-
# 给你两个下标从 0 开始的整数数组 nums 和 removeQueries ，两者长度都为 n 。对于第 i 个查询，nums 中位于下标
# removeQueries[i] 处的元素被删除，将 nums 分割成更小的子段。
#
#  一个 子段 是 nums 中连续 正 整数形成的序列。子段和 是子段中所有元素的和。
#
#  请你返回一个长度为 n 的整数数组 answer ，其中 answer[i]是第 i 次删除操作以后的 最大 子段和。
#
#  注意：一个下标至多只会被删除一次。
#
#
#
#  示例 1：
#
#  输入：nums = [1,2,5,6,1], removeQueries = [0,3,2,4,1]
# 输出：[14,7,2,2,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 0 个元素，nums 变成 [0,2,5,6,1] ，最大子段和为子段 [2,5,6,1] 的和 14 。
# 查询 2 ：删除第 3 个元素，nums 变成 [0,2,5,0,1] ，最大子段和为子段 [2,5] 的和 7 。
# 查询 3 ：删除第 2 个元素，nums 变成 [0,2,0,0,1] ，最大子段和为子段 [2] 的和 2 。
# 查询 4 ：删除第 4 个元素，nums 变成 [0,2,0,0,0] ，最大子段和为子段 [2] 的和 2 。
# 查询 5 ：删除第 1 个元素，nums 变成 [0,0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [14,7,2,2,0] 。
#
#  示例 2：
#
#  输入：nums = [3,2,11,1], removeQueries = [3,2,1,0]
# 输出：[16,5,3,0]
# 解释：用 0 表示被删除的元素，答案如下所示：
# 查询 1 ：删除第 3 个元素，nums 变成 [3,2,11,0] ，最大子段和为子段 [3,2,11] 的和 16 。
# 查询 2 ：删除第 2 个元素，nums 变成 [3,2,0,0] ，最大子段和为子段 [3,2] 的和 5 。
# 查询 3 ：删除第 1 个元素，nums 变成 [3,0,0,0] ，最大子段和为子段 [3] 的和 3 。
# 查询 5 ：删除第 0 个元素，nums 变成 [0,0,0,0] ，最大子段和为 0 ，因为没有任何子段存在。
# 所以，我们返回 [16,5,3,0] 。
#
#
#
#
#  提示：
#
#
#  n == nums.length == removeQueries.length
#  1 <= n <= 10⁵
#  1 <= nums[i] <= 10⁹
#  0 <= removeQueries[i] < n
#  removeQueries 中所有数字 互不相同 。
#
#
#  Related Topics 并查集 数组 有序集合 前缀和
#  👍 20 👎 0

from typing import List
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class UnionFind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        self.f.setdefault(x, x)
        if self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a != b:
            self.f[b] = a


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        m = collections.defaultdict(int)
        vec = [0] * (n := len(nums))
        uf = UnionFind()
        res = [0]
        ma = 0
        for i in range(n - 1, -1, -1):
            idx = removeQueries[i]
            vec[idx] = 1
            if idx + 1 < n and vec[idx + 1] != 0:
                m[uf.find(idx)] += m[uf.find(idx + 1)]
                uf.union(idx, idx + 1)
            if idx - 1 >= 0 and vec[idx - 1] != 0:
                m[uf.find(idx - 1)] += m[uf.find(idx)]
                uf.union(idx - 1, idx)
            m[uf.find(idx)] += nums[idx]
            ma = max(ma, m[uf.find(idx)])
            res.append(ma)
        return res[::-1][1:]


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().maximumSegmentSum(
    [1, 2, 5, 6, 1],
    [0, 3, 2, 4, 1]
))
