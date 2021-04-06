'''给定数组 nums 由正整数组成，找到三个互不重叠的子数组的最大和。

每个子数组的长度为k，我们要使这3*k个项的和最大化。

返回每个区间起始索引的列表（索引从 0 开始）。如果有多个结果，返回字典序最小的一个。

示例:

输入: [1,2,1,2,6,7,5,1], 2
输出: [0, 3, 5]
解释: 子数组 [1, 2], [2, 6], [7, 5] 对应的起始索引为 [0, 3, 5]。
我们也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。
注意:

nums.length的范围在[1, 20000]之间。
nums[i]的范围在[1, 65535]之间。
k的范围在[1, floor(nums.length / 3)]之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1特别动态规划
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        w = []
        x = 0
        for i in range(len(nums)):
            x += nums[i]
            if i >= k:
                x -= nums[i - k]
            if i >= k - 1:
                w.append(x)
        left = [0] * len(w)
        best = 0
        for i in range(len(w)):
            if w[i] > w[best]:
                best = i
            left[i] = best
        right = [0] * len(w)
        best = len(w) - 1
        for i in range(len(w) - 1, -1, -1):
            if w[i] >= w[best]:
                best = i
            right[i] = best
        ans = None
        m = float('-inf')
        for j in range(k, len(w) - k):
            a, b, c = left[j - k], j, right[j + k]
            if ans is None or w[a] + w[b] + w[c] > m:
                ans = [a, b, c]
                m = w[a] + w[b] + w[c]
        return ans
