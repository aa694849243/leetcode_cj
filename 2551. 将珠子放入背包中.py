# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-02 22:27 
# ide： PyCharm
class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        lst1, lst2 = [], []
        for i in range(1, len(weights)):
            heapq.heappush(lst1, weights[i] + weights[i - 1])
            heapq.heappush(lst2, -weights[i] - weights[i - 1])
        n = len(weights)
        union_cnt = n - k
        total1 = total2 = sum(weights) * 2
        while union_cnt:
            total1 -= heapq.heappop(lst1)
            total2 += heapq.heappop(lst2)
            union_cnt -= 1
        return total1 - total2

# leetcode submit region end(Prohibit modification and deletion)

