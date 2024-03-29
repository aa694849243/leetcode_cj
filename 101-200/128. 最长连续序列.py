'''
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 哈希表法
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsset = set(nums)
        maxsuccession = 0
        for i in numsset:
            if i - 1 in numsset:
                continue
            count = 1
            while i + 1 in numsset:
                count += 1
                i += 1
            maxsuccession=max(count,maxsuccession)
        return maxsuccession
