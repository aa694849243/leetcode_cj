# -*- coding: utf-8 -*-
import bisect
import collections
from typing import List


# 给你一个数组 events，其中 events[i] = [startDayi, endDayi] ，表示会议 i 开始于 startDayi ，结束于 e
# ndDayi 。
#
#  你可以在满足 startDayi <= d <= endDayi 中的任意一天 d 参加会议 i 。注意，一天只能参加一个会议。
#
#  请你返回你可以参加的 最大 会议数目。
#
#
#
#  示例 1：
#
#
#
#  输入：events = [[1,2],[2,3],[3,4]]
# 输出：3
# 解释：你可以参加所有的三个会议。
# 安排会议的一种方案如上图。
# 第 1 天参加第一个会议。
# 第 2 天参加第二个会议。
# 第 3 天参加第三个会议。
#
#
#  示例 2：
#
#  输入：events= [[1,2],[2,3],[3,4],[1,2]]
# 输出：4
#
#
#  示例 3：
#
#  输入：events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# 输出：4
#
#
#  示例 4：
#
#  输入：events = [[1,100000]]
# 输出：1
#
#
#  示例 5：
#
#  输入：events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
# 输出：7
#
#
#
#
#  提示：
#
#
#  1 <= events.length <= 10^5
#  events[i].length == 2
#  1 <= events[i][0] <= events[i][1] <= 10^5
#
#  Related Topics 贪心 数组 堆（优先队列）
#  👍 150 👎 0

#贪心+逆向思维
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[1]) #根据结束日期排序
        first_day=min(x[0] for x in events)
        second_day=max(x[1] for x in events)
        arr=list(range(first_day,second_day+1)) #最早到最晚做成一个列表，每一天参加一个事件
        ans=0
        for s,e in events: #events根据endday排序，我们先找结束早的，找离它开始时间最近的一天
            index=bisect.bisect_left(arr,s)
            if index==len(arr) or e<arr[index]: #如果列表里所有时间都小于开始时间或者找到的事件时间大于结束时间，则放弃这个会议
                continue
            del arr[index]
            ans+=1
        return ans



Solution().maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]])
