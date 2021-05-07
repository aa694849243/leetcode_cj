# -*- coding: utf-8 -*-
import collections, heapq, itertools
from typing import List


# 如果一个由 '0' 和 '1' 组成的字符串，是以一些 '0'（可能没有 '0'）后面跟着一些 '1'（也可能没有 '1'）的形式组成的，那么该字符串是单调
# 递增的。
#
#  我们给出一个由字符 '0' 和 '1' 组成的字符串 S，我们可以将任何 '0' 翻转为 '1' 或者将 '1' 翻转为 '0'。
#
#  返回使 S 单调递增的最小翻转次数。
#
#
#
#  示例 1：
#
#  输入："00110"
# 输出：1
# 解释：我们翻转最后一位得到 00111.
#
#
#  示例 2：
#
#  输入："010110"
# 输出：2
# 解释：我们翻转得到 011111，或者是 000111。
#
#
#  示例 3：
#
#  输入："00011000"
# 输出：2
# 解释：我们翻转得到 00000000。
#
#
#
#
#  提示：
#
#
#  1 <= S.length <= 20000
#  S 中只包含字符 '0' 和 '1'
#
#  Related Topics 数组
#  👍 93 👎 0


class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        S = S.lstrip('0').rstrip('1')
        if not S:
            return 0
        li = [0] * len(S)
        li[-1] = 1
        for i in range(len(S) - 2, -1, -1):
            if S[i] == '0':
                li[i] = li[i + 1] + 1
            else:
                li[i] = li[i + 1]
        ans = float('inf')[1,0,1,0,1]
        l = 0
        cnt1 = 0
        pre = 0
        while l < len(S):
            while S[l] == '1':
                cnt1 += 1
                l += 1
            ans = min(pre+li[l], ans)
            while l < len(S) and S[l] == '0':
                l += 1
            cnt0 = li[l] if l < len(S) else 0
            pre=cnt1
            ans = min(cnt1 + cnt0, ans)
        return ans


Solution().minFlipsMonoIncr("010110")
