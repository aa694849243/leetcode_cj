# 有一个二维矩阵 A 其中每个元素的值为 0 或 1 。
#
#  移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 0 都更改为 1，将所有 1 都更改为 0。
#
#  在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。
#
#  返回尽可能高的分数。
#
#
#
#
#
#
#  示例：
#
#  输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# 输出：39
# 解释：
# 转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
#
#
#
#  提示：
#
#
#  1 <= A.length <= 20
#  1 <= A[0].length <= 20
#  A[i][j] 是 0 或 1
#
#  Related Topics 贪心算法
#  👍 194 👎 0

from typing import List
import copy
import collections


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        B = copy.deepcopy(A)
        cal_c = [0] * (len(A[0]))
        cal_c[0] = len(A)
        for i in range(len(A)):
            if A[i][0] == 1:
                change = 0
            else:
                A[i][0] = 1
                change = 1
            for j in range(1, len(A[0])):
                if change:
                    A[i][j] ^= 1
        flag = 0
        for c in zip(*A):
            if flag == 0:
                flag += 1
                continue
            cal_c[flag] = max(collections.Counter(c)[0], collections.Counter(c)[1])
            flag += 1
        ans = 0
        for i, num in enumerate(cal_c):
            ans += (1 << (len(cal_c) - i - 1)) * num
        return ans


Solution().matrixScore([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]])
