# 我们有一些二维坐标，如 "(1, 3)" 或 "(2, 0.5)"，然后我们移除所有逗号，小数点和空格，得到一个字符串S。返回所有可能的原始字符串到一个列表
# 中。
#
#  原始的坐标表示法不会存在多余的零，所以不会出现类似于"00", "0.0", "0.00", "1.0", "001", "00.01"或一些其他更小的数
# 来表示坐标。此外，一个小数点前至少存在一个数，所以也不会出现“.1”形式的数字。
#
#  最后返回的列表可以是任意顺序的。而且注意返回的两个数字中间（逗号之后）都有一个空格。
#
#
#
#
# 示例 1:
# 输入: "(123)"
# 输出: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
#
#
#
# 示例 2:
# 输入: "(00011)"
# 输出:  ["(0.001, 1)", "(0, 0.011)"]
# 解释:
# 0.0, 00, 0001 或 00.01 是不被允许的。
#
#
#
# 示例 3:
# 输入: "(0123)"
# 输出: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12,
# 3)"]
#
#
#
# 示例 4:
# 输入: "(100)"
# 输出: [(10, 0)]
# 解释:
# 1.0 是不被允许的。
#
#
#
#
#  提示:
#
#
#  4 <= S.length <= 12.
#  S[0] = "(", S[S.length - 1] = ")", 且字符串 S 中的其他元素都是数字。
#
#
#
#  Related Topics 字符串
#  👍 29 👎 0

from typing import List


class Solution:
    def ambiguousCoordinates(self, S: str) -> List[str]:
        s = S[1:-1]
        res = []

        def judge(s):
            if len(s) >= 2:
                if s[0] == s[1] == '0':
                    return False
                if s[0] == '0' and s[1] != '.':
                    return False
                if float(s) == 0 and s[:2] == '0.':
                    return False
                if '.' in s and s[-1] == '0':
                    return False
            return True

        def cal(a, b):
            li = []
            lia = []
            lib = []
            if judge(a):
                lia.append(a)
            if judge(b):
                lib.append(b)
            for i in range(1, len(a)):
                x = a[:i] + '.' + a[i:]
                if judge(x):
                    lia.append(x)
            for i in range(1, len(b)):
                x = b[:i] + '.' + b[i:]
                if judge(x):
                    lib.append(x)
            for x in lia:
                for y in lib:
                    li.append((x, y))
            return li

        for i in range(1, len(s)):
            a = s[:i]
            b = s[i:]
            res.extend(cal(a, b))
        ans = []
        for a, b in res:
            x = '(' + a + ', ' + b + ')'
            ans.append(x)
        return ans


Solution().ambiguousCoordinates("(100)")
