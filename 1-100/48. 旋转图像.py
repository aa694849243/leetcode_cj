'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
示例 2:

给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 转置+逆序------------------------------------------
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()


# 四个矩形旋转法-----------------caojie_43%-------------------------
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        end = len(matrix)
        i = 0
        step = end - 1
        while i <= end // 2:
            # if step == 1:  # 测试发现step==1时，j会in[]，所以拿出来分情况讨论
            #     temp = matrix[i][i]
            #     matrix[i][i] = matrix[i + 1][i]
            #     matrix[i + 1][i] = matrix[i + 1][i + 1]
            #     matrix[i + 1][i + 1] = matrix[i][i + 1]
            #     matrix[i][i + 1] = temp
            #     break
            for j in range(0, step):
                temp = matrix[i][i + j]
                matrix[i][i + j] = matrix[i + step - j][i]
                matrix[i + step - j][i] = matrix[i + step][i + step - j]
                matrix[i + step][i + step - j] = matrix[i + j][i + step]
                matrix[i + j][i + step] = temp
            step -= 2
            i += 1


matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# matrix=[[1,2],[3,4]]
Solution().rotate(matrix)
