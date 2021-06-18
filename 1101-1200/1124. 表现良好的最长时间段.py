# -*- coding: utf-8 -*-
import itertools
from typing import List


# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
#
#  我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
#
#  所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
#
#  请你返回「表现良好时间段」的最大长度。
#
#
#
#  示例 1：
#
#  输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
#
#
#
#  提示：
#
#
#  1 <= hours.length <= 10000
#  0 <= hours[i] <= 16
#
#  Related Topics 栈
#  👍 136 👎 0

# 最长上坡类问题 类单调栈
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        li = [1 if x > 8 else -1 for x in hours]
        prefix = [0] + [*itertools.accumulate(li)]
        stack = [(prefix[0], 0)]
        for i, val in enumerate(prefix[1:], 1):
            if val < stack[-1][0]:
                stack.append((val, i))
        ans = 0
        for i in range(len(prefix) - 1, -1, -1):
            while stack and prefix[i] - stack[-1][0] > 0:
                ans = max(ans, i - stack[-1][1])
                stack.pop()
            if not stack:
                break
        return ans