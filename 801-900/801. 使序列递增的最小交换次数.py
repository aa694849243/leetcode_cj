'''我们有两个长度相等且不为空的整型数组 A 和 B 。

我们可以交换 A[i] 和 B[i] 的元素。注意这两个元素在各自的序列中应该处于相同的位置。

在交换过一些元素之后，数组 A 和 B 都应该是严格递增的（数组严格递增的条件仅为A[0] < A[1] < A[2] < ... < A[A.length - 1]）。

给定数组 A 和 B ，请返回使得两个数组均保持严格递增状态的最小交换次数。假设给定的输入总是有效的。

示例:
输入: A = [1,3,5,4], B = [1,2,3,7]
输出: 1
解释:
交换 A[3] 和 B[3] 后，两个数组如下:
A = [1, 3, 5, 7] ， B = [1, 2, 3, 4]
两个数组均为严格递增的。
注意:

A, B 两个数组的长度总是相等的，且长度的范围为 [1, 1000]。
A[i], B[i] 均为 [0, 2000]区间内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-swaps-to-make-sequences-increasing
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1二元动态规划 2元动态规划
class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        if not A or len(A) == 1:
            return 0

        n1, s1 = 0, 1  # n1代表A[i]不变的最小交换次数，s1代表A[i]改变的最小交换次数
        for i in range(1, len(A)):
            n2 = s2 = float('inf')
            if A[i - 1] < A[i] and B[i - 1] < B[i]:  # 在不确定A[i-1]和B[i-1]是否能交换的情况下
                n2 = min(n1, n2)  # A[i-1]不动，A[i]也不动
                s2 = min(s1 + 1, s2)  # A[i]动了，A[i-1]必须动，因为不确定A[i-1]和B[i-1]的关系，所以这个条件下要么交换两个要么都不交换
            if A[i - 1] < B[i] and B[i - 1] < A[i]:  # 明确A[i-1]和B[i-1]可以交换
                n2 = min(n2, s1)
                s2 = min(s2, n1 + 1)
            n1, s1 = n2, s2
        return min(n1, s1)
