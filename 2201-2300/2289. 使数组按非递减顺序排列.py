# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始的整数数组 nums 。在一步操作中，移除所有满足 nums[i - 1] > nums[i] 的 nums[i] ，其中 0 <
# i < nums.length 。
#
#  重复执行步骤，直到 nums 变为 非递减 数组，返回所需执行的操作数。
#
#
#
#  示例 1：
#
#
# 输入：nums = [5,3,4,4,7,3,6,11,8,5,11]
# 输出：3
# 解释：执行下述几个步骤：
# - 步骤 1 ：[5,3,4,4,7,3,6,11,8,5,11] 变为 [5,4,4,7,6,11,11]
# - 步骤 2 ：[5,4,4,7,6,11,11] 变为 [5,4,7,11,11]
# - 步骤 3 ：[5,4,7,11,11] 变为 [5,7,11,11]
# [5,7,11,11] 是一个非递减数组，因此，返回 3 。
#
#
#  示例 2：
#
#
# 输入：nums = [4,5,7,7,13]
# 输出：0
# 解释：nums 已经是一个非递减数组，因此，返回 0 。
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
#  Related Topics 栈 数组 链表 单调栈
#  👍 95 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 分段弹出
from   typing   import   List
class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        st = []
        res = 0
        for num in nums:
            time = 0
            while st and st[-1][0] <= num:
                _, tmp_time = st.pop()
                time = max(time, tmp_time)
                res = max(res, time)
            if not st:
                st.append((num, 0))
            else:
                st.append((num, time + 1))
        for _, time in st:
            res = max(res, time)
        return res
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().totalSteps([5,3,4,4,7,3,6,11,8,5,11]))