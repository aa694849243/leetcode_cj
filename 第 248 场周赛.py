# -*- coding: utf-8 -*-
import collections
import heapq
from typing import List


# 5800. 基于排列构建数组
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            ans.append(nums[nums[i]])
        return ans


import fractions


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        ans = 0
        li = []
        time = 0
        for i in range(len(dist)):
            heapq.heappush(li, fractions.Fraction(dist[i], speed[i]))
        while li:
            limit = heapq.heappop(li)
            if limit <= time:
                break
            ans += 1
            time += 1
        return ans


# 5802. 统计好数字的数目
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10 ** 9 + 7
        odd = n // 2
        even = (n - 1) // 2 + 1
        return (pow(4, odd, mod)) * (pow(5, even, mod)) % mod


# 5803. 最长公共子路径
class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        base, mod = 113, 10 ** 9 + 57

        def cal(leng):
            m = collections.defaultdict(int)
            mult = pow(base, leng - 1, mod)
            for path in paths:
                hash = 0
                for i in range(leng):
                    hash = (hash * base + path[i]) % mod
                visted = {hash}
                m[hash] += 1
                if m[hash]==len(paths):
                    return True
                for i in range(leng, len(path)):
                    hash = ((hash - path[i - leng] * mult) * base + path[i]) % mod
                    if hash not in visted:
                        visted.add(hash)
                        m[hash] += 1
                    if m[hash] == len(paths):
                        return True
            return False
        l,r=0,len(min(paths,key=lambda x:len(x)))+1
        while l<r:
            mid=(l+r)//2
            if not cal(mid):
                r=mid
            else:
                l=mid+1
        return l-1
Solution().longestCommonSubpath(5, [[1,2,3,4],[4,1,2,3],[4]])
1000
[[457,179,464,533,503,51,313,804,494,122,608,85,654,393,727,86,448,380,848,227,318,731,692,828,829,929,28,812,440,186,638,889,185,241,998,750,219,649,137,454,673,575,653,66,141,722,342,598,31,92,621,928,390,585,3,792,946,826,983,617,873,980,565,47,610,180,230,144,698,462,13,242,453,374,73,930,373,9,237,633,364,127,650,687,459,538,918,312,485,903,159,908,212,60,174,404,949,978,407,644,113,748,950,136,524,774,477,586,123,433,258,33,845,429,899,753,434,383,274,840,267,532,834,696,958,830,370,21,87,712,301,239,2,813,463,114,859,339,819,514,537,924,628,735,672,766,319,251,547,306,745,282,778,743,566,357,218,199,780,755,17,942,960,648,795,426,917,726,993,82,376,742,233,439,68,221,932,238,191,194,758,571,701,540,981,65,381,486,839,662,497,768,962,172,594,200,849,344,952,142,799,26,95,916,367,202,682],[82,993]]