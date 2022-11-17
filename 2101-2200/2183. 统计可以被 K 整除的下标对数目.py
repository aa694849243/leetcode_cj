# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始、长度为 n 的整数数组 nums 和一个整数 k ，返回满足下述条件的下标对 (i, j) 的数目：
#
#
#  0 <= i < j <= n - 1 且
#  nums[i] * nums[j] 能被 k 整除。
#
#
#
#
#  示例 1：
#
#  输入：nums = [1,2,3,4,5], k = 2
# 输出：7
# 解释：
# 共有 7 对下标的对应积可以被 2 整除：
# (0, 1)、(0, 3)、(1, 2)、(1, 3)、(1, 4)、(2, 3) 和 (3, 4)
# 它们的积分别是 2、4、6、8、10、12 和 20 。
# 其他下标对，例如 (0, 2) 和 (2, 4) 的乘积分别是 3 和 15 ，都无法被 2 整除。
#
#
#  示例 2：
#
#  输入：nums = [1,2,3,4], k = 5
# 输出：0
# 解释：不存在对应积可以被 5 整除的下标对。
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
#  Related Topics 数组 数学 数论
#  👍 46 👎 0
import collections

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# 组合去重
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x % y)

        m = collections.Counter()
        for num in nums:
            m[gcd(num, k)] += 1
        res = 0
        for num1 in m:
            for num2 in m:
                if num1 * num2 % k == 0:
                    res += m[num1] * m[num2]
        for num in nums:
            if num * num % k == 0:
                res -= 1
        return res // 2


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countPairs([3,6,9], 1))
