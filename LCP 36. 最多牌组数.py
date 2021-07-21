# -*- coding: utf-8 -*-
import collections
from typing import List


# 麻将的游戏规则中，共有两种方式凑成「一组牌」：
# - 顺子：三张牌面数字连续的麻将，例如 [4,5,6]
# - 刻子：三张牌面数字相同的麻将，例如 [10,10,10]
#
# 给定若干数字作为麻将牌的数值（记作一维数组 `tiles`），请返回所给 `tiles` 最多可组成的牌组数。
#
# 注意：凑成牌组时，每张牌仅能使用一次。
#
# **示例 1：**
# >输入：`tiles = [2,2,2,3,4]`
# >
# >输出：`1`
# >
# >解释：最多可以组合出 [2,2,2] 或者 [2,3,4] 其中一组牌。
#
# **示例 2：**
# >输入：`tiles = [2,2,2,3,4,1,3]`
# >
# >输出：`2`
# >
# >解释：最多可以组合出 [1,2,3] 与 [2,3,4] 两组牌。
#
# **提示：**
# - `1 <= tiles.length <= 10^5`
# - `1 <= tiles[i] <= 10^9` Related Topics 数组 动态规划 排序
#  👍 10 👎 0


class Solution:
    def maxGroupNumber(self, tiles: List[int]) -> int:
        m = collections.Counter(tiles)
        dp = {(0, 0): 0}
        for num in sorted(m):
            ndp=collections.defaultdict(int)
            x,y,z=m[num],m[num+1],m[num+2]
            for (i,j),c in dp.items():
                for k in range(3):
                    if i+k<=x and j+k<=y and k<=z:
                        ndp[j+k,k]=max(ndp[j+k,k],c+(x-i-k)//3+k)
            dp=ndp
        return max(dp.values())
Solution().maxGroupNumber([2,2,2,3,3,3,4,4,4,4,7,7,7,8,9,9,10,10])