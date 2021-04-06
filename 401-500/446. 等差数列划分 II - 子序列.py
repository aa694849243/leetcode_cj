'''如果一个数列至少有三个元素，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，以下数列为等差数列:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
以下数列不是等差数列。

1, 1, 2, 5, 7
 

数组 A 包含 N 个数，且索引从 0 开始。该数组子序列将划分为整数序列 (P0, P1, ..., Pk)，满足 0 ≤ P0 < P1 < ... < Pk < N。

 

如果序列 A[P0]，A[P1]，...，A[Pk-1]，A[Pk] 是等差的，那么数组 A 的子序列 (P0，P1，…，PK) 称为等差序列。值得注意的是，这意味着 k ≥ 2。

函数要返回数组 A 中所有等差子序列的个数。

输入包含 N 个整数。每个整数都在 -231 和 231-1 之间，另外 0 ≤ N ≤ 1000。保证输出小于 231-1。

 

示例：

输入：[2, 4, 6, 8, 10]

输出：7

解释：
所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/solution/dp-python-by-lu-gui-chen-2/
# https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence/solution/deng-chai-shu-lie-hua-fen-ii-zi-xu-lie-by-leetcode/
from typing import List
import collections


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        memo = [collections.defaultdict(int) for _ in A]
        res = 0
        for i in range(len(A)):
            for j in range(i):  # memo[i]表示以i结尾的等差序列，A[i]-A[j]表示两个数的差值，总结memo[i][A[i]-A[j]]=以i结尾差值为d的等差序列
                memo[i][A[i] - A[j]] += 1  # 塑造弱等差序列，即两个数必定有组成若等差序列
                if A[i] - A[j] in memo[j]:  # A[i]延伸了终点为j的等差序列，每延伸一个拓展总数为原数量+1，因为1234.。。x，与234.。。x数量是相等的，最后多了1个123.。。x+1
                    memo[i][A[i] - A[j]] += memo[j][A[i] - A[j]]
                    res += memo[j][A[i] - A[j]]
        return res
Solution().numberOfArithmeticSlices([1, 3, 5, 7, 9])