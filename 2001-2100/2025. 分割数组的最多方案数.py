# -*- coding: utf-8 -*-
# 给你一个下标从 0 开始且长度为 n 的整数数组 nums 。分割 数组 nums 的方案数定义为符合以下两个条件的 pivot 数目：
#
#
#  1 <= pivot < n
#  nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] +
# ... + nums[n - 1]
#
#
#  同时给你一个整数 k 。你可以将 nums 中 一个 元素变为 k 或 不改变 数组。
#
#  请你返回在 至多 改变一个元素的前提下，最多 有多少种方法 分割 nums 使得上述两个条件都满足。
#
#
#
#  示例 1：
#
#  输入：nums = [2,-1,2], k = 3
# 输出：1
# 解释：一个最优的方案是将 nums[0] 改为 k 。数组变为 [3,-1,2] 。
# 有一种方法分割数组：
# - pivot = 2 ，我们有分割 [3,-1 | 2]：3 + -1 == 2 。
#
#
#  示例 2：
#
#  输入：nums = [0,0,0], k = 1
# 输出：2
# 解释：一个最优的方案是不改动数组。
# 有两种方法分割数组：
# - pivot = 1 ，我们有分割 [0 | 0,0]：0 == 0 + 0 。
# - pivot = 2 ，我们有分割 [0,0 | 0]: 0 + 0 == 0 。
#
#
#  示例 3：
#
#  输入：nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
# 输出：4
# 解释：一个最优的方案是将 nums[2] 改为 k 。数组变为 [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14] 。
#
# 有四种方法分割数组。
#
#
#
#
#  提示：
#
#
#  n == nums.length
#  2 <= n <= 10⁵
#  -10⁵ <= k, nums[i] <= 10⁵
#
#
#  Related Topics 数组 哈希表 计数 枚举 前缀和 👍 27 👎 0
import bisect
import collections

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        presum = [nums[0]]
        for i in range(1, len(nums)):
            presum.append(presum[i - 1] + nums[i])
        diffs = [k - num for num in nums]
        md = collections.defaultdict(list)
        for i, diff in enumerate(diffs):
            md[diff].append(i)
        ans = 0
        m = collections.defaultdict(int)
        for i in range(len(nums) - 1):
            left = presum[i]
            right = presum[-1] - presum[i]
            if left == right:
                ans += 1
            else:
                d = right - left
                for k in md[d]:
                    if k <= i:
                        m[k] += 1
                    else:
                        break
                idx = bisect.bisect_right(md[-d], i)
                for k in md[-d][idx:]:
                    if k > i:
                        m[k] += 1
        return max(ans, max(m.values())) if m else ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().waysToPartition(nums=[22, 4, -25, -20, -15, 15, -16, 7, 19, -10, 0, -13, -14], k=-33))
