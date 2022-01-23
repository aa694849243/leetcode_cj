#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


# 在一个二维平面空间中，给你 n 个点的坐标。问，是否能找出一条平行于 y 轴的直线，让这些点关于这条直线成镜像排布？
#
#  注意：题目数据中可能有重复的点。
#
#
#
#  示例 1：
#
#
# 输入：points = [[1,1],[-1,1]]
# 输出：true
# 解释：可以找出 x = 0 这条线。
#
#
#  示例 2：
#
#
# 输入：points = [[1,1],[-1,-1]]
# 输出：false
# 解释：无法找出这样一条线。
#
#
#
#  提示：
#
#
#  n == points.length
#  1 <= n <= 10^4
#  -10^8 <= points[i][j] <= 10^8
#
#
#
#
#  进阶：你能找到比 O(n2) 更优的解法吗?
#  Related Topics 数组 哈希表 数学
#  👍 27 👎 0


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if len(points) == 1:
            return True
        points = set(map(tuple, points))
        points = sorted(points)
        if len(points) % 2:
            mid = len(points) // 2
            x = points[mid][0]
            points = points[:mid + 1] + sorted(points[mid + 1:], key=lambda x: (x[0], -x[1]))
            l, r = mid - 1, mid + 1
            while l >= 0 and r < len(points):
                if points[l][0] == x and points[r][0] == x:
                    l -= 1
                    r += 1
                    continue
                if x - points[l][0] != points[r][0] - x or points[l][1] != points[r][1]:
                    return False
                l -= 1
                r += 1
            return True
        else:
            mid = len(points) // 2
            l, r = mid - 1, mid
            x = (points[l][0] + points[r][0]) / 2
            points = points[:mid] + sorted(points[mid:], key=lambda x: (x[0], -x[1]))
            while l >= 0 and r < len(points):
                if points[l][0] == x and points[r][0] == x:
                    l -= 1
                    r += 1
                    continue
                if x - points[l][0] != points[r][0] - x or points[l][1] != points[r][1]:
                    return False
                l -= 1
                r += 1
            return True


Solution().isReflected([[0, 0], [0, -1]])
