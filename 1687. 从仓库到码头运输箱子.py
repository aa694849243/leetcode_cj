import collections, heapq, itertools
from typing import List
# https://leetcode.cn/problems/delivering-boxes-from-storage-to-ports/solution/cong-cang-ku-dao-ma-tou-yun-shu-xiang-zi-dqnq/
#单调队列+dp
class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        n = len(boxes)
        prefix_diff = [0] * (n + 1)
        prefix_w = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_w[i] = prefix_w[i - 1] + boxes[i - 1][1]
            prefix_diff[i] = prefix_diff[i - 1] + (boxes[i - 1][0] != boxes[i - 2][0] if i > 1 else 0)
        dq = deque([0])
        f = [0] * (n + 1)
        g = [0] * (n + 1)
        for i in range(1, n + 1):
            while dq and (i - dq[0] > maxBoxes or prefix_w[i] - prefix_w[dq[0]] > maxWeight):
                dq.popleft()
            f[i] = g[dq[0]] + prefix_diff[i] + 2
            g[i] = f[i] - prefix_diff[i + 1] if i < n else float('inf')
            while dq and g[i] <= g[dq[-1]]:
                dq.pop()
            dq.append(i)
        return f[n]

