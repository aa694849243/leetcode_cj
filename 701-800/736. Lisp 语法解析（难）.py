'''给定一个类似 Lisp 语句的表达式 expression，求出其计算结果。

表达式语法如下所示:

表达式可以为整数，let 语法，add 语法，mult 语法，或赋值的变量。表达式的结果总是一个整数。
(整数可以是正整数、负整数、0)
let 语法表示为 (let v1 e1 v2 e2 ... vn en expr), 其中 let语法总是以字符串 "let"来表示，接下来会跟随一个或多个交替变量或表达式，也就是说，第一个变量 v1被分配为表达式 e1 的值，第二个变量 v2 被分配为表达式 e2 的值，以此类推；最终 let 语法的值为 expr表达式的值。
add 语法表示为 (add e1 e2)，其中 add 语法总是以字符串 "add"来表示，该语法总是有两个表达式e1、e2, 该语法的最终结果是 e1 表达式的值与 e2 表达式的值之和。
mult 语法表示为 (mult e1 e2) ，其中 mult 语法总是以字符串"mult"表示， 该语法总是有两个表达式 e1、e2，该语法的最终结果是 e1 表达式的值与 e2 表达式的值之积。
在该题目中，变量的命名以小写字符开始，之后跟随0个或多个小写字符或数字。为了方便，"add"，"let"，"mult"会被定义为"关键字"，不会在表达式的变量命名中出现。
最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。我们将保证每一个测试的表达式都是合法的。有关作用域的更多详细信息，请参阅示例。
 

示例：

输入: (add 1 2)
输出: 3

输入: (mult 3 (add 2 3))
输出: 15

输入: (let x 2 (mult x 5))
输出: 10

输入: (let x 2 (mult x (let x 3 y 4 (add x y))))
输出: 14
解释:
表达式 (add x y), 在获取 x 值时, 我们应当由最内层依次向外计算, 首先遇到了 x=3, 所以此处的 x 值是 3.


输入: (let x 3 x 2 x)
输出: 2
解释: let 语句中的赋值运算按顺序处理即可

输入: (let x 1 y 2 x (add x y) (add x y))
输出: 5
解释:
第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。
第二个 (add x y) 计算结果就是 3+2 = 5 。

输入: (let x 2 (add (let x 3 (let x 4 x)) x))
输出: 6
解释:
(let x 4 x) 中的 x 的作用域仅在()之内。所以最终做加法操作时，x 的值是 2 。

输入: (let a1 3 b2 (add a1 1) b2)
输出: 4
解释:
变量命名时可以在第一个小写字母后跟随数字.
 

注意:

我们给定的 expression 表达式都是格式化后的：表达式前后没有多余的空格，表达式的不同部分(关键字、变量、表达式)之间仅使用一个空格分割，并且在相邻括号之间也没有空格。我们给定的表达式均为合法的且最终结果为整数。
我们给定的表达式长度最多为 2000 (表达式也不会为空，因为那不是一个合法的表达式)。
最终的结果和中间的计算结果都将是一个 32 位整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/parse-lisp-expression
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 表达式解析
def implicit_scope(func):
    def wrapper(*args):
        args[0].scope.append({})  # args[0]为函数，args[1]为参数
        ans = func(*args)
        args[0].scope.pop()
        return ans

    return wrapper


class Solution(object):
    def __init__(self):
        self.scope = [{}]

    @implicit_scope
    def evaluate(self, expression):
        if not expression.startswith('('):
            if expression[0].isdigit() or expression[0] == '-':
                return int(expression)
            for local in reversed(self.scope):
                if expression in local: return local[expression]

        tokens = list(self.parse(expression[5 + (expression[1] == 'm'): -1]))  # mult多一个字母
        if expression.startswith('(add'):
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expression.startswith('(mult'):
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:
            for j in range(1, len(tokens), 2):
                self.scope[-1][tokens[j - 1]] = self.evaluate(tokens[j])
            return self.evaluate(tokens[-1])

    def parse(self, expression):
        bal = 0
        buf = []
        for token in expression.split():
            bal += token.count('(') - token.count(')')
            buf.append(token)
            if bal == 0:
                yield " ".join(buf)
                buf = []
        if buf:
            yield " ".join(buf)

print(Solution().evaluate(
    "(let x 2 (mult x (let x 3 y 4 (add x y))))"
))
# 1仿写 字符串递归
# mult和add必跟两个字段，形如(mult a b) (add a b)；let跟奇数个字段，形如(let a 1 a+1) (let a 1 b 2 expression)
def implicit_scope(func):
    def wrapper(*args, **kwargs):
        args[0].scope.append({})
        ans = func(*args)
        args[0].scope.pop()
        return ans

    return wrapper


class Solution(object):
    def __init__(self):
        self.scope = [{}]

    @implicit_scope
    def evaluate(self, expression):  # 每一个expression生成一个{},括号结束或表达式结束弹出这个{}
        if expression[0] != '(':
            if expression[0].isdigit() or expression[0] == '-':
                return int(expression)
            for local in self.scope[::-1]:  # 寻找前一个对应变量的值
                if expression in local:
                    return local[expression]
        tokens = list(self.parse(expression[5 + (expression[1] == 'm'):-1]))  # mult比let和add多一个字母
        if expression[1] == 'a':
            return self.evaluate(tokens[0]) + self.evaluate(tokens[1])
        elif expression[1] == 'm':
            return self.evaluate(tokens[0]) * self.evaluate(tokens[1])
        else:  # let的情况
            for i in range(1, len(tokens), 2):
                self.scope[-1][tokens[i - 1]] = self.evaluate(tokens[i])
            return self.evaluate(tokens[-1])

    def parse(self, s):
        b = []
        bal = 0
        for ch in s.split():
            bal += ch.count('(') - ch.count(')')
            b.append(ch)
            if bal == 0:
                yield ' '.join(b)
                b = []
        if b:
            yield ' '.join(b)


# 2正则表达式
# https://leetcode-cn.com/problems/parse-lisp-expression/solution/python-di-gui-ji-jian-li-yong-zheng-ze-he-nei-zhi-/
# 正则表达式分割括号 eval制作元组 eval制作列表 eval妙用
import re


class Solution:
    def evaluate(self, expression: str) -> int:
        def f(vals, obj):
            if isinstance(obj, tuple):
                if obj[0] == 'let':
                    vals = vals.copy()
                    for i in range(1, len(obj) - 1, 2):
                        vals[obj[i]] = f(vals, obj[i + 1])
                    return f(vals, obj[-1])
                if obj[0] == 'add':
                    return f(vals, obj[1]) + f(vals, obj[2])
                if obj[0] == 'mult':
                    return f(vals, obj[1]) * f(vals, obj[2])
            return eval(obj, vals)

        return f({}, eval(re.sub(r'([^( )]+)', r"'\1'", expression).replace(' ', ',')))#r'([^( )]+)'组匹配非括号和空格字符串，r"'\1'"将gorup[1]的内容替换为‘group[1]’


Solution().evaluate('(let a 2 a)')
