# 给你一个 m x n 的矩阵 matrix 和一个整数 k ，找出并返回矩阵内部矩形区域的不超过 k 的最大数值和。
#
#  题目数据保证总会存在一个数值和不超过 k 的矩形区域。
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,0,1],[0,-2,3]], k = 2
# 输出：2
# 解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
#
#
#  示例 2：
#
#
# 输入：matrix = [[2,2,-1]], k = 3
# 输出：3
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 100
#  -100 <= matrix[i][j] <= 100
#  -10⁵ <= k <= 10⁵
#
#
#
#
#  进阶：如果行数远大于列数，该如何设计解决方案？
#
#  Related Topics 数组 二分查找 矩阵 有序集合 前缀和
#  👍 448 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
import bisect


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        R, C = len(matrix), len(matrix[0])
        res = -100000
        for left in range(C):  # 枚举左边界
            s = [0] * R
            for c in range(left, C):
                for r in range(R):
                    s[r] += matrix[r][c]
                cur = 0
                tmp_lst = [0]
                for r in range(R):
                    cur += s[r]
                    idx = bisect.bisect_left(tmp_lst, cur - k)
                    if idx < len(tmp_lst):
                        res = max(res, cur - tmp_lst[idx])
                    bisect.insort(tmp_lst, cur)
        return res


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().maxSumSubmatrix(
        [[2, 2, -1]], 2
    )
)
