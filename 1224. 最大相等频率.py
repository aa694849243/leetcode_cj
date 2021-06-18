# -*- coding: utf-8 -*-
import collections
from typing import List


# 给出一个正整数数组 nums，请你帮忙从该数组中找出能满足下面要求的 最长 前缀，并返回其长度：
#
#
#  从前缀中 删除一个 元素后，使得所剩下的每个数字的出现次数相同。
#
#
#  如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。
#
#
#
#  示例 1：
#
#  输入：nums = [2,2,1,1,5,3,3,5]
# 输出：7
# 解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4]=5，就可以得到 [2,2,1,1,3,3]，里面每个数字都
# 出现了两次。
#
#
#  示例 2：
#
#  输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
# 输出：13
#
#
#  示例 3：
#
#  输入：nums = [1,1,1,2,2,2]
# 输出：5
#
#
#  示例 4：
#
#  输入：nums = [10,2,8,9,3,8,1,5,2,3,7,6]
# 输出：8
#
#
#
#
#  提示：
#
#
#  2 <= nums.length <= 10^5
#  1 <= nums[i] <= 10^5
#
#  Related Topics 哈希表
#  👍 43 👎 0

# https://leetcode-cn.com/problems/maximum-equal-frequency/solution/c-python3-fen-4chong-qing-kuang-xiang-qi-rb62/
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        species = 0  # 种类数
        ans = 1
        maxfreq = 0
        freq = collections.defaultdict(int)
        freq_freq = collections.defaultdict(int)  # 频率的频率
        for i, num in enumerate(nums):
            if freq[num] == 0:
                species += 1
            freq[num] += 1
            maxfreq = max(maxfreq, freq[num])
            freq_freq[freq[num]] += 1
            if freq[num] != 1:
                freq_freq[freq[num] - 1] -= 1
            if freq_freq[1] == species:  # 全不同的情况
                ans = max(ans, i+1)
            elif freq_freq[maxfreq - 1] == species - 1:
                ans = max(ans, i+1)
            elif freq_freq[1] == 1 and freq_freq[maxfreq] == species - 1:
                ans = max(ans, i+1)
        return ans
