# -*- coding: utf-8 -*-
# 小扣出去秋游，途中收集了一些红叶和黄叶，他利用这些叶子初步整理了一份秋叶收藏集 `leaves`， 字符串 `leaves` 仅包含小写字符 `r` 和 `
# y`， 其中字符 `r` 表示一片红叶，字符 `y` 表示一片黄叶。
# 出于美观整齐的考虑，小扣想要将收藏集中树叶的排列调整成「红、黄、红」三部分。每部分树叶数量可以不相等，但均需大于等于 1。每次调整操作，小扣可以将一片红叶替
# 换成黄叶或者将一片黄叶替换成红叶。请问小扣最少需要多少次调整操作才能将秋叶收藏集调整完毕。
#
# **示例 1：**
# >输入：`leaves = "rrryyyrryyyrr"`
# >
# >输出：`2`
# >
# >解释：调整两次，将中间的两片红叶替换成黄叶，得到 "rrryyyyyyyyrr"
#
# **示例 2：**
# >输入：`leaves = "ryr"`
# >
# >输出：`0`
# >
# >解释：已符合要求，不需要额外操作
#
# **提示：**
# - `3 <= leaves.length <= 10^5`
# - `leaves` 中只包含字符 `'r'` 和字符 `'y'` Related Topics 字符串 动态规划
#  👍 197 👎 0

# 1动态规划
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        f = [[float('inf')] * 3 for _ in range(len(leaves))]
        n = len(leaves)
        # f[i][j] i代表位置 j代表状态，0 前段红，1中段黄 2后段红
        f[0][0] = 1 if leaves[0] == 'y' else 0
        for i in range(1, n):
            f[i][0] = min(f[i][0], f[i - 1][0] + int(leaves[i] == 'y'))
            f[i][1] = min(f[i][1], f[i - 1][0] + int(leaves[i] == 'r'), f[i - 1][1] + int(leaves[i] == 'r'))
            f[i][2] = min(f[i][2], f[i - 1][1] + int(leaves[i] == 'y'), f[i - 1][2] + int(leaves[i] == 'y'))
        return f[-1][2]


# 2公式推导
# https://leetcode-cn.com/problems/UlBDOe/solution/qiu-xie-shou-cang-ji-by-leetcode-solution/
# 补充下x!=y!=n-1
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        g = 1 if leaves[0] == 'y' else -1
        gmin = g
        ans = float('inf')
        for i in range(1, n):
            g += 2 * (int(leaves[i] == 'y')) - 1
            if i != n - 1:
                ans = min(ans, gmin - g)
            gmin = min(g, gmin)
        return ans + (g + n) // 2


Solution().minimumOperations("yry")
