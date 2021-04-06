'''给定二维空间中四点的坐标，返回四点是否可以构造一个正方形。

一个点的坐标（x，y）由一个有两个整数的整数数组表示。

示例:

输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True
 

注意:

所有输入整数都在 [-10000，10000] 范围内。
一个有效的正方形有四个等长的正长和四个等角（90度角）。
输入点没有顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1正方形排序
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        sqare = sorted([tuple(p1), tuple(p2), tuple(p3), tuple(p4)])
        if len(set(sqare))!=4:
            return False
        side1 = (sqare[0][0] - sqare[1][0]) ** 2 + (sqare[0][1] - sqare[1][1]) ** 2
        side2 = (sqare[0][0] - sqare[2][0]) ** 2 + (sqare[0][1] - sqare[2][1]) ** 2
        side3 = (sqare[3][0] - sqare[2][0]) ** 2 + (sqare[3][1] - sqare[2][1]) ** 2
        side4 = (sqare[3][0] - sqare[1][0]) ** 2 + (sqare[3][1] - sqare[1][1]) ** 2
        side5 = (sqare[0][0] - sqare[3][0]) ** 2 + (sqare[0][1] - sqare[3][1]) ** 2
        side6 = (sqare[1][0] - sqare[2][0]) ** 2 + (sqare[1][1] - sqare[2][1]) ** 2
        return side1 == side2 == side3 == side4 and side5==side6
Solution().validSquare([1,1], [5,3], [3,5], [7,7])