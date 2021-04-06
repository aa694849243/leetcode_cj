'''
在二维平面上计算出两个由直线构成的矩形重叠后形成的总面积。

每个矩形由其左下顶点和右上顶点坐标表示，如图所示。



示例:

输入: -3, 0, 3, 4, 0, -1, 9, 2
输出: 45
说明: 假设矩形面积不会超出 int 的范围。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rectangle-area
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        s = abs(D - B) * abs(C - A) + abs(H - F) * abs(G - E)
        area = max((C - A + G - E) - max(C,G)+min(A,E), 0) * max(D - B + H - F - max(D,H)+min(B,F), 0)
        return s - area


x = [-3, 0, 3, 4, 0, -1, 9, 2]
y=[-2, -2, 2, 2, 3, 3, 4, 4]
z=[0, 0, 0, 0, -1, -1, 1, 1]
Solution().computeArea(*z)
