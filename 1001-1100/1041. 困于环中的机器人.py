# -*- coding: utf-8 -*-
# 在无限的平面上，机器人最初位于 (0, 0) 处，面朝北方。机器人可以接受下列三条指令之一：
#
#
#  "G"：直走 1 个单位
#  "L"：左转 90 度
#  "R"：右转 90 度
#
#
#  机器人按顺序执行指令 instructions，并一直重复它们。
#
#  只有在平面中存在环使得机器人永远无法离开时，返回 true。否则，返回 false。
#
#
#
#  示例 1：
#
#  输入："GGLLGG"
# 输出：true
# 解释：
# 机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
# 重复这些指令，机器人将保持在以原点为中心，2 为半径的环中进行移动。
#
#
#  示例 2：
#
#  输入："GG"
# 输出：false
# 解释：
# 机器人无限向北移动。
#
#
#  示例 3：
#
#  输入："GL"
# 输出：true
# 解释：
# 机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动。
#
#
#
#  提示：
#
#
#  1 <= instructions.length <= 100
#  instructions[i] 在 {'G', 'L', 'R'} 中
#
#  Related Topics 数学
#  👍 74 👎 0

# 两种情况，回到原点会成环
# 方向与初始方向不同，会回到原点，因为最多经过四次偏转，会上下方向的距离抵消，左右方向的距离抵消
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        x, y = 0, 0
        for s in instructions:
            dx, dy = dirs[i]
            if s == 'G':
                x += dx
                y += dy
            elif s == 'L':
                i = (i - 1) % 4
            else:
                i = (i + 1) % 4
        if (x, y) == (0, 0) or i != 0:
            return True
        return False
