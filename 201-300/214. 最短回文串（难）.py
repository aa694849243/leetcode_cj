# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
#
#
#
#  示例 1：
#
#
# 输入：s = "aacecaaa"
# 输出："aaacecaaa"
#
#
#  示例 2：
#
#
# 输入：s = "abcd"
# 输出："dcbabcd"
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 5 * 10⁴
#  s 仅由小写英文字母组成
#
#
#  Related Topics 字符串 字符串匹配 哈希函数 滚动哈希
#  👍 539 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def gen_pnext(s):
            n = len(s)
            pnext = [-1] * n
            k = -1
            i = 0
            while i < n - 1:
                if k == -1 or s[i] == s[k]:
                    i += 1
                    k += 1
                    pnext[i] = k  # i之前的最长公共前后缀长度
                else:
                    k = pnext[k]
            return pnext

        tmp_s = s + '#' + s[::-1] + '$'
        pnext = gen_pnext(tmp_s)
        length = pnext[-1]
        return s[length:][::-1] + s
# leetcode submit region end(Prohibit modification and deletion)
