import collections, heapq, itertools
from typing import List


# 在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。
#
#  返回重复了 N 次的那个元素。
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：[1,2,3,3]
# 输出：3
#
#
#  示例 2：
#
#
# 输入：[2,1,2,5,3,2]
# 输出：2
#
#
#  示例 3：
#
#
# 输入：[5,1,5,2,5,3,5,4]
# 输出：5
#
#
#
#
#  提示：
#
#
#  4 <= A.length <= 10000
#  0 <= A[i] < 10000
#  A.length 为偶数
#
#  Related Topics 哈希表
#  👍 93 👎 0


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        if len(nums) <= 4:  # 数组长度为4，两个相同字母最远距离为3
            a = collections.Counter(nums)
            for i in a.keys():
                if a[i] >= 2:
                    return i
        for k in range(1, 3):  # 其他情况，距离为2的字母一定会在某处相同
            for i in range(len(nums) - k):
                if nums[i] == nums[i + k]:
                    return nums[i]
Solution().repeatedNTimes([1,2,3,3])