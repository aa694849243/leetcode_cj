# -*- coding: utf-8 -*-
# 给你一个下表从 0 开始的整数数组 nums 。每次操作中，你可以将数组中任何一个元素替换为 任意两个 和为该元素的数字。
#
#
#  比方说，nums = [5,6,7] 。一次操作中，我们可以将 nums[1] 替换成 2 和 4 ，将 nums 转变成 [5,2,4,7] 。
#
#
#  请你执行上述操作，将数组变成元素按 非递减 顺序排列的数组，并返回所需的最少操作次数。
#
#
#
#  示例 1：
#
#
# 输入：nums = [3,9,3]
# 输出：2
# 解释：以下是将数组变成非递减顺序的步骤：
# - [3,9,3] ，将9 变成 3 和 6 ，得到数组 [3,3,6,3]
# - [3,3,6,3] ，将 6 变成 3 和 3 ，得到数组 [3,3,3,3,3]
# 总共需要 2 步将数组变成非递减有序，所以我们返回 2 。
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3,4,5]
# 输出：0
# 解释：数组已经是非递减顺序，所以我们返回 0 。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  1 <= nums[i] <= 10⁹
#
#
#  Related Topics 贪心 数组 数学
#  👍 20 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        aft = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= aft:
                aft = nums[i]
                continue
            cnt = (nums[i] - 1) // aft  # 贪心，均匀递减，-1代表向下取整=号情况比如9，3和8，3情况是一样的
            ans += cnt
            aft = nums[i] // (cnt + 1)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().minimumReplacement([7, 2, 24, 11, 16, 1, 11, 23]))
