# -*- coding: utf-8 -*-
import collections
from typing import List


# 力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令
# 有两种：
#
#
#  U: 向y轴正方向移动一格
#  R: 向x轴正方向移动一格。
#
#
#  不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。
#
#  给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。
#
#
#
#  示例 1：
#
#  输入：command = "URR", obstacles = [], x = 3, y = 2
# 输出：true
# 解释：U(0, 1) -> R(1, 1) -> R(2, 1) -> U(2, 2) -> R(3, 2)。
#
#  示例 2：
#
#  输入：command = "URR", obstacles = [[2, 2]], x = 3, y = 2
# 输出：false
# 解释：机器人在到达终点前会碰到(2, 2)的障碍物。
#
#  示例 3：
#
#  输入：command = "URR", obstacles = [[4, 2]], x = 3, y = 2
# 输出：true
# 解释：到达终点后，再碰到障碍物也不影响返回结果。
#
#
#
#  限制：
#
#
#  2 <= command的长度 <= 1000
#  command由U，R构成，且至少有一个U，至少有一个R
#  0 <= x <= 1e9, 0 <= y <= 1e9
#  0 <= obstacles的长度 <= 1000
#  obstacles[i]不为原点或者终点
#
#  Related Topics 数组 哈希表 模拟
#  👍 90 👎 0


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        u, r = collections.Counter(command)['U'], collections.Counter(command)['R']
        m = collections.defaultdict(set)
        X,Y=x,y
        m[0].add(0)
        x, y = 0, 0

        for ch in command:
            if ch == 'U':
                y += 1
            else:
                x += 1
            m[x].add(y)
        def cal(x,y):
            cnt=0
            while x>=0 and y>=0:
                x-=r
                y-=u
                cnt+=1
            return cnt-1
        cnt=cal(X,Y)
        if Y-u*cnt not in m[X-r*cnt]:
            return False
        for x,y in obstacles:
            if x>X or y>Y:
                continue
            cnt=cal(x,y)
            x-=r*cnt
            y-=u*cnt
            if y in m[x]:
                return False
        return True
Solution().robot("URR",[[4, 2]], 3, 2)