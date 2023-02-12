# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-07 23:49 
# ide： PyCharm
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for tp in timePoints:
            h, m = tp.split(":")
            times.append(int(h) * 60 + int(m))
        end = 24 * 60
        times.sort()
        mi = math.inf
        for i in range(1, len(times)):
            mi = min(mi, times[i] - times[i - 1])
        mi = min(mi, end - times[-1] + times[0])
        return mi
# leetcode submit region end(Prohibit modification and deletion)

