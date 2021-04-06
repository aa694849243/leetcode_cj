'''在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用最短的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。

 

示例 1:

输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
解释:

示例 2:

输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]
解释:

即使树都在一条直线上，你也需要先用绳子包围它们。
 

注意:

所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
输入的整数在 0 到 100 之间。
花园至少有一棵树。
所有树的坐标都是不同的。
输入的点没有顺序。输出顺序也没有要求。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/erect-the-fence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1 jarvis算法
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def oriented(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])  # 相当于 负sinx的值，如果-sinx大于0说明qr相对于pq右拐了，则q点作为内部点可以忽略，反之-sinx小于0说明qr相对于pq左拐了，可以正常添加r点到序列中

        def inbetween(p, i, q):
            a = p[0] <= i[0] <= q[0] or q[0] <= i[0] <= p[0]
            b = p[1] <= i[1] <= q[1] or q[1] <= i[1] <= p[1]
            return a and b

        if len(points) < 4:
            return points
        points.sort()
        m = set()
        p = 0
        q = 1
        hull = []
        while q != 0:
            hull.append(points[p])
            m.add(p)
            q = (p + 1) % len(points)
            for r in range(len(points)):
                if oriented(points[p], points[r], points[q]) < 0:  # 发生右拐,r比q更近
                    q = r
            for r in range(len(points)):
                if r != p and r != q and oriented(points[p], points[q], points[r]) == 0 and inbetween(points[p], points[r], points[q]) and r not in m:
                    hull.append(points[r])  # r值不能与p,q重合，因为0与任何向量的sin值都为0，同时如果r点在p,q之间则将r点添加，否则r点会作为下一个最近点添加到hull里
                    m.add(r)  # 防止一条竖直的线的情况
            p = q
        return hull


# 2 Graham 扫描
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def oriented(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        def cos(origin, p):  # cos值
            return round((p[0] - origin[0]) / (distance(origin, p) ** 0.5), 7)  # 根据我调试后发现保留7位小数可以得到正确结果，太低或太高都不行

        def distance(origin, p):  # 距离的平方
            return (p[1] - origin[1]) ** 2 + (p[0] - origin[0]) ** 2

        if len(points) < 4:
            return points
        points.sort(key=lambda x: (x[1], x[0]))  # 先根据y值排序，y值相同则根据x值排序
        origin = points[0]
        polors = []  # 极坐标列表
        m = {}  # 储存极坐标与原坐标的对应关系
        for i in range(1, len(points)):
            polor = (cos(origin, points[i]), distance(origin, points[i]))
            m[polor] = points[i]
            polors.append(polor)
        polors.sort(key=lambda x: (-x[0], x[1]))  # 先根据cos值逆序排序，如果相同则距离近的排前面
        x = polors[-1][0]  # 最后一条边的cos值
        xs = []
        for i in range(len(polors) - 1, -1, -1):  # 最后一条边如果共线的点则需要反转顺序，即由远到近排序
            if polors[i][0] == x:
                xs.append(polors[i])
            else:
                break
        polors = polors[:i + 1] + xs if round(polors[i][0], 5) != x else xs
        stack = [origin, m[polors[0]]]  # 栈里面先储存两点
        for i in range(1, len(polors)):
            r = m[polors[i]]
            while len(stack) >= 2 and oriented(stack[-2], r, stack[-1]) < 0:  # 发生右拐，弹出栈顶的点
                stack.pop()
            stack.append(r)
        return stack
#
#
# # 3单调链
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        def oriented(p, q, r):
            return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])

        if len(points) < 4:
            return points

        points.sort()  # 按照x值正序排列
        hull = [points[0], points[1]]
        for i in range(2, len(points)):
            r = points[i]
            while len(hull) >= 2 and oriented(hull[-2], r, hull[-1]) < 0:
                hull.pop()
            hull.append(r)
        m = set()
        for p in hull:  # 将已经添加的树储存到集合中
            m.add(tuple(p))
        points = points[::-1]  # 按照x值逆序排列
        for i in range(1, len(points)):
            r = points[i]
            while len(hull) >= 2 and oriented(hull[-2], r, hull[-1]) < 0:
                hull.pop()
            if tuple(r) not in m:
                hull.append(r)
                m.add(tuple(r))
        return hull


a = [[0, 0], [74, 1], [74, 91], [76, 1], [77, 40], [77, 95], [79, 1], [85, 23], [85, 44]]


def cal(a, b):
    for i in a:
        if i not in b:
            return False
    return True


Solution().outerTrees([[0, 0], [1, 0], [2, 0], [3, 0], [3, 1], [3, 2], [3, 3], [1, 1], [2, 2], [1, 2], [0, 2], [0, 1]])
