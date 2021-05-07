# 5730. 将所有数字用字符替换
class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = ''
        for i, ch in enumerate(s):
            if ch.isdigit():
                ans += chr(ord(s[i - 1]) + int(ch))
            else:
                ans += ch
        return ans

    # 5731.  # 座位预约管理系统


class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt


import collections

import heapq


class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.li = list(range(1, n + 1))
        heapq.heapify(self.li)

    def reserve(self) -> int:
        return heapq.heappop(self.li)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.li, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
# 5732. 减小和重新排列数组后的最大元素
from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                continue
            else:
                arr[i] = arr[i - 1] + 1
        return arr[-1]


# 5733. 最近的房间
import bisect
import collections


class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:
        rooms.sort(key=lambda x: (x[1], x[0]), reverse=True)
        queries = [[id, size, i] for i, (id, size) in enumerate(queries)]
        queries.sort(key=lambda x: (x[1], x[0]), reverse=True)
        m = collections.deque(rooms)

        arr = []
        ans = [0] * len(queries)
        for id, size, i in queries:
            while m and m[0][1] >= size:
                bisect.insort_left(arr, m.popleft())
            if not arr:
                ans[i] = -1
                continue
            l = bisect.bisect_left(arr, [id, size])
            if l == 0:
                ans[i] = arr[0][0]
            elif l == len(arr):
                ans[i] = arr[-1][0]
            else:
                a = arr[l - 1][0]
                b = arr[l][0]
                if abs(a - id) <= abs(b - id):
                    ans[i] = a
                else:
                    ans[i] = b
        return ans


Solution().closestRoom([[2, 2], [1, 2], [3, 2]], [[3, 1], [3, 3], [5, 2]])
