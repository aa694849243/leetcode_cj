# -*- coding: utf-8 -*-
# 给定正整数 K，你需要找出可以被 K 整除的、仅包含数字 1 的最小正整数 N。
#
#  返回 N 的长度。如果不存在这样的 N，就返回 -1。
#
#
#
#  示例 1：
#
#  输入：1
# 输出：1
# 解释：最小的答案是 N = 1，其长度为 1。
#
#  示例 2：
#
#  输入：2
# 输出：-1
# 解释：不存在可被 2 整除的正整数 N 。
#
#  示例 3：
#
#  输入：3
# 输出：3
# 解释：最小的答案是 N = 111，其长度为 3。
#
#
#
#  提示：
#
#
#  1 <= K <= 10^5
#
#  Related Topics 数学
#  👍 35 👎 0

# https://leetcode-cn.com/problems/smallest-integer-divisible-by-k/solution/javajie-fa-yi-ji-zheng-ming-de-si-lu-by-jiangzk/
# 红笔记
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        a = str(k)
        if a[-1] not in ['1', '3', '7', '9']:
            return -1
        ans = 1
        s = 1
        while s % k != 0:
            s %= k
            s = s * 10 + 1
            ans += 1
        return ans
