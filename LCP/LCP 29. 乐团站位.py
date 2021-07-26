# -*- coding: utf-8 -*-
# 某乐团的演出场地可视作 `num * num` 的二维矩阵 `grid`（左上角坐标为 `[0,0]`)，每个位置站有一位成员。乐团共有 `9` 种乐器，乐
# 器编号为 `1~9`，每位成员持有 `1` 个乐器。
#
# 为保证声乐混合效果，成员站位规则为：自 `grid` 左上角开始顺时针螺旋形向内循环以 `1，2，...，9` 循环重复排列。例如当 num = `5` 时
# ，站位如图所示
#
# ![image.png](https://pic.leetcode-cn.com/1616125411-WOblWH-image.png)
#
#
# 请返回位于场地坐标 [`Xpos`,`Ypos`] 的成员所持乐器编号。
#
# **示例 1：**
# >输入：`num = 3, Xpos = 0, Ypos = 2`
# >
# >输出：`3`
# >
# >解释：
# ![image.png](https://pic.leetcode-cn.com/1616125437-WUOwsu-image.png)
#
#
# **示例 2：**
# >输入：`num = 4, Xpos = 1, Ypos = 2`
# >
# >输出：`5`
# >
# >解释：
# ![image.png](https://pic.leetcode-cn.com/1616125453-IIDpxg-image.png)
#
#
# **提示：**
# - `1 <= num <= 10^9`
# - `0 <= Xpos, Ypos < num` Related Topics 数学
#  👍 37 👎 0


class Solution:
    def orchestraLayout(self, num: int, xPos: int, yPos: int) -> int:
        layer = min(xPos, yPos, num - 1 - xPos, num - 1 - yPos)
        x_min = min(layer, num - 1 - layer)
        x_max = max(layer, num - 1 - layer)
        y_min = min(layer, num - 1 - layer)
        y_max = max(layer, num - 1 - layer)
        cnt = 0
        cnt += 2 * layer * num
        cnt += (num - (y_max - y_min + 1)) * (x_max - x_min + 1)
        if xPos == x_min:
            cnt += (yPos - y_min + 1)
        elif xPos == x_max:
            cnt += (y_max - y_min + x_max - x_min) + (y_max - y_min + 1) - (yPos - y_min)
        elif yPos == y_min:
            cnt += 2 * (y_max - y_min) + (x_max - x_min) + (x_max - x_min + 1) - (xPos - x_min)
        else:
            cnt += y_max - y_min + xPos - x_min + 1
        cnt %= 9
        return cnt if cnt!=0 else 9


Solution().orchestraLayout(7, 3, 4)
