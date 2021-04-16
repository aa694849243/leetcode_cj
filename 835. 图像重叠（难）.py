# 给出两个图像 A 和 B ，A 和 B 为大小相同的二维正方形矩阵。（并且为二进制矩阵，只包含0和1）。
#
#  我们转换其中一个图像，向左，右，上，或下滑动任何数量的单位，并把它放在另一个图像的上面。之后，该转换的重叠是指两个图像都具有 1 的位置的数目。
#
#  （请注意，转换不包括向任何方向旋转。）
#
#  最大可能的重叠是什么？
#
#  示例 1:
#
#  输入：A = [[1,1,0],
#           [0,1,0],
#           [0,1,0]]
#      B = [[0,0,0],
#           [0,1,1],
#           [0,0,1]]
# 输出：3
# 解释: 将 A 向右移动一个单位，然后向下移动一个单位。
#
#  注意:
#
#
#  1 <= A.length = A[0].length = B.length = B[0].length <= 30
#  0 <= A[i][j], B[i][j] <= 1
#
#  Related Topics 数组
#  👍 62 👎 0

# 虚数应用
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A = [complex(i, j) for i in range(len(img1)) for j in range(len(img1[0])) if img1[i][j]]
        B = [complex(i, j) for i in range(len(img2)) for j in range(len(img2[0])) if img2[i][j]]
        B2 = set(B)
        seen = set()
        ans = 0
        for i in range(len(A)):
            for j in range(len(B)):
                d = B[j] - A[i]
                if d not in seen:
                    seen.add(d)
                    ans = max(ans, sum(a + d in B2 for a in A))
        return ans


# 2反向思考
import collections


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        count = collections.Counter()
        for i in range(len(img1)):
            for j in range(len(img1[0])):
                for k in range(len(img2)):
                    for l in range(len(img2[0])):
                        if img1[i][j] == 1 and img2[k][l] == 1:
                            count[k - i, l - j] += 1
        return max(count.values()) if count else 0
