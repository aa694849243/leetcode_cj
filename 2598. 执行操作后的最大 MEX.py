# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-09-02 22:47 
# ide： PyCharm
# 给你一个下标从 0 开始的整数数组 nums 和一个整数 value 。
#
#  在一步操作中，你可以对 nums 中的任一元素加上或减去 value 。
#
#
#  例如，如果 nums = [1,2,3] 且 value = 2 ，你可以选择 nums[0] 减去 value ，得到 nums = [-1,2,3]
# 。
#
#
#  数组的 MEX (minimum excluded) 是指其中数组中缺失的最小非负整数。
#
#
#  例如，[-1,2,3] 的 MEX 是 0 ，而 [1,0,3] 的 MEX 是 2 。
#
#
#  返回在执行上述操作 任意次 后，nums 的最大 MEX 。
#
#
#
#  示例 1：
#
#  输入：nums = [1,-10,7,13,6,8], value = 5
# 输出：4
# 解释：执行下述操作可以得到这一结果：
# - nums[1] 加上 value 两次，nums = [1,0,7,13,6,8]
# - nums[2] 减去 value 一次，nums = [1,0,2,13,6,8]
# - nums[3] 减去 value 两次，nums = [1,0,2,3,6,8]
# nums 的 MEX 是 4 。可以证明 4 是可以取到的最大 MEX 。
#
#
#  示例 2：
#
#  输入：nums = [1,-10,7,13,6,8], value = 7
# 输出：2
# 解释：执行下述操作可以得到这一结果：
# - nums[2] 减去 value 一次，nums = [1,-10,0,13,6,8]
# nums 的 MEX 是 2 。可以证明 2 是可以取到的最大 MEX 。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length, value <= 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#
#
#  Related Topics 贪心 数组 哈希表 数学
#  👍 16 👎 0

from typing import List
import collections
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        lst = []
        for num in nums:
            lst.append(num % value)
        c = collections.Counter(lst)
        x = min(c.values())
        for i in range(value):
            if c[i]==0:
                return i
        for i in range(value):
            if c[i]==x:
                return x*value+i


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findSmallestInteger([1, -10, 7, 13, 6, 8], 5),
)
