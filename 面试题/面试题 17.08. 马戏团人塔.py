#!/usr/bin/env python
# -*- coding: utf-8 -*-
import bisect
from typing import List


# 有个马戏团正在设计叠罗汉的表演节目，一个人要站在另一人的肩膀上。出于实际和美观的考虑，在上面的人要比下面的人矮一点且轻一点。已知马戏团每个人的身高和体重，请
# 编写代码计算叠罗汉最多能叠几个人。
#
#  示例：
#
#
# 输入：height = [65,70,56,75,60,68] weight = [100,150,90,190,95,110]
# 输出：6
# 解释：从上往下数，叠罗汉最多能叠 6 层：(56,90), (60,95), (65,100), (68,110), (70,150), (75,190)
#
#
#  提示：
#
#
#  height.length == weight.length <= 10000
#
#  Related Topics 数组 二分查找 动态规划 排序
#  👍 72 👎 0

# LIS 最长上升子序列
class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        height, weight = zip(*sorted(zip(height, weight), key=lambda x: (x[0], -x[1])))
        dp = [0] * len(height)
        ans = 0
        for w in weight:
            i = bisect.bisect_left(dp, w, 0, ans)
            dp[i] = w
            if i == ans:
                ans += 1
        return ans
