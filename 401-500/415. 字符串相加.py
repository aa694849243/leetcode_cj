'''给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

 

提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        if n1 > n2:
            num1, num2 = num2, num1
            n1,n2=n2,n1
        i = 0
        add = 0
        ans = ''
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i < n1:
            a = int(num1[i]) + int(num2[i]) + add
            x = a % 10
            add = a // 10
            ans += str(x)
            i += 1
        while i < n2:
            a = int(num2[i]) + add
            x = a % 10
            add = a // 10
            ans += str(x)
            i += 1
        if add > 0:
            ans += str(add)
        return ans[::-1]
Solution().addStrings("98","9")