# -*- coding: utf-8 -*-
# 给你一个只包含小写英文字母的字符串 s 。
#
#  每一次 操作 ，你可以选择 s 中两个 相邻 的字符，并将它们交换。
#
#  请你返回将 s 变成回文串的 最少操作次数 。
#
#  注意 ，输入数据会确保 s 一定能变成一个回文串。
#
#
#
#  示例 1：
#
#  输入：s = "aabb"
# 输出：2
# 解释：
# 我们可以将 s 变成 2 个回文串，"abba" 和 "baab" 。
# - 我们可以通过 2 次操作得到 "abba" ："aabb" -> "abab" -> "abba" 。
# - 我们可以通过 2 次操作得到 "baab" ："aabb" -> "abab" -> "baab" 。
# 因此，得到回文串的最少总操作次数为 2 。
#
#
#  示例 2：
#
#  输入：s = "letelt"
# 输出：2
# 解释：
# 通过 2 次操作从 s 能得到回文串 "lettel" 。
# 其中一种方法是："letelt" -> "letetl" -> "lettel" 。
# 其他回文串比方说 "tleelt" 也可以通过 2 次操作得到。
# 可以证明少于 2 次操作，无法得到回文串。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 2000
#  s 只包含小写英文字母。
#  s 可以通过有限次操作得到一个回文串。
#
#
#  Related Topics 贪心 树状数组 双指针 字符串
#  👍 33 👎 0
import collections


# 逆序对 获取排列[3,2,1]->[1,2,3]
# leetcode submit region begin(Prohibit modification and deletion)
class Ftree:
    def __init__(self, n):
        self.lst = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & (-x)

    def update(self, x, val):
        while x < len(self.lst):
            self.lst[x] += val
            x += self.lowbit(x)

    def query(self, x):
        ans = 0
        while x > 0:
            ans += self.lst[x]
            x -= self.lowbit(x)
        return ans


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        F = collections.Counter(s)
        lcnt, rcnt = 0, 0
        left, right = collections.defaultdict(list), collections.defaultdict(list)
        ans = 0
        for i, ch in enumerate(s):
            if len(left[ch]) + 1 <= F[ch] // 2:
                lcnt += 1
                left[ch].append(lcnt)
                ans += (i - lcnt + 1)
            else:
                rcnt += 1
                right[ch].append(rcnt)
        for ch in F:
            if F[ch] % 2 == 1:
                lcnt += 1
                left[ch].append(lcnt)
        perm = [0] * lcnt
        for ch in F:
            for x, y in zip(left[ch], right[ch][::-1]):  # 还原到真实位置 【1，2，3...】
                perm[y - 1] = x
        perm = perm[::-1]  # 逆序还原
        ft = Ftree(lcnt)
        for num in perm[::-1]:  # 求逆序对
            ans += ft.query(num - 1)
            ft.update(num, 1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
