import collections
from typing import List


# @solution-sync:begin
class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ma = 0
        for i in range(1 << len(requests)):
            m = collections.defaultdict(int)
            for j in range(len(requests)):
                if i & (1 << j):
                    from_, to_ = requests[j]
                    m[from_] += 1
                    m[to_] -= 1
                    if m[from_] == 0:
                        m.pop(from_)
                    if m[to_] == 0:
                        m.pop(to_)
            if len(m) == 0:
                ma = max(ma, bin(i)[2:].count('1'))
        return ma
