# -*- coding: utf-8 -*-
# datetime： 2023-02-01 0:12
# ide： PyCharm
# 复杂模拟
import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# https://leetcode.cn/problems/time-to-cross-a-bridge/solution/by-endlesscheng-nzqo/
class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        time.sort(key=lambda x: x[0] + x[2])  # i越大效率越低
        # workL,workR, 大顶堆，[time,i] [完成搬运/放置的时间，工人编号]
        # waitL,waitR, 大顶堆，[i,time] [工人编号，完成搬运/放置的时间]
        workL, workR, waitL, waitR = [], [], [[-i, 0] for i in range(k)], []
        heapq.heapify(waitL)
        cur = 0
        while n:
            while workL and workL[0][0] <= cur:  # 完成左侧放置后可以进入等待队列的工人
                p = heapq.heappop(workL)
                heapq.heappush(waitL, [p[1], p[0]])
            while workR and workR[0][0] <= cur:  # 完成右侧搬运后可以进入等待队列的工人
                p = heapq.heappop(workR)
                heapq.heappush(waitR, [p[1], p[0]])
            # 每轮最多过一次桥，限制因素是右侧箱子数量
            if waitR:  # 右侧有等待的工人
                p = heapq.heappop(waitR)
                cur += time[-p[0]][2]  # 加过桥时间
                heapq.heappush(workL, [cur + time[-p[0]][3], p[0]])  # 加放置时间
            elif waitL:
                p = heapq.heappop(waitL)
                cur += time[-p[0]][0]  # 加过桥时间
                heapq.heappush(workR, [cur + time[-p[0]][1], p[0]])  # 加搬运时间
                n -= 1  # 搬运一个箱子
            else:
                a = workL[0][0] if workL else float('inf')
                b = workR[0][0] if workR else float('inf')
                cur = min(a, b)  # 左右都没有等待的工人，取最小完成工作时间
        while workR:
            p = heapq.heappop(workR)
            cur = max(cur, p[0]) + time[-p[1]][2]  # 最后的限制因素为过桥时间
        return cur


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findCrossingTime(
        1,
        3,
        [[1, 1, 2, 1], [1, 1, 3, 1], [1, 1, 4, 1]]
    )
)
