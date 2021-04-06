'''
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

 

示例：

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

返回 13。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# caojie 归并算法
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def merge(l1, l2):
            i, j = 0, 0
            x = []
            while i < len(l1) and j < len(l2):
                if l1[i] < l2[j]:
                    x.append(l1[i])
                    i += 1
                else:
                    x.append(l2[j])
                    j += 1
            while i < len(l1):
                x.append(l1[i])
                i += 1
            while j < len(l2):
                x.append(l2[j])
                j += 1
            return x

        def merge_pass(matrix):
            i = 0
            x = []
            while i + 1 < len(matrix):
                x.append(merge(matrix[i], matrix[i + 1]))
                i += 2
            if i < len(matrix):
                x.append(matrix[i])
            return x

        def merge_sort(matrix):
            while len(matrix) > 1:
                matrix = merge_pass(matrix)
            return matrix[0]

        l = merge_sort(matrix)
        return l[k - 1]


# 堆+归并排序
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / kth - smallest - element - in -a - sorted - matrix / solution / you - xu - ju - zhen - zhong - di - kxiao - de - yuan - su - by - leetco /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


# 二分法
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / kth - smallest - element - in -a - sorted - matrix / solution / you - xu - ju - zhen - zhong - di - kxiao - de - yuan - su - by - leetco /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
Solution().kthSmallest(matrix, k)
