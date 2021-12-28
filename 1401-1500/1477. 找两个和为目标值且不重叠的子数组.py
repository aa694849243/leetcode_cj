#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。
#
#
#  示例 3：
#
#  输入：arr = [4,3,2,6,2,3,4], target = 6
# 输出：-1
# 解释：我们只有一个和为 6 的子数组。
#
#
#  示例 4：
#
#  输入：arr = [5,5,4,4,5], target = 3
# 输出：-1
# 解释：我们无法找到和为 3 的子数组。
#
#
#  示例 5：
#
#  输入：arr = [3,1,1,1,5,1,2,1], target = 3
# 输出：3
# 解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 10^5
#  1 <= arr[i] <= 1000
#  1 <= target <= 10^8
#
#  Related Topics 数组 哈希表 二分查找 动态规划 滑动窗口
#  👍 88 👎 0

# https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/solution/biao-zhun-de-dong-tai-gui-hua-zhu-xing-jiang-jie-b/
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        pre = {0: -1}  # 储存累加和节点
        dp = [float('inf')] * len(arr)  # dp储存当前节点满足要求的最小长度
        p = 0  # 当前值
        res = float('inf')
        for i, val in enumerate(arr):
            p += val
            dp[i] = dp[i - 1]  # 与后面dp[p-target]!=float('inf')联合起来看，可以避免数组重叠
            if p - target in pre:  # 当前节点与之前某个节点相减可以满足target
                dis = i - pre[p - target]  # 当前节点满足条件的长度
                dp[i] = min(dp[i], dis)
                if pre[p - target] > -1 and dp[pre[p - target]] != float('inf'):  # 避免重叠,pre[p-target]>-1避免只有一个元素的情况会反身到原位置
                    tmp = dis + dp[pre[p - target]]
                    res = min(tmp, res)
            pre[p] = i
        return res if res != float('inf') else -1


Solution().minSumOfLengths([1], 1)
