'''

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        l1, l2 = len(num1), len(num2)
        ans = [0] * (l1 + l2)
        for i in range(l2 - 1, -1, -1):
            for j in range(l1 - 1, -1, -1):
                a = int(num1[j]) * int(num2[i])
                count = a // 10
                s = a % 10
                ans[l1 - i - 1 + l2 - j - 1] += s
                ans[l1 - i + l2 - j - 1] += count
        for i in range(len(ans)):
            if ans[i] >= 10:
                count = ans[i] // 10
                ans[i] = str(ans[i] % 10)
                ans[i + 1] += count
            else:
                ans[i] = str(ans[i])
        ans.reverse()

        res = ''.join(ans).lstrip('0')
        return res if len(res) > 0 else '0'


num1 = '999'
num2 = '999'
Solution().multiply(num1, num2)
