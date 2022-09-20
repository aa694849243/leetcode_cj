import collections, heapq, itertools
# 有一个立方体房间，其长度、宽度和高度都等于 n 个单位。请你在房间里放置 n 个盒子，每个盒子都是一个单位边长的立方体。放置规则如下：
#
#
#  你可以把盒子放在地板上的任何地方。
#  如果盒子 x 需要放置在盒子 y 的顶部，那么盒子 y 竖直的四个侧面都 必须 与另一个盒子或墙相邻。
#
#
#  给你一个整数 n ，返回接触地面的盒子的 最少 可能数量。
#
#
#
#  示例 1：
#
#
#
#
# 输入：n = 3
# 输出：3
# 解释：上图是 3 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应左侧位置。
#
#
#  示例 2：
#
#
#
#
# 输入：n = 4
# 输出：3
# 解释：上图是 3 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应左侧位置。
#
#
#  示例 3：
#
#
#
#
# 输入：n = 10
# 输出：6
# 解释：上图是 10 个盒子的摆放位置。
# 这些盒子放在房间的一角，对应后方位置。
#
#
#
#  提示：
#
#
#  1 <= n <= 10⁹
#
#
#  Related Topics 贪心 数学 二分查找 👍 32 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 1,3,6,10通项公式
# https://zhidao.baidu.com/question/567727001.html
import bisect


class Solution:
    def minimumBoxes(self, n: int) -> int:
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if mid * (mid + 1) * (mid + 2) // 6 > n:
                r = mid
            else:
                l = mid + 1
        l -= 1
        cell = l * (l + 1) * (l + 2) // 6
        rest = n - cell
        ans = l * (l + 1) // 2
        l, r = 0, rest
        while l < r:
            mid = (l + r) // 2
            if mid * (mid + 1) // 2 < rest:
                l = mid + 1
            else:
                r = mid
        ans += l
        return ans


# leetcode submit region end(Prohibit modification and deletion)
Solution().minimumBoxes(126)
from typing import List
