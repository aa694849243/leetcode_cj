# -*- coding: utf-8 -*-
# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
#
#  给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。
#
#
#
#  示例 1：
#
#
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
#
#
#  示例 2：
#
#
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
#
#
#  示例 3：
#
#
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
#
#
#
#  提示：
#
#
#  1 <= n <= 2 * 10⁹
#
#
#  Related Topics 数学 动态规划
#  👍 45 👎 0
import functools


# leetcode submit region begin(Prohibit modification and deletion)
# 数位dp
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        @functools.lru_cache(None)
        def dp(m, n):  # m种选择，n位数
            if n == 0:
                return 1
            return (m - n + 1) * dp(m, n - 1)  # 已经选掉了n-1位数，剩下的m-n+1种选择

        s = list(map(int, str(n + 1)))
        ans = 0
        for i in range(1, len(s)):  # 从1位数开始，直到n-1位数，全部的数都可以打满
            ans += 9 * dp(9, i - 1)  # 第1位数有9种选择,后面n-1位数也有9种选择，因为可以为0
        visted = set()
        for i, num in enumerate(s): # 如果是999这样的数，此部分值为0
            if i == 0:
                cur_canuse = num - 1  # 当前位可以用的数字数量
            else:
                cur_canuse = len([x for x in range(num) if x not in visted])  # 不是第一位，x可以为0
            ans += cur_canuse * dp(10 - i - 1, len(s) - i - 1)
            if num in visted: # 如果当前位顶格数字已经出现过，后面的位数就不用再考虑了
                break
            visted.add(num)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().countSpecialNumbers(20))