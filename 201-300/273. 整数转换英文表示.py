# 将非负整数 num 转换为其对应的英文表示。
#
#
#
#  示例 1：
#
#
# 输入：num = 123
# 输出："One Hundred Twenty Three"
#
#
#  示例 2：
#
#
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"
#
#
#  示例 3：
#
#
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#
#
#
#  提示：
#
#
#  0 <= num <= 2³¹ - 1
#
#
#  Related Topics 递归 数学 字符串
#  👍 320 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numberToWords(self, num: int) -> str:
        m = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
             8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
             14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen',
             19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
             70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

        def basic(num):
            if num <= 20:
                return m[num] + ' '
            elif num < 100:
                s = m[num // 10 * 10] + ' ' + m[num % 10]
                return s + ' ' if s[-1] != ' ' else s
            else:
                if num % 100 <= 20:
                    s = m[num // 100] + ' Hundred ' + m[num % 100]
                    return s + ' ' if s[-1] != ' ' else s
                else:
                    s = m[num // 100] + ' Hundred ' + m[num % 100 // 10 * 10] + ' ' + m[num % 10]
                    return s + ' ' if s[-1] != ' ' else s

        if num == 0:
            return 'Zero'

        billion = num // 10 ** 9
        billion_str = basic(billion) + 'Billion ' if billion else ''
        num = num % 10 ** 9
        million = num // 10 ** 6
        million_str = basic(million) + 'Million ' if million else ''
        num = num % 10 ** 6
        thousand = num // 10 ** 3
        thousand_str = basic(thousand) + 'Thousand ' if thousand else ''
        num = num % 10 ** 3
        resi_str = basic(num) if num else ''
        res = billion_str + million_str + thousand_str + resi_str
        return res[:-1] if res[-1] == ' ' else res


# leetcode submit region end(Prohibit modification and deletion)
print(Solution().numberToWords(1234567891))
