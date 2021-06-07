# -*- coding: utf-8 -*-


# 如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。
#
#  花括号展开的表达式可以看作一个由 花括号、逗号 和 小写英文字母 组成的字符串，定义下面几条语法规则：
#
#
#  如果只给出单一的元素 x，那么表达式表示的字符串就只有 "x"。R(x) = {x}
#
#
#  例如，表达式 {"a"} 表示字符串 "a"。
#  而表达式 {"w"} 就表示字符串 "w"。
#
#
#  当两个或多个表达式并列，以逗号分隔时，我们取这些表达式中元素的并集。R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
#
#  例如，表达式 "{a,b,c}" 表示字符串 "a","b","c"。
#  而表达式 "{{a,b},{b,c}}" 也可以表示字符串 "a","b","c"。
#
#
#  要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。R(e_1 + e_2) = {a + b for (a, b
# ) in R(e_1) × R(e_2)}
#
#  例如，表达式 "{a,b}{c,d}" 表示字符串 "ac","ad","bc","bd"。
#
#
#  表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
#
#  例如，表达式 "a{b,c,d}" 表示字符串 "ab","ac","ad"。
#  例如，表达式 "a{b,c}{d,e}f{g,h}" 可以表示字符串 "abdfg", "abdfh", "abefg", "abefh", "acdfg
# ", "acdfh", "acefg", "acefh"。
#
#
#
#
#  给出表示基于给定语法规则的表达式 expression，返回它所表示的所有字符串组成的有序列表。
#
#  假如你希望以「集合」的概念了解此题，也可以通过点击 “显示英文描述” 获取详情。
#
#
#
#  示例 1：
#
#
# 输入："{a,b}{c,{d,e}}"
# 输出：["ac","ad","ae","bc","bd","be"]
#
#  示例 2：
#
#
# 输入："{{a,z},a{b,c},{ab,z}}"
# 输出：["a","ab","ac","z"]
# 解释：输出中 不应 出现重复的组合结果。
#
#
#
#
#  提示：
#
#
#  1 <= expression.length <= 50
#  expression[i] 由 '{'，'}'，',' 或小写英文字母组成
#  给出的表达式 expression 用以表示一组基于题目描述中语法构造的字符串
#
#  Related Topics 字符串
#  👍 43 👎 0
import itertools
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


word = r'(?P<WORD>[a-z]+)'
comma = r'(?P<COMMA>\,)'
left = r'(?P<LEFT>\{)'
right = r'(?P<RIGHT>\})'
blank = r'(?P<BLANK>\s)'
token = namedtuple('token', ('type', 'val'))
pt = re.compile('|'.join([left, right, comma, blank, word]))


def genToken(s):
    sc = pt.scanner(s)
    for i in iter(sc.match, None):
        if i.lastgroup != 'BLANK':
            yield token(i.lastgroup, i.group(0))


class parser:
    def match(self, tp):
        if self.p.type == tp:
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
        return list(sorted(st))

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
            for i, j in itertools.product(list(ret), list(sufs)):
                new.add(i + j)
            ret = new
        return ret

    def factor(self):
        if self.p.type == 'LEFT':
            self.match('LEFT')
            ret = self.expr()
            self.match('RIGHT')
            return ret
        return {self.match('WORD')}


class Solution:
    def braceExpansionII(self, expression):
        return parser().parse(expression)


Solution().braceExpansionII("{a,b}{c,{d,e}}")
