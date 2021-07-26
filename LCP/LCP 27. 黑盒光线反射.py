# -*- coding: utf-8 -*-

# https://leetcode-cn.com/problems/IQvJ9i/solution/yu-chu-li-chu-suo-you-de-zu-by-zerotrac2/


# 秋日市集上有个奇怪的黑盒，黑盒的主视图为 n\*m 的矩形。从黑盒的主视图来看，黑盒的上面和下面各均匀分布有 m 个小孔，黑盒的左面和右面各均匀分布有 n # 个小孔。黑盒左上角小孔序号为 0，按顺时针编号，总共有 2*(m+n) 个小孔。每个小孔均可以打开或者关闭，初始时，所有小孔均处于关闭状态。每个小孔上的盖子均为
# 镜面材质。例如一个 2\*3 的黑盒主视图与其小孔分布如图所示:
#
# ![image.png](https://pic.leetcode-cn.com/1598951281-ZCBrif-image.png){:height=
# "200px"}
#
# 店长告诉小扣，这里是「几何学的快问快答」，店长可能有两种操作：
#
# - `open(int index, int direction)` - 若小孔处于关闭状态，则打开小孔，照入光线；否则直接照入光线；
# - `close(int index)` - 关闭处于打开状态小孔，店长保证不会关闭已处于关闭状态的小孔；
#
# 其中：
# - `index`： 表示小孔序号
# - `direction`：`1` 表示光线沿 $y=x$ 方向，`-1` 表示光线沿 $y=-x$ 方向。
#
# ![image.png](https://pic.leetcode-cn.com/1599620810-HdOlMi-image.png){:height=
# "200px"}
#
#
# 当光线照至边界时：若边界上的小孔为开启状态，则光线会射出；否则，光线会在小孔之间进行反射。特别地：
# 1. 若光线射向未打开的拐角（黑盒顶点），则光线会原路反射回去；
# 2. 光线自拐角处的小孔照入时，只有一种入射方向（如自序号为 0 的小孔照入方向只能为 `-1`）
#
# ![image.png](https://pic.leetcode-cn.com/1598953840-DLiAsf-image.png){:height=
# "200px"}
#
# 请帮助小扣判断并返回店长每次照入的光线从几号小孔射出。
#
#
# **示例 1：**
# >输入：
# >`["BlackBox","open","open","open","close","open"]`
# >`[[2,3],[6,-1],[4,-1],[0,-1],[6],[0,-1]]`
# >
# >输出：`[null,6,4,6,null,4]`
# >
# >解释：
# >BlackBox b = BlackBox(2,3); // 新建一个 2x3 的黑盒
# >b.open(6,-1) // 打开 6 号小孔，并沿 y=-x 方向照入光线，光线至 0 号小孔反射，从 6 号小孔射出
# >b.open(4,-1) // 打开 4 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 4-2-8-2-4，从 4 号小孔射出
# >b.open(0,-1) // 打开 0 号小孔，并沿 y=-x 方向照入光线，由于 6 号小孔为开启状态，光线从 6 号小孔射出
# >b.close(6) // 关闭 6 号小孔
# >b.shoot(0,-1) // 从 0 号小孔沿 y=-x 方向照入光线，由于 6 号小孔为关闭状态，4 号小孔为开启状态，光线轨迹为 0-6-4，从
# 4 号小孔射出
#
# **示例 2：**
# >输入：
# >`["BlackBox","open","open","open","open","close","open","close","open"]`
# >`[[3,3],[1,-1],[5,1],[11,-1],[11,1],[1],[11,1],[5],[11,-1]]`
# >
# >输出：`[null,1,1,5,1,null,5,null,11]`
# >
# >解释：
# >
# >![image.png](https://pic.leetcode-cn.com/1599204202-yGDMVk-image.png){:height
# ="300px"}
# >
# >BlackBox b = BlackBox(3,3); // 新建一个 3x3 的黑盒
# >b.open(1,-1) // 打开 1 号小孔，并沿 y=-x 方向照入光线，光线轨迹为 1-5-7-11-1，从 1 号小孔射出
# >b.open(5,1) // 打开 5 号小孔，并沿 y=x 方向照入光线，光线轨迹为 5-7-11-1，从 1 号小孔射出
# >b.open(11,-1) // 打开 11 号小孔，并沿逆 y=-x 方向照入光线，光线轨迹为 11-7-5，从 5 号小孔射出
# >b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1，从 1 号小孔射出
# >b.close(1) // 关闭 1 号小孔
# >b.open(11,1) // 从 11 号小孔沿 y=x 方向照入光线，光线轨迹为 11-1-5，从 5 号小孔射出
# >b.close(5) // 关闭 5 号小孔
# >b.open(11,-1) // 从 11 号小孔沿 y=-x 方向照入光线，光线轨迹为 11-1-5-7-11，从 11 号小孔射出
#
#
#
# **提示：**
# - `1 <= n, m <= 10000`
# - `1 <= 操作次数 <= 10000`
# - `direction` 仅为 `1` 或 `-1`
# - `0 <= index < 2*(m+n)`
#  Related Topics 设计 线段树 数学 有序集合
#  👍 14 👎 0

