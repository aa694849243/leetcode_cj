'''给定一个表达式 expression 如 expression = "e + 8 - a + 5" 和一个求值映射，如 {"e": 1}（给定的形式为 evalvars = ["e"] 和 evalints = [1]），返回表示简化表达式的标记列表，例如 ["-1*a","14"]

表达式交替使用块和符号，每个块和符号之间有一个空格。
块要么是括号中的表达式，要么是变量，要么是非负整数。
块是括号中的表达式，变量或非负整数。
变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 "2x" 或 "-x" 这样的前导系数或一元运算符 。
表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。例如，expression = "1 + 2 * 3" 的答案是 ["7"]。

输出格式如下：

对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。例如，我们永远不会写像 “b*a*c” 这样的项，只写 “a*b*c”。
项的次数等于被乘的自变量的数目，并计算重复项。(例如，"a*a*b*c" 的次数为 4。)。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。
项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。
格式良好的一个示例答案是 ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"] 。
系数为 0 的项（包括常数项）不包括在内。例如，“0” 的表达式输出为 []。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import collections


# 表达式解析类问题
class Poly(collections.Counter):
    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.update({k: -v for k, v in other.items()})
        return self

    def __mul__(self, other):
        a = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                a.update({tuple(sorted(k1 + k2)): v1 * v2})
        return a

    def evaluate(self, evalmap):
        a = Poly()
        for k, v in self.items():
            free = []
            for token in k:
                if token in evalmap:
                    v *= evalmap[token]
                else:
                    free.append(token)
            a[tuple(free)] += v
        return a

    def to_list(self):
        return ['*'.join((str(v),) + k) for k, v in sorted(self.items(), key=lambda x: (-len(x[0]), x[0], x[1])) if v]


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = dict(zip(evalvars, evalints))

        def combine(left, right, symbol):
            if symbol == '*':
                return left * right
            elif symbol == '-':
                return left - right
            elif symbol == '+':
                return left + right
            raise

        def make(exp):
            a = Poly()
            if exp.isdigit():
                a.update({(): int(exp)})
                return a
            else:
                a.update({(exp,): 1})
            return a

        def parse(exp):
            bucket = []
            symbols = []
            i = 0
            while i < len(exp):
                if exp[i] == '(':
                    bal = 1
                    for j in range(i + 1, len(exp)):
                        if exp[j] == '(':
                            bal += 1
                        elif exp[j] == ')':
                            bal -= 1
                        if bal == 0:
                            bucket.append(parse(exp[i + 1:j]))
                            break
                    i = j
                elif exp[i].isalnum():
                    for j in range(i, len(exp)):
                        if exp[j] == ' ':
                            bucket.append(make(exp[i:j]))
                            break
                    else:
                        bucket.append(make(exp[i:]))
                    i = j
                elif exp[i] in '*+-':
                    symbols.append(exp[i])
                i += 1
            for i in range(len(symbols) - 1, -1, -1):
                if symbols[i] == '*':
                    bucket[i] = combine(bucket[i], bucket.pop(i + 1), symbols.pop(i))
            if not bucket: return Poly()
            ans = bucket[0]
            for i, symbol in enumerate(symbols, 1):
                ans = combine(ans, bucket[i], symbol)
            return ans

        P = parse(expression).evaluate(evalmap)
        return P.to_list()


# 徒手写
class Poly(collections.Counter):
    def __add__(self, other):
        self.update(other)
        return self

    def __sub__(self, other):
        self.update({tuple(k): -v for k, v in other.items()})
        return self

    def __mul__(self, other):
        a = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                a[tuple(sorted(k1 + k2))] += v1 * v2
        return a

    def evaluate(self, evalmap):
        a = Poly()
        for k, v in self.items():
            free = []
            for token in k:
                if token in evalmap:
                    v *= evalmap[token]
                else:
                    free.append(token)
            a[tuple(sorted(free))] += v
        return a

    def to_list(self):
        return ['*'.join((str(v),) + k) for k, v in sorted(self.items(), key=lambda x: (-len(x[0]), x[0], x[1])) if v]


class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        evalmap = dict(zip(evalvars, evalints))

        def combine(left, right, symbol):
            if symbol == '*':
                return left * right
            elif symbol == '+':
                return left + right
            elif symbol == '-':
                return left - right

        def make(exp):
            if exp.isdigit():
                return Poly({(): int(exp)})
            else:
                return Poly({(exp,): 1})

        def parse(exp):
            bucket = []
            symbols = []
            i = 0
            while i < len(exp):
                if exp[i] == '(':
                    bal = 1
                    for j in range(i + 1, len(exp)):
                        if exp[j] == '(':
                            bal += 1
                        elif exp[j] == ')':
                            bal -= 1
                        if bal == 0:
                            bucket.append(parse(exp[i + 1:j]))
                            break
                    i = j
                elif exp[i].isalnum():
                    for j in range(i, len(exp)):
                        if exp[j] == ' ':
                            bucket.append(make(exp[i:j]))
                            break
                    else:
                        bucket.append(make(exp[i:]))
                    i = j
                elif exp[i] in '*+-':
                    symbols.append(exp[i])
                i += 1
            for i in range(len(symbols) - 1, -1, -1):
                if symbols[i] == '*':
                    bucket[i] = combine(bucket[i], bucket.pop(i + 1), symbols.pop(i))
            if not bucket: return Poly()
            ans = bucket[0]
            for i, symbol in enumerate(symbols, 1):
                ans = combine(ans, bucket[i], symbol)
            return ans

        a = Poly(parse(expression)).evaluate(evalmap)
        return a.to_list()


Solution().basicCalculatorIV("a * b * c + b * a * c * 4", [], [])
