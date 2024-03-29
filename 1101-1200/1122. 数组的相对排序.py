# -*- coding: utf-8 -*-
import collections
from typing import List


# 给你两个数组，arr1 和 arr2，
#
#
#  arr2 中的元素各不相同
#  arr2 中的每个元素都出现在 arr1 中
#
#
#  对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末
# 尾。
#
#
#
#  示例：
#
#
# 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
# 输出：[2,2,2,1,4,3,3,9,6,7,19]
#
#
#
#
#  提示：
#
#
#  1 <= arr1.length, arr2.length <= 1000
#  0 <= arr1[i], arr2[i] <= 1000
#  arr2 中的元素 arr2[i] 各不相同
#  arr2 中的每个元素 arr2[i] 都出现在 arr1 中
#
#  Related Topics 排序 数组
#  👍 177 👎 0


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = collections.defaultdict(lambda: 1000)
        for i, num in enumerate(arr2):
            m[num] = i
        arr1.sort(key=lambda x: (m[x],x))
        return arr1