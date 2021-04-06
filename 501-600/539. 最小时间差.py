'''给定一个 24 小时制（小时:分钟 "HH:MM"）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

 

示例 1：

输入：timePoints = ["23:59","00:00"]
输出：1
示例 2：

输入：timePoints = ["00:00","23:59","00:00"]
输出：0
 

提示：

2 <= timePoints <= 2 * 104
timePoints[i] 格式为 "HH:MM"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-time-difference
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        li = []
        for time in timePoints:
            t = time.split(':')
            li.append(int(t[0]) * 60 + int(t[1]))
        li.sort()
        ans = float('inf')
        for i in range(1, len(li)):
            ans = min(li[i] - li[i - 1], ans)
        ans=min(1440+li[0]-li[-1],ans)
        return ans
