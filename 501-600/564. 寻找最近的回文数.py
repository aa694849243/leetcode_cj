# 给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。
#
#  “最近的”定义为两个整数差的绝对值最小。
#
#
#
#  示例 1:
#
#
# 输入: n = "123"
# 输出: "121"
#
#
#  示例 2:
#
#
# 输入: n = "1"
# 输出: "0"
# 解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。
#
#
#
#
#  提示:
#
#
#  1 <= n.length <= 18
#  n 只由数字组成
#  n 不含前导 0
#  n 代表在 [1, 10¹⁸ - 1] 范围内的整数
#
#
#  Related Topics 数学 字符串
#  👍 278 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n=='1':
            return '0'
        def mirror(s):
            n = len(s)
            if n % 2:
                return int(s[:n // 2 + 1] + s[:n // 2][::-1])
            else:
                return int(s[:n // 2] + s[:n // 2][::-1])

        def gt_s(s):
            n = len(s)
            if n % 2:
                half = s[:n // 2 + 1]
                if half == '9' * (n // 2 + 1):  # 进位了
                    return int('1' + '0' * (n - 1) + '1')
                else:
                    half = str(int(half) + 1)
                    return int(half + half[:-1][::-1])
            else:
                half = s[:n // 2]
                if half == '9' * (n // 2):  # 进位了
                    return int('1' + '0' * (n - 1) + '1')
                else:
                    half = str(int(half) + 1)
                    return int(half + half[::-1])

        def lt_s(s):
            n = len(s)
            if n % 2:
                half = s[:n // 2 + 1]
                if half == '1' + '0' * (n // 2):  # 位数减少
                    return int('9' * (n - 1))
                else:
                    half = str(int(half) - 1)
                    return int(half + half[:-1][::-1])
            else:
                half = s[:n // 2]
                if half == '1' + '0' * (n // 2 - 1):  # 位数减少
                    return int('9' * (n - 1))
                else:
                    half = str(int(half) - 1)
                    return int(half + half[::-1])

        diff_a = abs(int(n) - (a := mirror(n)))
        diff_b = abs(int(n) - (b := gt_s(n)))
        diff_c = abs(int(n) - (c := lt_s(n)))
        diff_a = diff_a if diff_a else float('inf')
        diff_b = diff_b if diff_b else float('inf')
        diff_c = diff_c if diff_c else float('inf')
        return str(sorted([(diff_a,a),(diff_b,b),(diff_c,c)])[0][1])

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().nearestPalindromic('2'))
