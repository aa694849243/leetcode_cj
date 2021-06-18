'''
验证给定的字符串是否可以解释为十进制数字。

例如:

"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

说明: 我们有意将问题陈述地比较模糊。在实现代码之前，你应当事先思考所有可能的情况。这里给出一份可能存在于有效十进制数字中的字符列表：

数字 0-9
指数 - "e"
正/负号 - "+"/"-"
小数点 - "."
当然，在输入中，这些字符的上下文也很重要。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isNumber(self, s: str) -> bool:
        state = [
            {},
            # 状态1,初始状态(扫描通过的空格)
            {"blank": 1, "sign": 2, "digit": 3, ".": 4},
            # 状态2,发现符号位(后面跟数字或者小数点)
            {"digit": 3, ".": 4},
            # 状态3,数字(一直循环到非数字)
            {"digit": 3, ".": 5, "e": 6, "blank": 9},
            # 状态4,小数点(后面只有紧接数字)
            {"digit": 5},
            # 状态5,小数点之后(后面只能为数字,e,或者以空格结束)
            {"digit": 5, "e": 6, "blank": 9},
            # 状态6,发现e(后面只能符号位, 和数字)
            {"sign": 7, "digit": 8},
            # 状态7,e之后(只能为数字)
            {"digit": 8},
            # 状态8,e之后的数字后面(只能为数字或者以空格结束)
            {"digit": 8, "blank": 9},
            # 状态9, 终止状态 (如果发现非空,就失败)
            {"blank": 9}
        ]
        cur_state = 1
        for c in s:
            if c.isdigit():
                c = "digit"
            elif c in " ":
                c = "blank"
            elif c in "+-":
                c = "sign"
            elif c in 'eE':
                c = 'e'
            if c not in state[cur_state]:
                return False
            cur_state = state[cur_state][c]
        if cur_state not in [3, 5, 8, 9]:
            return False
        return True


Solution().isNumber("1E9")


class Solution:
    def __init__(self):
        self.transfer = [[0, 1, 6, 2, -1, -1],
                         [-1, -1, 6, 2, -1, -1],
                         [-1, -1, 3, -1, -1, -1],
                         [8, -1, 3, -1, 4, -1],
                         [-1, 7, 5, -1, -1, -1],
                         [8, -1, 5, -1, -1, -1],
                         [8, -1, 6, 3, 4, -1],
                         [-1, -1, 5, -1, -1, -1],
                         [8, -1, -1, -1, -1, -1]]
        self.state = 0

    def enter(self, c):
        if c == ' ':
            return 0
        elif c in ('+', '-'):
            return 1
        elif c.isdigit():
            return 2
        elif c == '.':
            return 3
        elif c == 'e':
            return 4
        else:
            return 5

    def get_state(self, c):
        self.state = self.transfer[self.state][self.enter(c)]

    def isNumber(self, s: str) -> bool:
        for i in s:
            self.get_state(i)
            if self.state == -1:
                return False
        return True if self.state in (6, 8, 5, 3) else False


Solution().isNumber('.. ')
