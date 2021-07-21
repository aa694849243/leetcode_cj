# -*- coding: utf-8 -*-
# 小扣在秋日市集购买了一个古董键盘。由于古董键盘年久失修，键盘上只有 26 个字母 **a~z** 可以按下，且每个字母最多仅能被按 `k` 次。
#
# 小扣随机按了 `n` 次按键，请返回小扣总共有可能按出多少种内容。由于数字较大，最终答案需要对 1000000007 (1e9 + 7) 取模。
#
#
# **示例 1：**
# >输入：`k = 1, n = 1`
# >
# >输出：`26`
# >
# >解释：由于只能按一次按键，所有可能的字符串为 "a", "b", ... "z"
#
# **示例 2：**
# >输入：`k = 1, n = 2`
# >
# >输出：`650`
# >
# >解释：由于只能按两次按键，且每个键最多只能按一次，所有可能的字符串（按字典序排序）为 "ab", "ac", ... "zy"
#
# **提示：**
# - `1 <= k <= 5`
# - `1 <= n <= 26*k`
#
#
#  Related Topics 数学 动态规划 组合数学
#  👍 23 👎 0
import functools
import math


class Solution:
    def keyboard(self, k: int, n: int) -> int:
        mod = 10 ** 9 + 7

        @functools.lru_cache(None)
        def dfs(i, s, rem):  # i代表多少号字母,s代表字母总数，rem代表剩余数量
            if i == s-1: #最后一个字母，只能填剩下的坑
                return 1
            ans = 0
            for cnt in range(1, k + 1):
                if s - i - 1 > rem - cnt: #格子不够用了
                    break
                if rem-cnt>k*(s-i-1): #字母种类乘以最大数量也填不满坑
                    continue
                ans += math.comb(rem, cnt) * dfs(i + 1, s, rem - cnt)

            return ans % mod

        res = 0
        for vars in range(1, 27):
            if vars > n:
                break
            if vars * k < n:
                continue
            res += math.comb(26, vars) * dfs(0, vars, n)
        return res % mod


Solution().keyboard(2, 7)
