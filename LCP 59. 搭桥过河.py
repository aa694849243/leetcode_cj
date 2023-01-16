# -*- coding: utf-8 -*-
# 欢迎各位勇者来到力扣城，本次试炼主题为「搭桥过河」。
#
# 勇者面前有一段长度为 `num` 的河流，河流可以划分为若干河道。每条河道上恰有一块浮木，`wood[i]` 记录了第 `i` 条河道上的浮木初始的覆盖范围
# 。
#
# - 当且仅当浮木与相邻河道的浮木覆盖范围有重叠时，勇者才可以在两条浮木间移动
# - 勇者 **仅能在岸上** 通过花费一点「自然之力」，使任意一条浮木沿着河流移动一个单位距离
#
# 请问勇者跨越这条河流，最少需要花费多少「自然之力」。
#
# **示例 1：**
#
# > 输入： `num = 10, wood = [[1,2],[4,7],[8,9]]`
# > 输出： `3`
# > 解释：如下图所示，
# > 将 [1,2] 浮木移动至 [3,4]，花费 2「自然之力」，
# > 将 [8,9] 浮木移动至 [7,8]，花费 1「自然之力」，
# > 此时勇者可以顺着 [3,4]->[4,7]->[7,8] 跨越河流，
# > 因此，勇者最少需要花费 3 点「自然之力」跨越这条河流
# > ![wood (2).gif](https://pic.leetcode-cn.com/1648196478-ophADL-wood%20(2).
# gif)
#
# **示例 2：**
#
# > 输入： `num = 10, wood = [[1,5],[1,1],[10,10],[6,7],[7,8]]`
# > 输出： `10`
# > 解释：
# > 将 [1,5] 浮木移动至 [2,6]，花费 1「自然之力」，
# > 将 [1,1] 浮木移动至 [6,6]，花费 5「自然之力」，
# > 将 [10,10] 浮木移动至 [6,6]，花费 4「自然之力」，
# > 此时勇者可以顺着 [2,6]->[6,6]->[6,6]->[6,7]->[7,8] 跨越河流，
# > 因此，勇者最少需要花费 10 点「自然之力」跨越这条河流
#
# **示例 3：**
#
# > 输入： `num = 5, wood = [[1,2],[2,4]]`
# > 输出： `0`
# > 解释：勇者不需要移动浮木，仍可以跨越这条河流
#
# **提示:**
# - `1 <= num <= 10^9`
# - `1 <= wood.length <= 10^5`
# - `wood[i].length == 2`
# - `1 <= wood[i][0] <= wood[i][1] <= num`
#
#  Related Topics 数组 动态规划
#  👍 4 👎 0

import heapq
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:  # 斜率差分
    def buildBridge(self, num: int, wood: List[List[int]]) -> int:
        biasl, biasr = 0, 0
        lq, rq = [-wood[0][0]], [wood[0][0]]
        ans = 0
        for i in range(1, len(wood)):
            biasl -= wood[i][1] - wood[i][0]  # 标记偏移点
            biasr += wood[i - 1][1] - wood[i - 1][0]
            L, R = -lq[0] + biasl, rq[0] + biasr
            if wood[i][0] < L:
                ans += L - wood[i][0]
                heapq.heappop(lq)
                heapq.heappush(lq, -(wood[i][0] - biasl))  # 插入li点，减去biasl是因为后面考虑左右边界的时候得加回来,斜率差为2
                heapq.heappush(lq, -(wood[i][0] - biasl))  # 插入长度为0的线段这里斜率变为-1了
                heapq.heappush(rq, L - biasr)  # 预计算的L变为右边界
            elif wood[i][0] > R:
                ans += wood[i][0] - R
                heapq.heappop(rq)
                heapq.heappush(rq, wood[i][0] - biasr)
                heapq.heappush(rq, wood[i][0] - biasr)
                heapq.heappush(lq, -(R - biasl))
            else:
                heapq.heappush(lq, -(wood[i][0] - biasl))
                heapq.heappush(rq, wood[i][0] - biasr)
        return ans


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().buildBridge(10, [[1, 2], [4, 7], [8, 9]]))
