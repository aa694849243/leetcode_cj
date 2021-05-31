import collections, heapq, itertools

from typing import List


# 给定一个整数数组 arr，如果它是有效的山脉数组就返回 true，否则返回 false。
#
#  让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
#
#
#  arr.length >= 3
#  在 0 < i < arr.length - 1 条件下，存在 i 使得：
#
#  arr[0] < arr[1] < ... arr[i-1] < arr[i]
#  arr[i] > arr[i+1] > ... > arr[arr.length - 1]
#
#
#
#
#
#
#
#
#
#
#  示例 1：
#
#
# 输入：arr = [2,1]
# 输出：false
#
#
#  示例 2：
#
#
# 输入：arr = [3,5,5]
# 输出：false
#
#
#  示例 3：
#
#
# 输入：arr = [0,3,2,1]
# 输出：true
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 104
#  0 <= arr[i] <= 104
#
#  Related Topics 数组
#  👍 144 👎 0


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        stack1 = []
        stack2 = []
        for i, val in enumerate(arr):
            if not stack1:
                stack1.append(val)
            elif not stack2:
                if val == stack1[-1]:
                    return False
                elif val > stack1[-1]:
                    stack1.append(val)
                else:
                    if len(stack1)<2:
                        return False
                    stack2.append(val)
            else:
                if val >= stack2[-1]:
                    return False
                else:
                    stack2.append(val)
        return True if len(stack2) > 0 and len(stack1) > 1 else False


Solution().validMountainArray([0,3,2,1])
