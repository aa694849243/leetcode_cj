# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，其中散布着 N 个推销点，编号 0 到 N-1，不存在三点共线的情况。每两点之间有一条直
# 线相连。游戏没有规定起点和终点，但限定了每次转角的方向。首先，小王需要先选择两个点分别作为起点和终点，然后从起点开始访问剩余 N-2 个点恰好一次并回到终点。访
# 问的顺序需要满足一串给定的长度为 N-2 由 L 和 R 组成的字符串 direction，表示从起点出发之后在每个顶点上转角的方向。根据这个提示，小王希望你能
# 够帮她找到一个可行的遍历顺序，输出顺序下标（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。
#
#
#
#  （上图：A->B->C 右转； 下图：D->E->F 左转）
#
#  示例 1：
#
#
#  输入：points = [[1,1],[1,4],[3,2],[2,1]], direction = "LL"
#
#  输入：[0,2,1,3]
#
#  解释：[0,2,1,3] 是符合"LL"的方案之一。在 [0,2,1,3] 方案中，0->2->1 是左转方向， 2->1->3 也是左转方向
#
#
#  示例 2：
#
#
#  输入：points = [[1,3],[2,4],[3,3],[2,1]], direction = "LR"
#
#  输入：[0,3,1,2]
#
#  解释：[0,3,1,2] 是符合"LR"的方案之一。在 [0,3,1,2] 方案中，0->3->1 是左转方向， 3->1->2 是右转方向
#
#
#  限制：
#
#
#  3 <= points.length <= 1000 且 points[i].length == 2
#  1 <= points[i][0],points[i][1] <= 10000
#  direction.length == points.length - 2
#  direction 只包含 "L","R"
#
#  Related Topics 贪心 几何 数组 数学
#  👍 10 👎 0

class Solution:
    def visitOrder(self, points: List[List[int]], direction: str) -> List[int]:
