import bisect
import math
from typing import List


# @solution-sync:begin
# 角度滑动窗口
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        if not points:
            return 0
        delta = angle / 180 * math.pi
        angles = []
        x0, y0 = location
        cnt = 0
        same_cnt = 0
        for x, y in points:
            dx, dy = x - x0, y - y0
            if dx == 0 and dy == 0:
                same_cnt += 1
            else:
                angle = math.atan2(dy, dx)
                angles.append(angle)

        angles.sort()
        angles += [angle + 2 * math.pi for angle in angles]
        tmp = []
        p = 0
        for i, angle in enumerate(angles):
            while p < len(angles) and angle - angles[p] > delta:
                p += 1
            cnt = max(cnt, i - p + 1)
        return cnt + same_cnt


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        delta = angle / 180 * math.pi
        angles = []
        x0, y0 = location
        cnt = 0
        same_cnt = 0
        for x, y in points:
            dx, dy = x - x0, y - y0
            if dx == 0 and dy == 0:
                same_cnt += 1
            else:
                angle = math.atan2(dy, dx)
                angles.append(angle)

        angles.sort()
        angles += [angle + 2 * math.pi for angle in angles]
        for i, angle in enumerate(angles):
            cnt = max(cnt, bisect.bisect_right(angles, angle + delta) - i)
        return cnt + same_cnt

    print(Solution().visiblePoints([[20, 64], [47, 77], [73, 40]], 42, [9, 61]))
