
# 有限状态自动机
class Solution:
    def isNumber(self, s: str) -> bool:
        m = {
            'start': {'signed': 'first_signed', 'digit': 'first_digit', 'dot': 'space_dot'},
            'space_dot': {'digit': 'second_digit'},
            'first_signed': {'digit': 'first_digit', 'dot': 'space_dot'},
            'first_digit': {'digit': 'first_digit', 'dot': 'dot', 'e': 'e'},
            'dot': {'digit': 'second_digit', 'e': 'e'},
            'e': {'signed': 'e_signed', 'digit': 'e_digit'},
            'second_digit': {'digit': 'second_digit', 'e': 'e'},
            'e_digit': {'digit': 'e_digit'},
            'e_signed': {'digit': 'e_digit'},
        }
        end = {'first_digit', 'second_digit', 'e_digit', 'dot'}
        alls = set()
        status = 'start'
        for ch in s:
            if ch in '+-':
                nxt = 'signed'
            elif ch in '0123456789':
                nxt = 'digit'
            elif ch == '.':
                nxt = 'dot'
            elif ch in 'eE':
                nxt = 'e'
            else:
                return False
            if nxt not in m[status]:
                return False
            status = m[status][nxt]
            alls.add(status)
        if status not in end:
            return False
        # if status == 'dot' and alls != {'first_digit', 'dot'}:
        #     return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
print(Solution().isNumber('-1.'))


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
