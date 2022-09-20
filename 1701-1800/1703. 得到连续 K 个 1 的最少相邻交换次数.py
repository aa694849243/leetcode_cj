import collections, heapq, itertools
from typing import List
# 给你一个整数数组 nums 和一个整数 k 。 nums 仅包含 0 和 1 。每一次移动，你可以选择 相邻 两个数字并将它们交换。
#
#  请你返回使 nums 中包含 k 个 连续 1 的 最少 交换次数。
#
#
#
#  示例 1：
#
#  输入：nums = [1,0,0,1,0,1], k = 2
# 输出：1
# 解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。
#
#
#  示例 2：
#
#  输入：nums = [1,0,0,0,0,0,1,1], k = 3
# 输出：5
# 解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。
#
#
#  示例 3：
#
#  输入：nums = [1,1,0,1], k = 2
# 输出：0
# 解释：nums 已经有连续 2 个 1 了。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  nums[i] 要么是 0 ，要么是 1 。
#  1 <= k <= sum(nums)
#
#
#  Related Topics 贪心 数组 前缀和 滑动窗口 👍 54 👎 0

# https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solution/de-dao-lian-xu-k-ge-1-de-zui-shao-xiang-lpa9i/
# 求差值同时抬高，滑动窗口不必重置
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        prefix_cum = [0]
        cnt = -1
        g = []
        for i, num in enumerate(nums):
            if num == 1:
                cnt += 1
                g.append(i - cnt)
                prefix_cum.append(prefix_cum[-1] + g[-1])
        m = len(g)  # 1的数量
        ans = float('inf')
        for i in range(m - k + 1):
            mid = (i + i + k - 1) // 2
            q = g[mid]
            ans = min(ans,(2 * (mid - i) - k + 1) * q + (prefix_cum[k + i] - prefix_cum[mid + 1])-(prefix_cum[mid]-prefix_cum[i]))
        return ans
