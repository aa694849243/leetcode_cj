import collections, heapq, itertools
from typing import List


# 给定一个整数数组 A，坡是元组 (i, j)，其中 i < j 且 A[i] <= A[j]。这样的坡的宽度为 j - i。
#
#  找出 A 中的坡的最大宽度，如果不存在，返回 0 。
#
#
#
#  示例 1：
#
#  输入：[6,0,8,2,1,5]
# 输出：4
# 解释：
# 最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.
#
#
#  示例 2：
#
#  输入：[9,8,1,0,1,9,4,0,4,1]
# 输出：7
# 解释：
# 最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.
#
#
#
#
#  提示：
#
#
#  2 <= A.length <= 50000
#  0 <= A[i] <= 50000
#
#
#
#  Related Topics 数组
#  👍 116 👎 0

# 提取索引
# 根据真实值提取索引，保留最左端的索引，每次计算最大宽度，由于是根据真实值递增的提取索引，所以每次计算都是有效的
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        mindex = float('inf')
        for index in sorted(list(range(n := len(nums))), key=nums.__getitem__):
            ans = max(index - mindex, ans)
            mindex = min(index, mindex)
        return ans


# 类单调栈
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        ans = 0
        stack = []
        for i, num in enumerate(nums):
            if not stack:
                stack.append((i, num))
            else:
                if num < stack[-1][1]:
                    stack.append((i, num))
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[i] >= stack[-1][1]:
                ans = max(ans, i - stack[-1][0])
                stack.pop()
                if not stack:  # 栈空，提前结束
                    return ans
        return ans
