# 给你一个数组 rectangles ，其中 rectangles[i] = [xi, yi, ai, bi] 表示一个坐标轴平行的矩形。这个矩形的左下顶点是
#  (xi, yi) ，右上顶点是 (ai, bi) 。 
# 
#  如果所有矩形一起精确覆盖了某个矩形区域，则返回 true ；否则，返回 false 。 
# 
#  示例 1： 
#  
#  
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
# 输出：true
# 解释：5 个矩形一起可以精确地覆盖一个矩形区域。 
#  
# 
#  示例 2： 
#  
#  
# 输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
# 输出：false
# 解释：两个矩形之间有间隔，无法覆盖成一个矩形。 
# 
#  示例 3： 
#  
#  
# 输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
# 输出：false
# 解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= rectangles.length <= 2 * 10⁴ 
#  rectangles[i].length == 4 
#  -10⁵ <= xi, yi, ai, bi <= 10⁵ 
#  
# 
#  Related Topics 数组 扫描线 
#  👍 250 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        xmin = ymin = float('inf')
        xmax = ymax = float('-inf')
        cur_area = 0
        self.lookup = set()
        for x1, y1, x2, y2 in rectangles:
            xmin = min(xmin, x1)
            ymin = min(ymin, y1)
            xmax = max(xmax, x2)
            ymax = max(ymax, y2)
            cur_area += (x2 - x1) * (y2 - y1)
            self.lookup ^= {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}
        if cur_area==(xmax-xmin)*(ymax-ymin) and len(self.lookup)==4 and (xmin, ymin) in self.lookup and (xmin, ymax) in self.lookup and (xmax, ymin) in self.lookup and (xmax, ymax) in self.lookup:
            return True
        return False


# leetcode submit region end(Prohibit modification and deletion)
