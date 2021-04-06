'''
实现一个基本的计算器来计算一个简单的字符串表达式的值。

字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:

输入: "3+2*2"
输出: 7
示例 2:

输入: " 3/2 "
输出: 1
示例 3:

输入: " 3+5 / 2 "
输出: 5
说明：

你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def calculate(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        operator = '+-*/ '
        priority={'+':1,'-':1,'*':2,'/':2}
        st = []
        exp = []
        i, n = 0, len(s)
        while i < n:
            if s[i] not in operator:
                j = i+1
                while j < n and s[j] not in operator:
                    j += 1
                exp.append(int(s[i:j]))
                i = j
                continue
            if s[i] == ' ':
                i += 1
                continue
            if s[i] in operator:
                while st and priority[st[-1]] >=priority[s[i]]:
                    exp.append(st.pop())
                st.append(s[i])
            i += 1
        while st:
            exp.append(st.pop())
        for i in exp:
            if type(i) is int:
                st.append(i)
            else:
                a=st.pop()
                b=st.pop()
                if i=='+':
                    st.append(a+b)
                elif i=='-':
                    st.append(b-a)
                elif i=='*':
                    st.append(a*b)
                else:
                    st.append(int(b/a))
        return st[0]


a='3-9*8/64'
Solution().calculate(a)
