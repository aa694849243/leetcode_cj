# 给你一个整数数组 nums 以及两个整数 lower 和 upper 。求数组中，值位于范围 [lower, upper] （包含 lower 和
# upper）之内的 区间和的个数 。
#
#  区间和 S(i, j) 表示在 nums 中，位置从 i 到 j 的元素之和，包含 i 和 j (i ≤ j)。
#
#
# 示例 1：
#
#
# 输入：nums = [-2,5,-1], lower = -2, upper = 2
# 输出：3
# 解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。
#
#
#  示例 2：
#
#
# 输入：nums = [0], lower = 0, upper = 0
# 输出：1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  -2³¹ <= nums[i] <= 2³¹ - 1
#  -10⁵ <= lower <= upper <= 10⁵
#  题目数据保证答案是一个 32 位 的整数
#
#
#  Related Topics 树状数组 线段树 数组 二分查找 分治 有序集合 归并排序
#  👍 557 👎 0
import bisect


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre_sum = [0] + list(accumulate(nums))
        lst = []
        ans = 0
        for x in pre_sum:
            l_idx = bisect.bisect_left(lst, x - upper)
            r_idx = bisect.bisect_right(lst, x - lower)
            bisect.insort(lst, x)
            ans += r_idx - l_idx
        return ans
# leetcode submit region end(Prohibit modification and deletion)
