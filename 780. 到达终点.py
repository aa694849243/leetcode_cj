'''从点 (x, y) 可以转换到 (x, x+y)  或者 (x+y, y)。

给定一个起点 (sx, sy) 和一个终点 (tx, ty)，如果通过一系列的转换可以从起点到达终点，则返回 True ，否则返回 False。

示例:
输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: True
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

输入: sx = 1, sy = 1, tx = 2, ty = 2
输出: False

输入: sx = 1, sy = 1, tx = 1, ty = 1
输出: True

注意:

sx, sy, tx, ty 是范围在 [1, 10^9] 的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reaching-points
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        if sx > tx or sy > ty:  # 因为序列只能不断增加或不变
            return False
        while sx <= tx and sy <= ty:
            if tx == ty:  # 不能再变换任何值了
                break
            if tx > ty:
                if ty > sy:
                    tx %= ty  # 只能用大的一直减小的
                elif ty == sy:  # ty不能再改变了,ty已经变的和初始一样小了，不能再变小了
                    return (tx - sx) % ty == 0  # tx % ty == sx 的话 9，3，3这种就输出False了
            elif tx < ty:
                if tx > sx:
                    ty %= tx
                elif tx == sx:
                    return (ty - sy) % tx == 0
        return sx == tx and sy == ty


Solution().reachingPoints(3, 3, 9, 12)
