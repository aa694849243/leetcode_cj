# 5746. 到目标元素的最小距离
from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float('inf')
        for i, num in enumerate(nums):
            if num == target:
                if abs(i - start) < ans:
                    ans = abs(i - start)
        return ans

    # 5747.  # 将字符串拆分为递减的连续值


class Solution:
    def splitString(self, s: str) -> bool:
        if not s.lstrip('0'):
            return False
        s = s.lstrip('0')
        n = len(s)
        m = {}

        def dfs(i, j):
            if i == 0 and j == n:
                return False
            a = int(s[i:j])
            for k in range(j + 1, n + 1):
                if int(s[j:k]) == a - 1:
                    if k == n:
                        return True
                    else:
                        if dfs(j, k):
                            return True
            return False

        for i in range(1, n):
            if dfs(0, i):
                return True
        return False


# 5749. 邻位交换的最小次数
import math

import bisect
import collections

class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        li = list(num)

        def bisect(l, r, target):
            while l < r:
                mid = (l + r) // 2
                if li[mid] > target:
                    l = mid + 1
                else:
                    r = mid
            return l

        n = len(li)

        def nxtnum():
            for i in range(len(li) - 2, -1, -1):
                if li[i] < li[i + 1]:
                    flag = i
                    break
            a = bisect(flag + 1, n, li[flag]) - 1
            li[flag], li[a] = li[a], li[flag]
            li[flag + 1:] = sorted(li[flag + 1:])

        for _ in range(k):
            nxtnum()
        orgin = collections.deque(list(num))
        target = collections.deque(li)
        ans = 0
        while orgin and target:
            if orgin[0] == target[0]:
                orgin.popleft()
                target.popleft()
            else:
                a = target.popleft()
                b = orgin.index(a)
                ans+=b
                orgin.remove(a)
        return ans

Solution().getMinSwaps(num = "5489355142", k = 4)

import heapq
import collections


# 包含每个查询的最小区间
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(val, i) for i, val in enumerate(queries)]
        queries.sort()
        intervals.sort()
        ans = [-1] * len(queries)
        pq = []
        flag = 0
        for val, id in queries:
            for j in range(flag, len(intervals)):
                l, r = intervals[j]
                if l <= val:
                    heapq.heappush(pq, (r - l + 1, r))
                else:
                    flag = j
                    break
            while pq and pq[0][1] < val:
                heapq.heappop(pq)
            if pq:
                ans[id] = pq[0][0]
        return ans


Solution().minInterval(intervals=[[2, 3], [2, 5], [1, 8], [20, 25]], queries=[2, 19, 5, 22])
