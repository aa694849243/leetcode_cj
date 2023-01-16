# -*- coding: utf-8 -*-
# 给你一个仅由小写英文字母组成的字符串 s 。在一步操作中，你可以：
#
#
#  删除 整个字符串 s ，或者
#  对于满足 1 <= i <= s.length / 2 的任意 i ，如果 s 中的 前 i 个字母和接下来的 i 个字母 相等 ，删除 前 i 个字母。
#
#
#
#  例如，如果 s = "ababc" ，那么在一步操作中，你可以删除 s 的前两个字母得到 "abc" ，因为 s 的前两个字母和接下来的两个字母都等于
# "ab" 。
#
#  返回删除 s 所需的最大操作数。
#
#
#
#  示例 1：
#
#
# 输入：s = "abcabcdabc"
# 输出：2
# 解释：
# - 删除前 3 个字母（"abc"），因为它们和接下来 3 个字母相等。现在，s = "abcdabc"。
# - 删除全部字母。
# 一共用了 2 步操作，所以返回 2 。可以证明 2 是所需的最大操作数。
# 注意，在第二步操作中无法再次删除 "abc" ，因为 "abc" 的下一次出现并不是位于接下来的 3 个字母。
#
#
#  示例 2：
#
#
# 输入：s = "aaabaab"
# 输出：4
# 解释：
# - 删除第一个字母（"a"），因为它和接下来的字母相等。现在，s = "aabaab"。
# - 删除前 3 个字母（"aab"），因为它们和接下来 3 个字母相等。现在，s = "aab"。
# - 删除第一个字母（"a"），因为它和接下来的字母相等。现在，s = "ab"。
# - 删除全部字母。
# 一共用了 4 步操作，所以返回 4 。可以证明 4 是所需的最大操作数。
#
#
#  示例 3：
#
#
# 输入：s = "aaaaa"
# 输出：5
# 解释：在每一步操作中，都可以仅删除 s 的第一个字母。
#
#
#
#
#  提示：
#
#
#  1 <= s.length <= 4000
#  s 仅由小写英文字母组成
#
#
#  Related Topics 字符串 动态规划 字符串匹配 哈希函数 滚动哈希
#  👍 34 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 线性dp
class Solution:
    def deleteString(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1:# 特判全部相同的情况，要不然超时
            return n
        lcp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):  # 预处理s[i:]和s[j:]的最长公共前缀长度
            for j in range(n - 1, i, -1):
                if s[i] == s[j]:
                    lcp[i][j] = lcp[i + 1][j + 1] + 1
        f = [0] * n
        for i in range(n - 1, -1, -1):
            for length in range(1, (n - i) // 2 + 1):
                if lcp[i][i + length] >= length:  # s[i:i+length]可以删
                    f[i] = max(f[i], f[i + length])
            f[i] += 1
        return f[0]

# leetcode submit region end(Prohibit modification and deletion)
