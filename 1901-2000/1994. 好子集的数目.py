# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2022-09-23 2:39 
# ide： PyCharm
# 给你一个整数数组 nums 。如果 nums 的一个子集中，所有元素的乘积可以表示为一个或多个 互不相同的质数 的乘积，那么我们称它为 好子集 。
#
#
#  比方说，如果 nums = [1, 2, 3, 4] ：
#
#
#
#  [2, 3] ，[1, 2, 3] 和 [1, 3] 是 好 子集，乘积分别为 6 = 2*3 ，6 = 2*3 和 3 = 3 。
#  [1, 4] 和 [4] 不是 好 子集，因为乘积分别为 4 = 2*2 和 4 = 2*2 。
#
#
#
#
#  请你返回 nums 中不同的 好 子集的数目对 10⁹ + 7 取余 的结果。
#
#  nums 中的 子集 是通过删除 nums 中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视
# 为不同的子集。
#
#
#
#  示例 1：
#
#
# 输入：nums = [1,2,3,4]
# 输出：6
# 解释：好子集为：
# - [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
# - [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
# - [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
# - [2]：乘积为 2 ，可以表示为质数 2 的乘积。
# - [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
# - [3]：乘积为 3 ，可以表示为质数 3 的乘积。
#
#
#  示例 2：
#
#
# 输入：nums = [4,2,3,15]
# 输出：5
# 解释：好子集为：
# - [2]：乘积为 2 ，可以表示为质数 2 的乘积。
# - [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
# - [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
# - [3]：乘积为 3 ，可以表示为质数 3 的乘积。
# - [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 10⁵
#  1 <= nums[i] <= 30
#
#
#  Related Topics 位运算 数组 数学 动态规划 状态压缩 👍 133 👎 0
import collections
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        primes = [2, 3, 5, 7, 11, 13, 17, 18, 19, 23, 29]
        mod = 10 ** 9 + 7
        ns = len(primes)
        nums = [*filter(lambda x: x not in {4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28}, nums)]
        m = {2: [2], 3: [3], 5: [5], 6: [2, 3], 7: [7], 10: [2, 5], 11: [11], 13: [13], 14: [2, 7], 15: [3, 5], 17: [17],
             19: [19], 21: [3, 7], 22: [2, 11], 23: [23], 26: [2, 13], 29: [29], 30: [2, 3, 5]}
        m_ = {}
        for num in m:
            m_[num] = sum(1 << primes.index(x) for x in m[num])
        c = collections.Counter(nums)
        flag1 = c[1]
        dp = collections.defaultdict(int)
        dp[0] = 1
        for num in sorted(c):
            if num==1:
                continue
            tmp_dp = dp.copy()
            for status in dp:
                if status & m_[num] == 0:
                    tmp_dp[status | m_[num]] += dp[status] * c[num]
                    tmp_dp[status | m_[num]] %= mod
            dp = tmp_dp.copy()
        return (sum(dp.values()) - 1) * pow(2, flag1, mod) % mod


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numberOfGoodSubsets([30, 6, 5]))
