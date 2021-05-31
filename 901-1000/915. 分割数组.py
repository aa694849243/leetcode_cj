# 给定一个数组 A，将其划分为两个连续子数组 left 和 right， 使得：
#
#
#  left 中的每个元素都小于或等于 right 中的每个元素。
#  left 和 right 都是非空的。
#  left 的长度要尽可能小。
#
#
#  在完成这样的分组后返回 left 的长度。可以保证存在这样的划分方法。
#
#
#
#  示例 1：
#
#
# 输入：[5,0,3,8,6]
# 输出：3
# 解释：left = [5,0,3]，right = [8,6]
#
#
#  示例 2：
#
#
# 输入：[1,1,1,0,6,12]
# 输出：4
# 解释：left = [1,1,1,0]，right = [6,12]
#
#
#
#
#  提示：
#
#
#  2 <= A.length <= 30000
#  0 <= A[i] <= 10^6
#  可以保证至少有一种方法能够按题目所描述的那样对 A 进行划分。
#
#
#
#  Related Topics 数组
#  👍 70 👎 0

from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        stack = []
        right = []
        for i, val in enumerate(A[::-1]):
            if not right:
                right.append(val)
            else:
                right.append(min(val, right[-1]))
        right = right[::-1]
        stack.append(A[0])
        for i, val in enumerate(A[1:], 1):
            while stack and right[i] >= stack[-1]:
                stack.pop()
            if not stack:
                return i
            stack.append(val)

Solution().partitionDisjoint([1,1,1,0,6,12])