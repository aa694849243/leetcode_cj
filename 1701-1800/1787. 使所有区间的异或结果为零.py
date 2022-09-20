# -*- coding: utf-8 -*-
# 给你一个整数数组 nums 和一个整数 k 。区间 [left, right]（left <= right）的 异或结果 是对下标位于 left 和
# right（包括 left 和 right ）之间所有元素进行 XOR 运算的结果：nums[left] XOR nums[left+1] XOR ... XOR
# nums[right] 。
#
#  返回数组中 要更改的最小元素数 ，以使所有长度为 k 的区间异或结果等于零。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,0,3,0], k = 1
# 输出：3
# 解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]
#
#
#  示例 2：
#
#
# 输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
# 输出：3
# 解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]
#
#
#  示例 3：
#
#
# 输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
# 输出：3
# 解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3]
#
#
#
#  提示：
#
#
#  1 <= k <= nums.length <= 2000
#  0 <= nums[i] < 2¹⁰
#
#
#  Related Topics 位运算 数组 动态规划 👍 134 👎 0
import collections
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        MAXX = 2 ** 10
        f = [float('inf')] * MAXX
        f[0] = 0 # f初始状态为f(-1) 此时只有0是合法的，其他值都不存在，给他们赋予一个极大值
        for i in range(k):
            size = 0
            c = collections.Counter()
            for j in range(i, len(nums), k):
                size += 1
                c[nums[j]] += 1
            t2min = min(f)
            nxt_f = [t2min] * MAXX
            for mask in range(MAXX):
                for x, x_cnt in c.items():
                    nxt_f[mask] = min(nxt_f[mask], f[x ^ mask] - x_cnt)
            f = [val + size for val in nxt_f]
        return f[0]
# author： caoji
# datetime： 2022-08-28 14:27 
# ide： PyCharm
