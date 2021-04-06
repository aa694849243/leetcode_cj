'''给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

示例:

输入: matrix = [[1,0,1],[0,-2,3]], k = 2
输出: 2
解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
说明：

矩阵内的矩形区域面积必须大于 0。
如果行数远大于列数，你将如何解答呢？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not len(matrix):
            return 0
        if not len(matrix[0]):
            return -1000000000
        col, row = len(matrix[0]), len(matrix)
        res=float('-inf')
        for left in range(col):  # 先固定一列作为最左边
            s = [0] * row
            for i in range(left, col):  # 逐渐扩展列，每一列累加前一列值
                for j in range(row):  # s记录每列从上到下的累加值
                    s[j] += matrix[j][i]
                lst = [0]
                cur = 0  # cur为s序列的累加值，设s累加点为j
                # 题目求cur-s[x]<=k 此时x要小于j(因为至少为一个长度，如果题目可以设置无长度，则最后再与0比就行了)即 s[x]>=cur-k 即cur-k要在lst内部
                for i in range(row):
                    cur += s[i]
                    loc = bisect.bisect_left(lst, cur - k)
                    if loc < len(lst):
                        res = max(res, cur - lst[loc])
                    bisect.insort_left(lst,cur)
        return res
a=[[7,7,4,-6,-10],[-7,-3,-9,-1,-7],[9,6,-3,-7,7],[-4,1,4,-3,-8],[-7,-4,-4,6,-10],[1,3,-2,3,-10],[8,-2,1,1,-8]]
k=12
Solution().maxSumSubmatrix(a,k)