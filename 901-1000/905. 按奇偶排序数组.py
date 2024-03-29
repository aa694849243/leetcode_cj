# 给定一个非负整数数组 A，返回一个数组，在该数组中， A 的所有偶数元素之后跟着所有奇数元素。
#
#  你可以返回满足此条件的任何数组作为答案。
#
#
#
#  示例：
#
#  输入：[3,1,2,4]
# 输出：[2,4,3,1]
# 输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。
#
#
#
#
#  提示：
#
#
#  1 <= A.length <= 5000
#  0 <= A[i] <= 5000
#
#  Related Topics 数组
#  👍 206 👎 0

from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A, key=lambda x: x % 2)


# 2快速排序+双指针
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            else:
                if A[i] % 2 and A[j] % 2:  # 两个都为奇数，最终i位置不变，j要-=1
                    i -= 1
                elif not (A[i] % 2 or A[j] % 2):  # 两个都为偶数，最终j位置不变，i要+=1
                    j += 1
            j -= 1
            i += 1
        return A
Solution().sortArrayByParity([3,1,2,4])