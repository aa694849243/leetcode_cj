#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 有一个整数数组 nums ，和一个查询数组 requests ，其中 requests[i] = [starti, endi] 。第 i 个查询求 nums
# [starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi] 的结果 ，starti 和 en
# di 数组索引都是 从 0 开始 的。
#
#  你可以任意排列 nums 中的数字，请你返回所有查询结果之和的最大值。
#
#  由于答案可能会很大，请你将它对 109 + 7 取余 后返回。
#
#
#
#  示例 1：
#
#  输入：nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
# 输出：19
# 解释：一个可行的 nums 排列为 [2,1,3,4,5]，并有如下结果：
# requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
# requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
# 总和为：8 + 3 = 11。
# 一个总和更大的排列为 [3,5,4,2,1]，并有如下结果：
# requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
# requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
# 总和为： 11 + 8 = 19，这个方案是所有排列中查询之和最大的结果。
#
#
#  示例 2：
#
#  输入：nums = [1,2,3,4,5,6], requests = [[0,1]]
# 输出：11
# 解释：一个总和最大的排列为 [6,5,4,3,2,1] ，查询和为 [11]。
#
#  示例 3：
#
#  输入：nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
# 输出：47
# 解释：一个和最大的排列为 [4,10,5,3,2,1] ，查询结果分别为 [19,18,10]。
#
#
#
#  提示：
#
#
#  n == nums.length
#  1 <= n <= 105
#  0 <= nums[i] <= 105
#  1 <= requests.length <= 105
#  requests[i].length == 2
#  0 <= starti <= endi < n
#
#  Related Topics 贪心 数组 前缀和 排序
#  👍 44 👎 0

# 经典差分
class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        cnts = [0] * (n := len(nums))
        for s, e in requests:
            cnts[s] += 1
            if e + 1 < n:
                cnts[e + 1] -= 1

        for i in range(1, n):
            cnts[i] += cnts[i - 1]
        cnts.sort()
        nums.sort()
        return sum(cnt * num for cnt, num in zip(cnts, nums)) % mod
Solution().maxSumRangeQuery([1,2,3,4,5],[[1,3],[0,1]])