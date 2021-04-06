'''有两个容量分别为 x升 和 y升 的水壶以及无限多的水。请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？

如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶
清空任意一个水壶
从一个水壶向另外一个水壶倒水，直到装满或者倒空
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4
输出: True
示例 2:

输入: x = 2, y = 6, z = 5
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/water-and-jug-problem
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1 栈 模拟递归
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 and y == 0:
            return not z
        elif x == 0:
            return z % y == 0
        elif y == 0:
            return z % x == 0
        stack = [(0, 0)]
        seen = set()
        while stack:
            a = stack.pop()
            if a not in seen:
                seen |= {a}
            else:
                continue

            rx, ry = a[0], a[1]
            if rx + ry == z:
                return True
            if rx > x or ry > y:
                continue
            # 1 将x倒满
            stack.append((x, ry))
            # 2 将y倒满
            stack.append((rx, y))
            # 3 将x 倒掉
            stack.append((0, ry))
            # 4 将y 倒掉
            stack.append((rx, 0))
            # 5 x倒入y，x倒空,y未满
            if rx + ry < y:
                stack.append((0, rx + ry))
            # 6 x倒入y, y 满了,则要把y倒掉
            if rx + ry > y:
                stack.append((rx + ry - y, 0))
            # 7 y 倒入x,y倒空，x未满
            if rx + ry < x:
                stack.append((rx + ry, 0))
            # 8 y倒入x，x满了，则要把x倒掉
            if rx + ry > x:
                stack.append((0, rx + ry - x))
        return False


# 2 数学 贝祖定理
import math


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x + y < z:
            return False
        if x == 0 and y == 0:
            return not z
        elif x == 0:
            return z % y == 0
        elif y == 0:
            return z % x == 0
        return z % math.gcd(x, y) == 0
