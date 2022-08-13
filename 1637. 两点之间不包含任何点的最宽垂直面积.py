from typing import List


# @solution-sync:begin
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ma = 0
        points = sorted(points)
        for i in range(1,len(points)):
            ma = max(ma, points[i][0]-points[i-1][0])
        return  ma