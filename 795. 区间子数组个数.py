'''给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。

求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。

例如 :
输入:
A = [2, 1, 4, 3]
L = 2
R = 3
输出: 3
解释: 满足条件的子数组: [2], [2, 1], [3].
注意:

L, R  和 A[i] 都是整数，范围在 [0, 10^9]。
数组 A 的长度范围在[1, 50000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-subarrays-with-bounded-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 前缀和问题
# 最大元素满足，也就是所有元素都满足<R,减去全部元素都小于L
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        accum1 = 0
        accum2 = 0
        ans = 0
        for i in range(len(A)):
            if A[i] <= R:
                accum1 += 1
            else:
                accum1 = 0
            if A[i] < L:
                accum2 += 1
            else:
                accum2=0
            ans += accum1-accum2
        return ans


A = [1, 1, 4, 3]
L = 1
R = 2
Solution().numSubarrayBoundedMax(A, L, R)
