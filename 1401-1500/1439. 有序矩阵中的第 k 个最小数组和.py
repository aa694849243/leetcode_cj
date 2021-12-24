# -*- coding: utf-8 -*-
import heapq
from typing import List


# 给你一个 m * n 的矩阵 mat，以及一个整数 k ，矩阵中的每一行都以非递减的顺序排列。
#
#  你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 最小 数组和。
#
#
#
#  示例 1：
#
#  输入：mat = [[1,3,11],[2,4,6]], k = 5
# 输出：7
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。
#
#  示例 2：
#
#  输入：mat = [[1,3,11],[2,4,6]], k = 9
# 输出：17
#
#
#  示例 3：
#
#  输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
# 输出：9
# 解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
# [1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。
#
#
#  示例 4：
#
#  输入：mat = [[1,1,10],[2,2,9]], k = 7
# 输出：12
#
#
#
#
#  提示：
#
#
#  m == mat.length
#  n == mat.length[i]
#  1 <= m, n <= 40
#  1 <= k <= min(200, n ^ m)
#  1 <= mat[i][j] <= 5000
#  mat[i] 是一个非递减数组
#
#  Related Topics 数组 二分查找 矩阵 堆（优先队列）
#  👍 65 👎 0

# https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/solution/bao-li-jie-fa-zui-xiao-dui-by-coldme-2/
# 1 堆
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        R, C = len(mat), len(mat[0])
        a = sum(mat[i][0] for i in range(R))
        if C == 1:
            return a
        pq = [(a, [0] * R)]
        visted = {tuple([0] * R)}
        for _ in range(k - 1):
            num, status = heapq.heappop(pq)
            for r, c in enumerate(status):
                n_status = status.copy()
                if c < C - 1:
                    n_val = num - mat[r][c] + mat[r][c + 1]
                    n_status[r] = c + 1
                    if tuple(n_status) not in visted:
                        heapq.heappush(pq, (n_val, n_status))
                        visted.add(tuple(n_status))
        return pq[0][0]


# 2模拟

class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        R, C = len(mat), len(mat[0])
        prev = sorted(mat[0][:])[:k]
        for r in range(1, R):
            cur = []
            for num1 in prev:
                for num2 in mat[r]:
                    cur.append(num1 + num2)
            cur.sort()
            prev = cur[:k]
        return prev[-1]


# 3 二分
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        R, C = len(mat), len(mat[0])
        l, r = sum(mat[i][0] for i in range(R)), sum(mat[i][-1] for i in range(R)) + 1
        init=l
        def count(index, s, mid):
            if index == R:
                return 1
            cnt = 0
            for c in range(C):
                if s + mat[index][c] - mat[index][0] <= mid: #这里是直接计算的count,小于等于目标值的都可以计算一个count，这里的目标值最高为r-1,取到最高值一定要进入二分的else中
                    cnt += count(index + 1, s + mat[index][c] - mat[index][0], mid)
                    if cnt >= k:
                        break
                else:
                    break
            return cnt

        while l < r:
            mid = (l + r) // 2
            if count(0, init, mid) < k:
                l = mid + 1
            else:
                r = mid
        return l


Solution().kthSmallest([[1, 3, 11], [2, 4, 6]], 9)
