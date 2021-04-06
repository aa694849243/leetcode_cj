'''
将非负整数转换为其对应的英文表示。可以保证给定输入小于 231 - 1 。

示例 1:

输入: 123
输出: "One Hundred Twenty Three"
示例 2:

输入: 12345
输出: "Twelve Thousand Three Hundred Forty Five"
示例 3:

输入: 1234567
输出: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
示例 4:

输入: 1234567891
输出: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-english-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 分治法
class Solution:
    def numberToWords(self, num: int) -> str:
        def one(nums):
            a = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
            return a[nums] if nums > 0 else ''

        def lt_20(nums):
            a = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen',
                 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
            return a[nums]

        def gt_20(nums):
            a = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty',
                 9: 'Ninety'}
            rest = nums - (nums // 10) * 10
            return a[nums // 10] + ' ' + one(rest) if rest > 0 else a[nums // 10]

        def hd(nums):
            a = nums // 100
            if nums - a * 100 >= 20:
                return one(a) + ' Hundred' + ' ' + gt_20(nums - a * 100)
            if 9 < nums - a * 100 < 20:
                return one(a) + ' Hundred' + ' ' + lt_20(nums - a * 100)
            if 0 < nums - a * 100:
                return one(a) + ' Hundred' + ' ' + one(nums - a * 100)
            if nums - a * 100 == 0:
                return one(a) + ' Hundred'

        if not num:
            return 'Zero'
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        ans = ''
        if billion > 0:
            ans = ans + one(billion) + ' Billion'
        if million > 0:
            if million >= 100:
                ans = ans + ' ' + hd(million) + ' Million'
            elif 20 <= million:
                ans = ans + ' ' + gt_20(million) + ' Million'
            elif 9 < million:
                ans = ans + ' ' + lt_20(million) + ' Million'
            else:
                ans = ans + ' ' + one(million) + ' Million'
        if thousand > 0:
            if thousand >= 100:
                ans = ans + ' ' + hd(thousand) + ' Thousand'
            elif 20 <= thousand:
                ans = ans + ' ' + gt_20(thousand) + ' Thousand'
            elif 9 < thousand:
                ans = ans + ' ' + lt_20(thousand) + ' Thousand'
            else:
                ans = ans + ' ' + one(thousand) + ' Thousand'
        if rest > 0:
            if rest >= 100:
                ans = ans + ' ' + hd(rest)
            elif rest >= 20:
                ans = ans + ' ' + gt_20(rest)
            elif rest > 9:
                ans = ans + ' ' + lt_20(rest)
            else:
                ans = ans + ' ' + one(rest)
        return ans.lstrip()


Solution().numberToWords(100000000)
