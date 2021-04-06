'''如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从0开始。数组 A 的一个子数组划分为数组 (P, Q)，P 与 Q 是整数且满足 0<=P<Q<N 。

如果满足以下条件，则称子数组(P, Q)为等差数组：

元素 A[P], A[p + 1], ..., A[Q - 1], A[Q] 是等差的。并且 P + 1 < Q 。

函数要返回数组 A 中所有为等差数组的子数组个数。

 

示例:

A = [1, 2, 3, 4]

返回: 3, A 中有三个子等差数组: [1, 2, 3], [2, 3, 4] 以及自身 [1, 2, 3, 4]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1递归
class Solution:
    sum = 0

    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) <= 2:
            return 0

        def rec(l, i):
            if i <= 2:
                a = int(l[0] + l[2] == 2 * l[1])
                self.sum += a
                return a
            if l[i] - l[i - 1] == l[i - 1] - l[i - 2]:
                a = rec(l, i - 1) + 1
                self.sum += a
                return a
            else:
                rec(l, i - 1)
                return 0

        rec(A, len(A) - 1)
        return self.sum


# 2动态规划
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) <= 2:
            return 0
        sum = 0
        dp = [0, 0]
        for i in range(2, len(A)):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp.append(dp[-1] + 1)
                sum += dp[-1]
            else:
                dp.append(0)
        return sum


# 3数学
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) <= 2:
            return 0
        left = 0
        sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i - 1] != A[i - 1] - A[i - 2]:
                a = (i - left - 2) * (i - left - 1) // 2 if i - left > 2 else 0
                left = i - 1
            elif i == len(A) - 1:
                a = (i - left - 1) * (i - left) // 2
            else:
                a = 0
            sum += a
        return sum


Solution().numberOfArithmeticSlices([1, 2, 4, 5])
