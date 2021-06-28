# -*- coding: utf-8 -*-


# 给你两个数 hour 和 minutes 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。
#
#
#
#  示例 1：
#
#
#
#  输入：hour = 12, minutes = 30
# 输出：165
#
#
#  示例 2：
#
#
#
#  输入：hour = 3, minutes = 30
# 输出；75
#
#
#  示例 3：
#
#
#
#  输入：hour = 3, minutes = 15
# 输出：7.5
#
#
#  示例 4：
#
#  输入：hour = 4, minutes = 50
# 输出：155
#
#
#  示例 5：
#
#  输入：hour = 12, minutes = 0
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= hour <= 12
#  0 <= minutes <= 59
#  与标准答案误差在 10^-5 以内的结果都被视为正确结果。
#
#  Related Topics 数学
#  👍 30 👎 0


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        a = 30 * minutes / 60
        h = hour * 30 + a if hour!=12 else a
        mih=minutes*6
        ans=abs(h-mih)

        return min(ans, 360 - ans)


Solution().angleClock(3, 15)
