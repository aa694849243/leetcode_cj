# -*- coding: utf-8 -*-
# 给你一个整数数组 nums 和一个整数 k 。
#
#  找到 nums 中满足以下要求的最长子序列：
#
#
#  子序列 严格递增
#  子序列中相邻元素的差值 不超过 k 。
#
#
#  请你返回满足上述要求的 最长子序列 的长度。
#
#  子序列 是从一个数组中删除部分元素后，剩余元素不改变顺序得到的数组。
#
#
#
#  示例 1：
#
#  输入：nums = [4,2,1,4,3,4,5,8,15], k = 3
# 输出：5
# 解释：
# 满足要求的最长子序列是 [1,3,4,5,8] 。
# 子序列长度为 5 ，所以我们返回 5 。
# 注意子序列 [1,3,4,5,8,15] 不满足要求，因为 15 - 8 = 7 大于 3 。
#
#
#  示例 2：
#
#  输入：nums = [7,4,5,1,8,12,4,7], k = 5
# 输出：4
# 解释：
# 满足要求的最长子序列是 [4,5,8,12] 。
# 子序列长度为 4 ，所以我们返回 4 。
#
#
#  示例 3：
#
#  输入：nums = [1,5], k = 1
# 输出：1
# 解释：
# 满足要求的最长子序列是 [1] 。
# 子序列长度为 1 ，所以我们返回 1 。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  1 <= nums[i], k <= 10⁵
#
#
#  Related Topics 树状数组 线段树 队列 数组 分治 动态规划 单调队列
#  👍 50 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 区间求最大值 线段树
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        u = max(nums)
        sgtree = [0] * (4 * u)

        def update(o, l, r, i, val):
            if l == r:
                sgtree[o] = val
                return
            m = (l + r) // 2
            if i <= m:
                update(o * 2, l, m, i, val)
            else:
                update(o * 2 + 1, m + 1, r, i, val)
            sgtree[o] = max(sgtree[o * 2], sgtree[o * 2 + 1])

        def query(o, l, r, L, R):
            if r < L or l > R:
                return 0
            if L <= l and r <= R:
                return sgtree[o]
            m = (l + r) // 2
            return max(query(o * 2, l, m, L, R), query(o * 2 + 1, m + 1, r, L, R))

        for x in nums:
            if x == 1:
                update(1, 1, u, 1, 1)
            else:
                res = query(1, 1, u, max(1, x - k), x - 1) + 1
                update(1, 1, u, x, res)
        return sgtree[1]

# leetcode submit region end(Prohibit modification and deletion)
