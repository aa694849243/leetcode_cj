'''
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
示例 2:

输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# caojie-98%
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        ans = [0] * (rows * cols)
        lenth = rows * cols
        j = 0
        l = 0
        k = 0
        i = 0
        while i < lenth:
            if rows == 1:
                while i < lenth:
                    ans[i] = matrix[l][j]
                    i += 1
                    j += 1
                break
            elif cols == 1:
                while i < lenth:
                    ans[i] = matrix[l][j]
                    l += 1
                    i += 1
                break
            if k < cols - 1:
                ans[i] = matrix[j][k + l]
                k += 1
            elif cols - 1 <= k < rows + cols - 2:
                ans[i] = matrix[k - (cols - 1) + j][cols - 1 + l]
                k += 1
            elif rows + cols - 2 <= k < 2 * cols + rows - 3:
                ans[i] = matrix[rows - 1 + j][cols - (k - rows - cols + 2) - 1 + l]
                k += 1
            elif 2 * cols + rows - 3 <= k < 2 * cols + 2 * rows - 4:
                ans[i] = matrix[rows - 1 - (k - (2 * cols + rows - 3)) + j][l]
                k += 1
            else:
                l += 1
                j += 1
                k = 0
                i -= 1
                rows -= 2
                cols -= 2
            i += 1

        return ans


# 官方更简洁的解法
# https://leetcode-cn.com/problems/spiral-matrix/solution/luo-xuan-ju-zhen-by-leetcode-solution/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        visited = [[False] * columns for _ in range(rows)]
        total = rows * columns
        order = [0] * total

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        row, column = 0, 0
        directionIndex = 0
        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + directions[directionIndex][0], column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex + 1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order

#
# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / spiral - matrix / solution / luo - xuan - ju - zhen - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
