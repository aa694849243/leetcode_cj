# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一个数组 arr ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用 -1 替换。
#
#  完成所有替换操作后，请你返回这个数组。
#
#
#
#  示例 1：
#
#
# 输入：arr = [17,18,5,4,6,1]
# 输出：[18,6,6,6,1,-1]
# 解释：
# - 下标 0 的元素 --> 右侧最大元素是下标 1 的元素 (18)
# - 下标 1 的元素 --> 右侧最大元素是下标 4 的元素 (6)
# - 下标 2 的元素 --> 右侧最大元素是下标 4 的元素 (6)
# - 下标 3 的元素 --> 右侧最大元素是下标 4 的元素 (6)
# - 下标 4 的元素 --> 右侧最大元素是下标 5 的元素 (1)
# - 下标 5 的元素 --> 右侧没有其他元素，替换为 -1
#
#
#  示例 2：
#
#
# 输入：arr = [400]
# 输出：[-1]
# 解释：下标 0 的元素右侧没有其他元素。
#
#
#
#
#  提示：
#
#
#  1 <= arr.length <= 104
#  1 <= arr[i] <= 105
#
#  Related Topics 数组
#  👍 63 👎 0


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        stack=[]
        for i in range(len(arr)-1,-1,-1):
            if not stack:
                stack.append(arr[i])
            else:
                stack.append(max(arr[i],stack[-1]))
        return stack[::-1][1:]+[-1]