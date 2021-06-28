# -*- coding: utf-8 -*-
#
#
#  二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 A 位于坐标 (0,0)，字母 B 位于坐标 (0,1
# )，字母 P 位于坐标 (2,3) 且字母 Z 位于坐标 (4,1)。
#
#  给你一个待输入字符串 word，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 (x1,y1) 和 (x2,y2) 之间的
# 距离是 |x1 - x2| + |y1 - y2|。
#
#  注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。
#
#
#
#  示例 1：
#
#  输入：word = "CAKE"
# 输出：3
# 解释：
# 使用两根手指输入 "CAKE" 的最佳方案之一是：
# 手指 1 在字母 'C' 上 -> 移动距离 = 0
# 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'C' 到字母 'A' 的距离 = 2
# 手指 2 在字母 'K' 上 -> 移动距离 = 0
# 手指 2 在字母 'E' 上 -> 移动距离 = 从字母 'K' 到字母 'E' 的距离  = 1
# 总距离 = 3
#
#
#  示例 2：
#
#  输入：word = "HAPPY"
# 输出：6
# 解释：
# 使用两根手指输入 "HAPPY" 的最佳方案之一是：
# 手指 1 在字母 'H' 上 -> 移动距离 = 0
# 手指 1 在字母 'A' 上 -> 移动距离 = 从字母 'H' 到字母 'A' 的距离 = 2
# 手指 2 在字母 'P' 上 -> 移动距离 = 0
# 手指 2 在字母 'P' 上 -> 移动距离 = 从字母 'P' 到字母 'P' 的距离 = 0
# 手指 1 在字母 'Y' 上 -> 移动距离 = 从字母 'A' 到字母 'Y' 的距离 = 4
# 总距离 = 6
#
#
#  示例 3：
#
#  输入：word = "NEW"
# 输出：3
#
#
#  示例 4：
#
#  输入：word = "YEAR"
# 输出：7
#
#
#
#
#  提示：
#
#
#  2 <= word.length <= 300
#  每个 word[i] 都是一个大写英文字母。
#
#  Related Topics 字符串 动态规划
#  👍 57 👎 0

#朴素的动态规划
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        dp = [[[float('inf') for _ in range(26)] for _ in range(26)] for _ in range(n)]
        # dp[pos][l][r]
        init=ord(word[0])-65
        for i in range(26):
            dp[0][i][init] = 0  # 右手处于pos，左手乱放
            dp[0][init][i] = 0  # 左手处于pos，右手乱放

        def distance(p, q):
            x1, y1 = divmod(p, 6)
            x2, y2 = divmod(q, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        for pos, ch in enumerate(word[1:], 1):
            cur, prev = ord(ch) - 65, ord(word[pos - 1]) - 65
            d = distance(cur, prev)
            for j in range(26):
                dp[pos][cur][j] = min(dp[pos - 1][prev][j] + d, dp[pos][cur][j])  # 左手处于prev，左手转移，右手位置不变
                dp[pos][j][cur] = min(dp[pos - 1][j][prev] + d, dp[pos][j][cur])  # 右手处于prev，右手转移，左手位置不变
                if prev == j:  # prev处于左手，但右手转移到cur或者prev处于右手，左手转移到ur
                    for k in range(26):
                        nd = distance(cur, k)
                        dp[pos][cur][prev] = min(dp[pos - 1][k][prev] + nd, dp[pos][cur][prev])  # 右手处于prev,左手转移到cur
                        dp[pos][prev][cur] = min(dp[pos - 1][prev][k] + nd, dp[pos][prev][cur])  # 左手处于prev,右手转移到cur
        ans = min(min(dp[-1][k]) for k in range(26))
        return ans
#2优化空间，对称模式
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        dp=[[float('inf') for _ in range(26)] for _ in range(n)]
        init=ord(word[0])-65
        for i in range(26):
            dp[0][i]=0 #初始情况，不论另一只手摆在哪里，都是0

        def distance(p, q):
            x1, y1 = divmod(p, 6)
            x2, y2 = divmod(q, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        for pos in range(1,n):
            cur,prev=ord(word[pos])-65,ord(word[pos-1])-65
            d=distance(cur,prev)
            for j in range(26):
                dp[pos][j]=min(dp[pos][j],dp[pos-1][j]+d) #pos-1手转移到pos，当前手处于pos,另一只手处于j
                if j==prev:
                    for k in range(26):
                        nd=distance(k,cur)
                        dp[pos][j]=min(dp[pos][j],dp[pos-1][k]+nd) #k手转移到pos,另一只手变成pos-1字母处的手，即j处
        return min(dp[-1])

Solution().minimumDistance("NEW")