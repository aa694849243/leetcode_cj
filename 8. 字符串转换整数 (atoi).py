"""
请你来实现一个 atoi 函数，使其能将字符串转换成整数。

首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：

如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。
假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。
该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。
注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。

在任何情况下，若函数不能进行有效的转换时，请返回 0 。

提示：

本题中的空白字符只包括空格字符 ' ' 。
假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

来源：力扣（LeetCodedef myAtoi(self, str: str) -> int:）
链接：https://leetcode-cn.com/problems/string-to-integer-atoi
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# -----------------------------------------caojie----96.29%--------------------------------------------------------------
def myAtoi(str: str) -> int:
    s = str.lstrip()
    flag = 1
    sum = 0
    i = 0
    if len(s) < 1: return 0
    if not s[0].isdigit() and s[0] not in ('-', '+'):
        return 0
    if s[0] in ('-', "+"):
        if s[0] == '-':
            flag = -1
        s = s[1:]
    for i in range(len(s)):
        if s[i].isdigit():
            sum *= 10
            sum += int(s[i])
        else:
            break
    if flag < 0:
        s = sum * flag if -2 ** 31 <= sum * flag else -2 ** 31
    else:
        s = sum * flag if 2 ** 31 > sum * flag else 2 ** 31 - 1
    return s


# --------------------正则表达式-----1行代码--------------------------------------------------------------------
def myAtoi(s: str) -> int:
    return max(min(int(*re.findall('^[\+\-]?\d', s.lstrip()), -2 ** 31), 2 ** 31 - 1))


# -----------------------有限状态自动机（deterministic finite automaton, DFA）-官方-----------------------------------
class Automaton:
    def __init__(self):
        self.state = 'start'  # 开始状态
        self.ans = 0  # 开始计数
        self.flag = 1  # 标记正负号
        self.table = {'start': ['start', 'sign', 'in_number', 'end'],
                      'sign': ['end', 'end', 'in_number', 'end'],
                      'in_number': ['end', 'end', 'in_number', 'end'],
                      'end': ['end', 'end', 'end', 'end']}  # 构建状态转移表

    def get_state(self, c):
        if c == ' ':
            return 0
        elif c in ('+', '-'):
            return 1
        elif c.isdigit():
            return 2
        else:
            return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_state(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(max(self.ans, -2 ** 31), 2 ** 31 - 1)
        if self.state == 'sign':
            self.flag = 1 if c == '+' else -1
            # 不用定义end状态


def myAtoi(self, str: str) -> int:
    auto = Automaton()
    for c in str:
        auto.get(c)
    return auto.sign*auto.ans


def add_(n):
    s = Automaton()
    for i in range(n):
        s.get(i)
    return s.state


add_(10)
import string

str = '  -42'
myAtoi(str)
import re

''
