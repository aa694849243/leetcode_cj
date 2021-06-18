# -*- coding: utf-8 -*-
import collections
from typing import List


# 数轴上放置了一些筹码，每个筹码的位置存在数组 chips 当中。
#
#  你可以对 任何筹码 执行下面两种操作之一（不限操作次数，0 次也可以）：
#
#
#  将第 i 个筹码向左或者右移动 2 个单位，代价为 0。
#  将第 i 个筹码向左或者右移动 1 个单位，代价为 1。
#
#
#  最开始的时候，同一位置上也可能放着两个或者更多的筹码。
#
#  返回将所有筹码移动到同一位置（任意位置）上所需要的最小代价。
#
#
#
#  示例 1：
#
#  输入：chips = [1,2,3]
# 输出：1
# 解释：第二个筹码移动到位置三的代价是 1，第一个筹码移动到位置三的代价是 0，总代价为 1。
#
#
#  示例 2：
#
#  输入：chips = [2,2,2,3,3]
# 输出：2
# 解释：第四和第五个筹码移动到位置二的代价都是 1，所以最小总代价为 2。
#
#
#
#
#  提示：
#
#
#  1 <= chips.length <= 100
#  1 <= chips[i] <= 10^9
#
#  Related Topics 贪心算法 数组 数学
#  👍 92 👎 0


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        m = collections.Counter(position)
        li = m.keys()
        ans = float('inf')
        for key in li:
            for t in [key - 2, key - 1, key, key + 1, key + 2]:
                steps = 0
                if t < 1 or t > 10 ** 9:
                    continue
                if t == key - 1 or t == key + 1:
                    steps += m[key]
                for key2 in li:
                    if key2 != key:
                        steps += (abs(key2 - t) % 2) * m[key2]
                ans = min(ans, steps)
        return ans


# 奇偶
# 奇数移到一起不花任何代价，偶数移到一起不花任何代价，奇数移到偶数或偶数移到奇数代价为1
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ou_l = len([i for i in position if i % 2 == 0])
        ji_l = len(position) - ou_l
        return min(ou_l, ji_l)


#
# 作者：westqi
# 链接：https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position/solution/1217-wan-chou-ma-by-westqi-mef2/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
Solution().minCostToMoveChips([2, 2, 2, 3, 3])
