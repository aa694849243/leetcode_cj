# 给定一个二进制矩阵 A，我们想先水平翻转图像，然后反转图像并返回结果。
#
#  水平翻转图片就是将图片的每一行都进行翻转，即逆序。例如，水平翻转 [1, 1, 0] 的结果是 [0, 1, 1]。
#
#  反转图片的意思是图片中的 0 全部被 1 替换， 1 全部被 0 替换。例如，反转 [0, 1, 1] 的结果是 [1, 0, 0]。
#
#
#
#  示例 1：
#
#
# 输入：[[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]
#
#
#  示例 2：
#
#
# 输入：[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# 输出：[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# 解释：首先翻转每一行: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]；
#      然后反转图片: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
#
#
#
#
#  提示：
#
#
#  1 <= A.length = A[0].length <= 20
#  0 <= A[i][j] <= 1
#
#  Related Topics 数组
#  👍 251 👎 0

from typing import List


# 1遍历两遍
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        image = [x[::-1] for x in image]
        image = [[val ^ 1 for val in row] for row in image]
        return image


# 2遍历1遍
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image[0])
        for row in image:
            l, r = 0, n - 1
            while l < r:
                if row[l] == row[r]:
                    row[l] ^= 1
                    row[r] ^= 1
                l += 1
                r -= 1
            if l == r:
                row[r] ^= 1
        return image


Solution().flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]])
