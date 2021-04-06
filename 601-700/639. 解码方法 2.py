'''
一条包含字母 A-Z 的消息通过以下的方式进行了编码：

'A' -> 1
'B' -> 2
...
'Z' -> 26
除了上述的条件以外，现在加密字符串可以包含字符 '*'了，字符'*'可以被当做1到9当中的任意一个数字。

给定一条包含数字和字符'*'的加密信息，请确定解码方法的总数。

同时，由于结果值可能会相当的大，所以你应当对109 + 7取模。（翻译者标注：此处取模主要是为了防止溢出）

示例 1 :

输入: "*"
输出: 9
解释: 加密的信息可以被解密为: "A", "B", "C", "D", "E", "F", "G", "H", "I".
示例 2 :

输入: "1*"
输出: 9 + 9 = 18（翻译者标注：这里1*可以分解为1,* 或者当做1*来处理，所以结果是9+9=18）
说明 :

输入的字符串长度范围是 [1, 105]。
输入的字符串只会包含字符 '*' 和 数字'0' - '9'。'''


# 1递归
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        m = {}

        def rec(s):
            if not s:
                return 1
            if s in m:
                return m[s]
            if s[-1] == '*':
                if len(s) == 1:
                    return 9
                else:
                    if s[-2] == '1':
                        a = 9 * rec(s[:-1]) + 9 * rec(s[:-2])
                    elif s[-2] == '2':
                        a = 9 * rec(s[:-1]) + 6 * rec(s[:-2])
                    elif s[-2] == '*':
                        a = 9 * rec(s[:-1]) + 15 * rec(s[:-2])
                    else:
                        a = 9 * rec(s[:-1])
            elif int(s[-1]) > 6:
                if len(s) == 1:
                    return 1
                if s[-2] == '*' or s[-2] == '1':
                    a = rec(s[:-1]) + rec(s[:-2])
                else:
                    a = rec(s[:-1])
            elif 0 < int(s[-1]) <= 6:
                if len(s) == 1:
                    return 1
                if s[-2] == '*':
                    a = rec(s[:-1]) + 2 * rec(s[:-2])
                elif s[-2] == '1' or s[-2] == '2':
                    a = rec(s[:-1]) + rec(s[:-2])
                else:
                    a = rec(s[:-1])
            elif s[-1] == '0':
                if s[-2] == '1' or s[-2] == '2':
                    a = rec(s[:-2])
                elif s[-2] == '*':
                    a = 2 * rec(s[:-2])
                else:
                    return 0

            a %= (10 ** 9 + 7)
            m[s] = a
            return a

        return rec(s)


# 2dp和动态规划
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp1 = 9 if s[0] == '*' else 1
        if len(s) == 1:
            return dp1
        dp2 = 1
        for i in range(1, len(s)):
            tmp = dp1
            if s[i] == '*':
                if s[i - 1] == '1':
                    dp1 = 9 * dp1 + 9 * dp2
                elif s[i - 1] == '2':
                    dp1 = 9 * dp1 + 6 * dp2
                elif s[i - 1] == '*':
                    dp1 = 9 * dp1 + 15 * dp2
                else:
                    dp1 = 9 * dp1
            elif int(s[i]) > 6:
                if s[i - 1] == '*' or s[i - 1] == '1':
                    dp1 = dp1 + dp2
                else:
                    dp1 = dp1
            elif 0 < int(s[i]) <= 6:
                if s[i - 1] == '*':
                    dp1 = dp1 + 2 * dp2
                elif s[i - 1] == '1' or s[i - 1] == '2':
                    dp1 = dp1 + dp2
            elif s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp1 = dp2
                elif s[i-1] == '*':
                    dp1 = 2 * dp2
                else:
                    return 0
            dp1%=(10**9+7)
            dp2 = tmp
        return dp1


Solution().numDecodings("5*5*")
