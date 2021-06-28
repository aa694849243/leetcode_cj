# -*- coding: utf-8 -*-
from typing import List


# 给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。
#
#  只有当 c <= a 且 b <= d 时，我们才认为区间 [a,b) 被区间 [c,d) 覆盖。
#
#  在完成所有删除操作后，请你返回列表中剩余区间的数目。
#
#
#
#  示例：
#
#
# 输入：intervals = [[1,4],[3,6],[2,8]]
# 输出：2
# 解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。
#
#
#
#
#  提示：
#
#
#  1 <= intervals.length <= 1000
#  0 <= intervals[i][0] < intervals[i][1] <= 10^5
#  对于所有的 i != j：intervals[i] != intervals[j]
#
#  Related Topics 贪心算法 排序 Line Sweep
#  👍 46 👎 0


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        li=[intervals[0]]
        for l,r in intervals[1:]:
            while li and l<=li[-1][0]:
                li.pop()
            li.append([l,r])
        return len(li)