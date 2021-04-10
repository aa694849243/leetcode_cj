# 给定的整数数组 A ，我们要将 A数组 中的每个元素移动到 B数组 或者 C数组中。（B数组和C数组在开始的时候都为空）
#
#  返回true ，当且仅当在我们的完成这样的移动后，可使得B数组的平均值和C数组的平均值相等，并且B数组和C数组都不为空。
#
#
# 示例:
# 输入:
# [1,2,3,4,5,6,7,8]
# 输出: true
# 解释: 我们可以将数组分割为 [1,4,5,8] 和 [2,3,6,7], 他们的平均值都是4.5。
#
#
#  注意:
#
#
#  A 数组的长度范围为 [1, 30].
#  A[i] 的数据范围为 [0, 10000].
#
#  Related Topics 数学
#  👍 63 👎 0

from typing import List
# meet in the middle
from fractions import Fraction  # 用分数，因为小数会存在精度问题，如果没有分数，可以使用*len使其变为整数


# 利用公式求出A平均值与B平均值相等

class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        av = Fraction(sum(nums), n)
        A = [nums[i] - av for i in range(n)]
        if n==1: return False
        left = {A[0]}
        for i in range(1, n // 2):
            left = {z + A[i] for z in left} | left | {A[i]}
        if 0 in left:
            return True
        right = {A[-1]}
        for i in range(n // 2, n - 1):
            right = {z + A[i] for z in right} | right | {A[i]}
        if 0 in right:
            return True
        sleft = sum(A[:n // 2])
        sright = sum(A[n // 2:])
        return True if any(-c in left and (sleft, sright) != (-c, c) for c in right) else False
Solution().splitArraySameAverage([1,2,3,4,5,6,7,8])