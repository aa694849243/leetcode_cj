# -*- coding: utf-8 -*-
# 5754. 长度为三且各字符不同的子字符串
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s) - 2):
            if len(set(s[i:i + 3])) == 3:
                ans += 1
        return ans


Solution().countGoodSubstrings("aababcabc")
# 5755. 数组中最大数对和的最小值
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = 0
        while l < r:
            ans = max(nums[l] + nums[r], ans)
            l += 1
            r -= 1
        return ans


# 5757. 矩阵中最大的三个菱形和
class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        R = len(grid)
        C = len(grid[0])
        limit = (min(R, C) + 1) // 2
        res = set()

        def cal(centeri, centerj, b):
            flag = 0
            inc = 1
            ans = 0
            for j in range(centerj - b + 1, centerj + b):
                if flag == 0:
                    ans += grid[centeri][j]
                    flag += inc
                else:
                    ans += grid[centeri + flag][j] + grid[centeri - flag][j]
                    if flag == b - 1:
                        inc *= -1
                    flag += inc
            return ans

        for b in range(1, limit + 1):
            for r in range(b - 1, R - b + 1):
                for c in range(b - 1, C - b + 1):
                    peri = cal(r, c, b)
                    res.add(peri)
        return sorted(list(res), reverse=True)[:3]


# 5756. 两个数组最小的异或值之和
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        maxn = 1 << n
        b = [float('inf')] * maxn
        b[0] = 0
        for i in range(n):
            c = i + 1  # a数组前导1的数量
            for j in range(1, maxn):
                if bin(j).count('1') == c:
                    for k in range(n):
                        if (1 << k) & j:
                            b[j] = min(b[j], b[j - (1 << k)] + (nums2[k] ^ nums1[i]))
        return b[-1]


Solution().minimumXORSum([1, 2], [2, 3])