# https://leetcode-cn.com/problems/IQvJ9i/solution/yu-chu-li-chu-suo-you-de-zu-by-zerotrac2/
from sortedcontainers import SortedSet


class BlackBox:

    def __init__(self, n: int, m: int):
        self.groupNeg, self.groupPos, self.groupstatus = [], [], []
        cnt = 2 * (n + m)
        self.groupNeg, self.groupPos = [(-1, -1) for _ in range(cnt)], [(-1, -1) for _ in range(cnt)]
        for index in range(cnt):
            if index != 0 and index != n + m and self.groupPos[index][0] == -1:  # 左上角，右下角不能进行y=x照射，再排除已经遍历的状态
                self.creatgroup(n, m, index, 1)
            if index != m and index != 2 * m + n and self.groupNeg[index][0] == -1:  # 右上角，左下角不能进行y=-x照射，再排除已经遍历到的状态
                self.creatgroup(n, m, index, -1)

    def creatgroup(self, n, m, index, dir):
        id = len(self.groupstatus)  # 状态id，这里的状态是一个整体的大的循环
        self.groupstatus.append(SortedSet())
        loc = 0  # 设置每一个大循环的初始位置
        while dir == 1 and self.groupPos[index][0] == -1 or dir == -1 and self.groupNeg[index][0] == -1:  # 如果某个index孔已经在某个循环中遍历到了，则结束目前的循环
            if dir == 1:
                self.groupPos[index] = (id, loc)
                index = 2 * (m + n) - index
            else:
                self.groupNeg[index] = (id, loc)
                index = 2 * m - index if index <= 2 * m else 4 * m + 2 * n - index
            if index not in (0, m, m + n, 2 * m + n):  # 除4个角外，其余的方向会改变
                dir *= -1
            loc += 1

    def open(self, index: int, direction: int) -> int:
        id, loc = self.groupPos[index]  # 将小孔两个方向都加入到对应的循环数组中
        if id != -1:
            self.groupstatus[id].add((loc, index))
        id, loc = self.groupNeg[index]
        if id != -1:
            self.groupstatus[id].add((loc, index))
        id, loc = self.groupPos[index] if direction == 1 else self.groupNeg[index]
        p = self.groupstatus[id].bisect_left((loc, index))
        if p == len(self.groupstatus[id]) - 1:  # 该状态是状态集合中最后一个，则返回第一个，否则返回下一个
            ans = self.groupstatus[id][0][1]
        else:
            ans = self.groupstatus[id][p + 1][1]
        return ans

    def close(self, index: int) -> None:
        id, loc = self.groupPos[index]
        if id != -1:  # 对于四个角的小孔，id是有可能等于-1的
            self.groupstatus[id].discard((loc, index))
        id, loc = self.groupNeg[index]
        if id != -1:
            self.groupstatus[id].discard((loc, index))


# 复写

from sortedcontainers import SortedSet
class BlackBox:

    def __init__(self, n: int, m: int):
        cnt = 2 * (m + n)
        self.neg, self.pos, self.status = [], [], []
        self.neg, self.pos = [(-1, -1) for _ in range(cnt)], [(-1, -1) for _ in range(cnt)]
        for index in range(cnt):
            if index != 0 and index != n + m and self.pos[index][0] == -1:
                self.creatgroup(n, m, index, 1)
            if index != m and index != 2 * m + n and self.neg[index][0] == -1:
                self.creatgroup(n, m, index, -1)

    def creatgroup(self, n, m, index, dir):
        id = len(self.status)
        self.status.append(SortedSet())
        loc = 0
        while dir == 1 and self.pos[index][0] == -1 or dir == -1 and self.neg[index][0] == -1:
            if dir == 1:
                self.pos[index] = (id, loc)
                index = 2 * (m + n) - index
            else:
                self.neg[index] = (id, loc)
                index = 2 * m - index if index <= 2 * m else 4 * m + 2 * n - index
            if index not in (0, m, m + n, 2 * m + n):
                dir *= -1
            loc += 1

    def open(self, index: int, direction: int) -> int:
        id, loc = self.pos[index]
        if id != -1:
            self.status[id].add((loc, index))
        id, loc = self.neg[index]
        if id != -1:
            self.status[id].add((loc, index))
        id, loc = self.pos[index] if direction == 1 else self.neg[index]
        p = self.status[id].bisect_left((loc, index))
        if p == len(self.status[id]) - 1:
            ans = self.status[id][0][1]
        else:
            ans = self.status[id][p + 1][1]
        return ans

    def close(self, index: int) -> None:
        id, loc = self.pos[index]
        if id != -1:
            self.status[id].discard((loc, index))
        id, loc = self.neg[index]
        if id != -1:
            self.status[id].discard((loc, index))


# Your BlackBox object will be instantiated and called as such:
obj = BlackBox(2, 3)
obj.open(6, -1)
obj.open(4, -1)
