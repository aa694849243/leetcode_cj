'''给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:

可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]

输出: 1

解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]

输出: 2

解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]

输出: 0

解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/non-overlapping-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1从前往后动态规划 超时
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or not len(intervals[0]):
            return 0
        if len(intervals) == 1:
            return 0
        intervals = sorted(intervals)
        n = len(intervals)
        dp = [1]
        for i in range(1, n):
            m = 0
            for j in range(i):
                if intervals[i][0] >= intervals[j][1]:
                    m = max(dp[j] + 1, m)
            dp.append(m)
        return n - max(dp)


# 2从后往前动态规划 超时
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or not len(intervals[0]):
            return 0
        if len(intervals) == 1:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        dp = [1]
        n = len(intervals)
        for i in range(1, n):
            m = 1
            for j in range(i - 1, -1, -1):
                if intervals[i][0] >= intervals[j][1]:
                    m = dp[j] + 1
                    break
            dp.append(max(m, dp[i - 1]))
        return n - max(dp)


# 从前往后贪心
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or not len(intervals[0]):
            return 0
        if len(intervals) == 1:
            return 0
        intervals = sorted(intervals)
        n = len(intervals)
        ans = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] >= ans[-1][1]:
                ans.append(intervals[i])
            elif intervals[i][1] <= ans[-1][1]:
                ans.pop()
                ans.append(intervals[i])
            elif intervals[i][1] > ans[-1][1] and intervals[i][0] >= ans[-1][0]:
                continue
        return n - len(ans)


# 从前往后贪心
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals or not len(intervals[0]):
            return 0
        if len(intervals) == 1:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        n = len(intervals)
        ans = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] >= ans[-1][1]:
                ans.append(intervals[i])
            elif intervals[i][0] <= ans[-1][0]:
                continue
            elif intervals[i][1] > ans[-1][1] and intervals[i][0] >= ans[-1][0]:
                continue
        return n - len(ans)


Solution().eraseOverlapIntervals([[3, 37], [9, 19], [19, 37], [20, 86], [28, 40], [29, 97], [48, 89], [51, 155]])
