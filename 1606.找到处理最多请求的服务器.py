import heapq
from typing import List

from sortedcontainers import SortedList


# @solution-sync:begin
# 有序集合
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = []
        available = SortedList(range(k))
        requests = [0] * k
        for i, (start, dur) in enumerate(zip(arrival, load)):
            while busy:
                if busy[0][0] <= start:
                    _, id = heapq.heappop(busy)
                    available.add(id)
                else:
                    break
            if available:
                j = available.bisect_left(i % k)
                if j == len(available):
                    j = 0
                id = available[j]
                requests[id] += 1
                heapq.heappush(busy, (start + dur, id))
                available.remove(id)
        maxReq = max(requests)
        return [i for i, v in enumerate(requests) if v == maxReq]


# 双优先队列
# 负数求余 距离 环技巧
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy = []
        available = [*range(k)]
        requests = [0] * k
        for i, (start, dur) in enumerate(zip(arrival, load)):
            while busy:
                if busy[0][0] <= start:
                    _, id = heapq.heappop(busy)
                    new_id = i + (id - i) % k
                    heapq.heappush(available, new_id)
                else:
                    break
            if available:
                id = heapq.heappop(available) % k
                requests[id] += 1
                heapq.heappush(busy, (start + dur, id))
        req_max=max(requests)
        return [i for i,v in enumerate(requests) if v==req_max]


print(Solution().busiestServers(k=3, arrival=[1, 2, 3, 4, 5], load=[5, 2, 3, 3, 3]))
