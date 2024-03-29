import collections, heapq, itertools
from typing import List


# 给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。
#
#  返回使 A 中的每个值都是唯一的最少操作次数。
#
#  示例 1:
#
#  输入：[1,2,2]
# 输出：1
# 解释：经过一次 move 操作，数组将变为 [1, 2, 3]。
#
#  示例 2:
#
#  输入：[3,2,1,2,1,7]
# 输出：6
# 解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
# 可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
#
#
#  提示：
#
#
#  0 <= A.length <= 40000
#  0 <= A[i] < 40000
#
#  Related Topics 数组
#  👍 172 👎 0


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        move = 0
        for i, num in enumerate(nums[1:], 1):
            if num == nums[i - 1]:
                move += 1
                nums[i]+=1
            elif num<nums[i-1]:
                a=(nums[i-1]-num)+1
                move+=a
                nums[i]+=a
        return move
