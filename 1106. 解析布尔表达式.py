# -*- coding: utf-8 -*-


# 给你一个以字符串形式表述的 布尔表达式（boolean） expression，返回该式的运算结果。
#
#  有效的表达式需遵循以下约定：
#
#
#  "t"，运算结果为 True
#  "f"，运算结果为 False
#  "!(expr)"，运算过程为对内部表达式 expr 进行逻辑 非的运算（NOT）
#  "&(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 与的运算（AND）
#  "|(expr1,expr2,...)"，运算过程为对 2 个或以上内部表达式 expr1, expr2, ... 进行逻辑 或的运算（OR）
#
#
#
#
#  示例 1：
#
#  输入：expression = "!(f)"
# 输出：true
#
#
#  示例 2：
#
#  输入：expression = "|(f,t)"
# 输出：true
#
#
#  示例 3：
#
#  输入：expression = "&(t,f)"
# 输出：false
#
#
#  示例 4：
#
#  输入：expression = "|(&(t,f,t),!(t))"
# 输出：false
#
#
#
#
#  提示：
#
#
#  1 <= expression.length <= 20000
#  expression[i] 由 {'(', ')', '&', '|', '!', 't', 'f', ','} 中的字符组成。
#  expression 是以上述形式给出的有效表达式，表示一个布尔值。
#
#  Related Topics 字符串
#  👍 48 👎 0

import re
from collections import namedtuple

# https://leetcode-cn.com/problems/brace-expansion-ii/solution/pythondi-gui-xia-jiang-yu-fa-fen-xi-yi-chong-fan-2/

token = namedtuple('token', ['type', 'value'])

left = r'(?P<LEFT>\{)'
right = r'(?P<RIGHT>\})'
word = r'(?P<WORD>[a-z]+)'
comma = r'(?P<COMMA>\,)'
blank = r'(?P<BLANK>\s)'
pt = re.compile('|'.join([left, right, word, comma, blank]))


def genToken(s):
    scanner = pt.scanner(s)
    for i in iter(scanner.match, None):
        if i.lastgroup != 'BLANK':
            yield token(i.lastgroup, i.group(0))


class parser:
    '''gramar
        expr -> item | item ',' expr
        item -> factor | factor item
        factor -> WORD | '{' expr '}'
    '''

    def match(self, tp):
        # print(self.p.value)
        if tp == self.p.type:
            val = self.p.value
            try:
                self.p = next(self.gen)
            except StopIteration:
                self.p = None
            except Exception as e:
                print(e)
            return val
        else:
            raise Exception(f"[Error]: {tp} expected, got {self.p.type}")

    def parse(self, s):
        self.gen = genToken(s)
        self.p = next(self.gen)
        st = self.expr()
        return sorted(list(st))

    def expr(self):
        ret = self.item()
        while self.p and self.p.type == 'COMMA':
            self.match('COMMA')
            ret = ret.union(self.item())
        return ret

    def item(self):
        ret = self.factor()
        while self.p and self.p.type in ['WORD', 'LEFT']:
            sufs = self.factor()
            new = set()
            for pre in ret:
                for suf in sufs:
                    new.add(pre + suf)
            ret = new
        return ret

    def factor(self):
        if self.p.type == 'LEFT':
            self.match('LEFT')
            ret = self.expr()
            self.match('RIGHT')
            return ret
        return {self.match('WORD')}


t = r'(?P<TRUE>t)'
f = r'(?P<FALSE>f)'
and_ = r'(?P<AND>\&)'
neg = r'(?P<NEG>\!)'
or_ = r'(?P<OR>\|)'
comma = r'(?P<COMMA>\,)'
left = r'(?P<LEFT>\()'
right = r'(?P<RIGHT>\))'
blank = r'(?P<BLANK>\s+)'

token = namedtuple('token', ('type', 'val'))
pt = re.compile('|'.join([left, right, t, f, and_, or_, neg, comma, blank]))


def genToken(s):
    sc = pt.scanner(s)
    for i in iter(sc.match, None):
        if i.lastgroup != 'BLANK':
            yield token(i.lastgroup, i.group(0))


class parser:
    def match(self, tp=None):
        if not tp or self.p.type == tp:
            val = self.p.val
            try:
                self.p = next(self.gen)  # 更新指针
            except StopIteration:
                self.p = None
            except Exception as e:
                print(e)
            return val
        else:
            raise Exception(f'[Error]: {tp} except, get {self.p.type} get')

    def parse(self, s):
        self.gen = genToken(s)
        self.p = next(self.gen)
        st = self.expr()
        return st.pop()

    def expr(self):
        ret = self.term()
        while self.p and self.p.type == 'COMMA':
            self.match('COMMA')
            a=self.term()
            ret = ret.union(a)
        return ret

    def term(self):
        op = self.item().pop()
        ans = op
        if self.p and self.p.type == 'LEFT':
            it = self.item()
            if op == '!':
                ans = not it.pop()
            elif op == '&':
                ans = all(x for x in it)
            elif op == '|':
                ans = any(x for x in it)
            else:
                raise Exception('invalid input')
        return {ans}

    def item(self):
        if self.p.type == 'LEFT':
            self.match('LEFT')
            ret = self.expr()
            self.match('RIGHT')
            return ret
        elif self.p.type == 'FALSE':
            self.match('FALSE')
            return {False}
        elif self.p.type == 'TRUE':
            self.match('TRUE')
            return {True}
        elif self.p.type == 'AND':
            self.match('AND')
            return {'&'}
        elif self.p.type == 'OR':
            self.match('OR')
            return {'|'}
        elif self.p.type == 'NEG':
            self.match('NEG')
            return {'!'}


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        return parser().parse(expression)


Solution().parseBoolExpr("|(&(t,f,t),!(t))")
