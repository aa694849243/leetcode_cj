# -*- coding: utf-8 -*-
# 给你两个下标从 0 开始且长度为 n 的整数数组 nums1 和 nums2 ，两者都是 [0, 1, ..., n - 1] 的 排列 。
#
#  好三元组 指的是 3 个 互不相同 的值，且它们在数组 nums1 和 nums2 中出现顺序保持一致。换句话说，如果我们将 pos1v 记为值 v 在
# nums1 中出现的位置，pos2v 为值 v 在 nums2 中的位置，那么一个好三元组定义为 0 <= x, y, z <= n - 1 ，且 pos1x
# < pos1y < pos1z 和 pos2x < pos2y < pos2z 都成立的 (x, y, z) 。
#
#  请你返回好三元组的 总数目 。
#
#
#
#  示例 1：
#
#  输入：nums1 = [2,0,1,3], nums2 = [0,1,2,3]
# 输出：1
# 解释：
# 总共有 4 个三元组 (x,y,z) 满足 pos1x < pos1y < pos1z ，分别是 (2,0,1) ，(2,0,3) ，(2,1,3) 和 (
# 0,1,3) 。
# 这些三元组中，只有 (0,1,3) 满足 pos2x < pos2y < pos2z 。所以只有 1 个好三元组。
#
#
#  示例 2：
#
#  输入：nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
# 输出：4
# 解释：总共有 4 个好三元组 (4,0,3) ，(4,0,2) ，(4,1,3) 和 (4,1,2) 。
#
#
#
#
#  提示：
#
#
#  n == nums1.length == nums2.length
#  3 <= n <= 10⁵
#  0 <= nums1[i], nums2[i] <= n - 1
#  nums1 和 nums2 是 [0, 1, ..., n - 1] 的排列。
#
#
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序
#  👍 38 👎 0

# leetcode submit region begin(Prohibit modification and deletion)
class Ftree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def update(self, x, val):
        while x <= self.n:
            self.tree[x] += val
            x += self.lowbit(x)

    def query(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= self.lowbit(x)
        return res


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        g = [0] * len(nums1)
        for i, num in enumerate(nums1):
            g[num] = i + 1
        ftree = Ftree(len(nums1))
        res = 0
        n = len(nums1)
        for i, num in enumerate(nums2):
            left = ftree.query(g[num] - 1)
            left_sum = i
            rank = g[num]  # 当前数排名
            right = (n - rank) - (left_sum - left)  # 右边比当前数大的数个数
            res += left * right
            ftree.update(rank, 1)
        return res
# leetcode submit region end(Prohibit modification and deletion)
