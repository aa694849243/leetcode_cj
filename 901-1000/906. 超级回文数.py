# 如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。
#
#  现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目。
#
#
#
#  示例：
#
#  输入：L = "4", R = "1000"
# 输出：4
# 解释：
# 4，9，121，以及 484 是超级回文数。
# 注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。
#
#
#
#  提示：
#
#
#  1 <= len(L) <= 18
#  1 <= len(R) <= 18
#  L 和 R 是表示 [1, 10^18) 范围的整数的字符串。
#  int(L) <= int(R)
#
#
#
#  Related Topics 数学
#  👍 26 👎 0


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        L = len(left)
        R = len(right)
        l = L // 2 + 1
        r = min(R // 2 + 1, 9)
        odd, even = 0, 0
        s = max(l // 2, 1)
        e = r // 2 + 1

        def isPalindrome(s):
            return s == s[::-1]

        def ge(x, y):
            if len(x) > len(y):
                return True
            elif len(x) == len(y):
                return x >= y
            else:
                return False

        for x in range(10 ** (s - 1), 10 ** e - 1):
            a = str(x)
            a_a = a + a[:-1][::-1]  # odd型
            aa = a + a[::-1]  # even型
            a_a2 = str(int(a_a) ** 2)
            aa2 = str(int(aa) ** 2)
            if ge(a_a2, left) and ge(right, a_a2):
                if isPalindrome(a_a2):
                    odd += 1
            if ge(aa2, left) and ge(right, aa2):
                if isPalindrome(aa2):
                    even += 1
        return odd + even


Solution().superpalindromesInRange("111", "231")
