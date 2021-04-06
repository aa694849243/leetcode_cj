'''
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        res = [[0] * n for _ in range(n)]
        visited = [[False] * n for _ in range(n)]
        col, row, t = 0, 0, n * n
        d_indext = 0
        for i in range(t):
            res[row][col] = i+1
            visited[row][col] = True
            next_row=row+direction[d_indext][0]
            next_col=col+direction[d_indext][1]
            if not (0 <= next_col < n and 0 <= next_row < n and not visited[next_row][next_col]):
                d_indext = (d_indext + 1) % 4
            next_col_d = direction[d_indext][1]
            next_row_d = direction[d_indext][0]
            row += next_row_d
            col += next_col_d
        return res
Solution().generateMatrix(3)