'''我们有 N 个与坐标轴对齐的矩形, 其中 N > 0, 判断它们是否能精确地覆盖一个矩形区域。

每个矩形用左下角的点和右上角的点的坐标来表示。例如， 一个单位正方形可以表示为 [1,1,2,2]。 ( 左下角的点的坐标为 (1, 1) 以及右上角的点的坐标为 (2, 2) )。



示例 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

返回 true。5个矩形一起可以精确地覆盖一个矩形区域。
 



示例 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

返回 false。两个矩形之间有间隔，无法覆盖成一个矩形。
 



示例 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

返回 false。图形顶端留有间隔，无法覆盖成一个矩形。
 



示例 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

返回 false。因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/perfect-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# https://leetcode-cn.com/problems/perfect-rectangle/solution/wan-mei-ju-xing-by-powcai/
# 除了最终矩形的四个端点，其他内部或边界的点一定要是偶数个，此外为了避免有空心和重叠的区域，需要保证面积符合
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        xmax = float('-inf')
        ymax = float('-inf')
        xmin = float('inf')
        ymin = float('inf')
        lookup = set()
        area = 0
        for x1, y1, x2, y2 in rectangles:
            xmax = max(x2, xmax)
            ymax = max(y2, ymax)
            xmin = min(x1, xmin)
            ymin = min(y1, ymin)
            area+=(y2-y1)*(x2-x1)
            for dot in [(x1,y1),(x2,y2),(x1,y2),(x2,y1)]:
                if dot in lookup:
                    lookup.remove(dot)
                else:
                    lookup.add(dot)
        if {(xmin,ymin),(xmin,ymax),(xmax,ymin),(xmax,ymax)}==lookup and area==(xmax-xmin)*(ymax-ymin):
            return True
        return False

a=[[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
Solution().isRectangleCover(a)