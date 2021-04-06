'''给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

 

示例:

输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释:

 

说明:

给定矩阵中的元素总数不会超过 100000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diagonal-traverse
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1模拟
# https://leetcode-cn.com/problems/diagonal-traverse/solution/dui-jiao-xian-bian-li-by-leetcode/
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix[0]) == 0:
            return []
        i, j = 0, 0
        ans = []
        flag = 1
        while i < len(matrix) and j < len(matrix[0]):
            ans.append(matrix[i][j])
            if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
                break
            if flag == 1:
                if i - 1 >= 0 and j + 1 < len(matrix[0]):
                    i -= 1
                    j += 1
                elif i - 1 < 0 and j + 1 < len(matrix[0]):
                    j += 1
                    flag *= -1
                elif j + 1 >= len(matrix[0]) and i + 1 < len(matrix):
                    i += 1
                    flag *= -1
                else:
                    break
            elif flag == -1:
                if i + 1 < len(matrix) and j - 1 >= 0:
                    i += 1
                    j -= 1
                elif i + 1 >= len(matrix) and j + 1 < len(matrix[0]):
                    j += 1
                    flag *= -1
                elif j - 1 < 0 and i + 1 < len(matrix):
                    i += 1
                    flag *= -1
        return ans


# 2简化
# 偶数反向提取对角线，奇数正向提取对角线
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix[0]) == 0:
            return []
        n = 0
        res = []
        while n < len(matrix) + len(matrix[0]) - 1:
            tmp = []
            if n < len(matrix[0]):
                y_origin = 0
                x_origin = n
            else:
                y_origin = n - len(matrix[0]) + 1
                x_origin = len(matrix[0]) - 1
            while 0 <= x_origin < len(matrix[0]) and 0 <= y_origin < len(matrix):
                tmp.append(matrix[y_origin][x_origin])
                x_origin -= 1
                y_origin += 1
            if not n % 2:  # 偶数
                res.extend(tmp[::-1])
            else:  # 奇数
                res.extend(tmp[:])
            n += 1
        return res


Solution().findDiagonalOrder([[2, 3]])
