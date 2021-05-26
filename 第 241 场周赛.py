import collections, heapq, itertools
from typing import List


# 5759. 找出所有子集的异或总和再求和
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        self.m = set()

        def xorsum(li):
            a = 0
            for num in li:
                a ^= num
            return a

        def dfs(j):
            if j == 0:
                return [[], [nums[0]]]
            a = dfs(j - 1)
            b = [li + [nums[j]] for li in a]
            return a + b

        res = dfs(len(nums) - 1)
        for li in res:
            ans += xorsum(li)
        return ans


Solution().subsetXORSum([1, 3])


# 5760. 构成交替字符串需要的最小交换次数
class Solution:
    def minSwaps(self, s: str) -> int:
        odd = set()
        even = set()
        ans = float('inf')
        for i, ch in enumerate(s):
            if i % 2 and ch == '1':
                odd.add(i)
            elif i % 2 == 0 and ch == '0':
                even.add(i)
        if len(odd) == len(even):
            ans = min(ans, len(odd))
        odd, even = set(), set()
        for i, ch in enumerate(s):
            if i % 2 and ch == '0':
                odd.add(i)
            elif i % 2 == 0 and ch == '1':
                even.add(i)
        if len(odd) == len(even):
            ans = min(ans, len(odd))
        return ans if ans != float('inf') else -1


Solution().minSwaps("111000")


# 5761. 找出和为指定值的下标对
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.Count = collections.Counter(nums2)
        self.nums1, self.nums2 = nums1, nums2

    def add(self, index: int, val: int) -> None:
        self.Count[self.nums2[index]] -= 1
        self.Count[self.nums2[index] + val] += 1
        self.nums2[index]+=val

    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.nums1:
            target = tot - num
            cnt += self.Count[target]
        return cnt


# ["FindSumPairs","add","add","count","add","add","add","add","add","add","add","add","count","count"]
# [[[9,70,14,9,76],[26,26,58,23,74,68,68,78,58,26]],[6,10],[5,6],[32],[3,55],[9,32],[9,16],[1,48],[1,4],[0,52],[8,20],[9,4],[88],[154],[9,4501],[2,20],[2,4501],[8,4501],[5,4505],[4,4],[5,4241],[4,4501],[4,4241]]
obj = FindSumPairs([9, 70, 14, 9, 76], [26, 26, 58, 23, 74, 68, 68, 78, 58, 26])
obj.add(6, 10)
obj.add(5, 6)
obj.count(32)
obj.add(3, 55)
obj.add(9, 32)
obj.add(9, 16)
obj.add(1, 48)
obj.add(1, 4)
obj.add(0, 52)
obj.add(8, 20)
obj.count(88)
obj.count(154)
