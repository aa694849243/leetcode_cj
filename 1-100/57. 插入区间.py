'''
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

#caojie_贪心算法_83%_
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        res = []
        left = newInterval[0]
        right = newInterval[1]  # 做左右指针
        for i in range(len(intervals)):
            if intervals[i][1] < left:  # 区间右边小于左指针，直接添加到结果里
                res.append(intervals[i])
            else:  # 找到区间插入位置，更新左指针后弹出循环，继续从i开始比对
                left = min(intervals[i][0], left)
                break
        for j in range(i, len(intervals)):
            if intervals[j][0] <= right:  # 更新右指针
                right = max(right, intervals[j][1])
            else:
                res.append([left, right])
                res.extend(intervals[j:])
                return res
        res.append([left, right])
        return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]
Solution().insert(intervals, newInterval)
