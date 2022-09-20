# -*- coding: utf-8 -*-
# 特殊序列 是由 正整数 个 0 ，紧接着 正整数 个 1 ，最后 正整数 个 2 组成的序列。
#
#
#  比方说，[0,1,2] 和 [0,0,1,1,1,2] 是特殊序列。
#  相反，[2,1,0] ，[1] 和 [0,1,2,0] 就不是特殊序列。
#
#
#  给你一个数组 nums （仅 包含整数 0，1 和 2），请你返回 不同特殊子序列的数目 。由于答案可能很大，请你将它对 10⁹ + 7 取余 后返回。
#
#
#  一个数组的 子序列 是从原数组中删除零个或者若干个元素后，剩下元素不改变顺序得到的序列。如果两个子序列的 下标集合 不同，那么这两个子序列是 不同的 。
#
#
#
#
#  示例 1：
#
#
# 输入：nums = [0,1,2,2]
# 输出：3
# 解释：特殊子序列为 [0,1,2,2]，[0,1,2,2] 和 [0,1,2,2] 。
#
#
#  示例 2：
#
#
# 输入：nums = [2,2,0,0]
# 输出：0
# 解释：数组 [2,2,0,0] 中没有特殊子序列。
#
#
#  示例 3：
#
#
# 输入：nums = [0,1,2,0,1,2]
# 输出：7
# 解释：特殊子序列包括：
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
# - [0,1,2,0,1,2]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  0 <= nums[i] <= 2
#
#
#  Related Topics 数组 动态规划 👍 24 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def countSpecialSubsequences(self, nums: List[int]) -> int:
        mod=10**9+7
        f0=f1=f2=0
        for num in nums:
            if num==0:
                f0=2*f0+1
            elif num==1:
                f1=2*f1+f0
            else:
                f2=2*f2+f1
        return f2%mod
# leetcode submit region end(Prohibit modification and deletion)
