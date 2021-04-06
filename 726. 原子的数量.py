'''给定一个化学式formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随0个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如 H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

示例 1:

输入:
formula = "H2O"
输出: "H2O"
解释:
原子的数量是 {'H': 2, 'O': 1}。
示例 2:

输入:
formula = "Mg(OH)2"
输出: "H2MgO2"
解释:
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
示例 3:

输入:
formula = "K4(ON(SO3)2)2"
输出: "K4N2O14S4"
解释:
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
注意:

所有原子的第一个字母为大写，剩余字母都是小写。
formula的长度在[1, 1000]之间。
formula只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-atoms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
import collections


# 1有限状态自动机
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        # states = {'upper': ['lower', 'upper', 'number', 'l_p', 'r_p'],
        #           'lower': ['upper', 'number', 'l_p', 'r_p'],
        #           'number': ['upper', 'number', 'l_p', 'r_p'],
        #           'l_p': ['upper', 'l_p'],
        #           'r_p': ['upper', 'number', 'lp']}
        stack = []
        a = ''  # a代表原子式
        n = 0
        for i in range(len(formula)):
            if i == 0:  # 初始只能为左括号或大写字母
                if formula[i] == '(':
                    stack.append('(')
                    state = 'l_p'
                else:
                    a += formula[i]
                    state = 'upper'
                continue
            if state == 'upper':  # 当处于大写字母状态时，可转移到如下5个状态
                if formula[i].islower():  # 遇到小写字母，更新原子式
                    a += formula[i]
                    stack.append([a, 0])
                    state = 'lower'
                elif formula[i].isupper():  # 遇到大写字母，则储存上一个原子式入栈，数量为1
                    stack.append([a, 1])
                    a = formula[i]
                    state = 'upper'
                elif formula[i].isdigit():  # 遇到数字则储存上一个原子式入栈，数量未知
                    stack.append([a, 0])
                    n = n * 10 + int(formula[i])
                    state = 'number'
                elif formula[i] == '(':  # 遇到左右括号，更新状态，并需要额外将左右括号入栈
                    stack.append([a, 1])
                    stack.append('(')
                    state = 'l_p'
                elif formula[i] == ')':
                    stack.append([a, 1])
                    stack.append(')')
                    state = 'r_p'
            elif state == 'lower':  # 状态为小写字母
                if formula[i].isupper():
                    stack[-1][1] = 1
                    a = formula[i]
                    state = 'upper'
                elif formula[i].isdigit():
                    n = n * 10 + int(formula[i])
                    state = 'number'
                elif formula[i] == '(':
                    stack[-1][1] = 1
                    stack.append('(')
                    state = 'l_p'
                elif formula[i] == ')':
                    stack[-1][1] = 1
                    stack.append(')')
                    state = 'r_p'
            elif state == 'number':  # 状态为数字
                if formula[i].isdigit():  # 接着遇到数字就更新数量
                    n = n * 10 + int(formula[i])
                else:
                    if stack[-1] != ')':  # 如果遇到非数字，且栈顶部不为右括号，则更新栈顶原子的数量
                        stack[-1][1] = n
                    else:  # 遇到右括号
                        li = []
                        stack.pop()  # 弹出')'
                        while stack[-1] != '(':  # 更新括号中原子的数量
                            x = stack.pop()
                            x[1] = x[1] * n
                            li.append(x)
                        stack.pop()  # 弹出'('
                        stack.extend(li[::-1])
                    n = 0
                    if formula[i].isupper():  # 将新的原子入栈，并更新状态
                        a = formula[i]
                        state = 'upper'
                    elif formula[i] == '(':
                        stack.append('(')
                        state = 'l_p'
                    elif formula[i] == ')':
                        stack.append(')')
                        state = 'r_p'
            elif state == 'l_p':
                if formula[i].isupper():
                    a = formula[i]
                    state = 'upper'
                elif formula[i] == '(':
                    stack.append('(')
                    state = 'l_p'
            elif state == 'r_p':  # 状态为右括号
                if formula[i].isdigit():
                    n = n * 10 + int(formula[i])
                    state = 'number'
                else:  # 如果遇到非数字，则说明括号里的原子数量不变，那么只需要弹出栈里的括号就行了
                    stack.pop()
                    li = []
                    while stack[-1] != '(':
                        li.append(stack.pop())
                    stack.pop()
                    stack.extend(li)
                    if formula[i].isupper():
                        a = formula[i]
                        state = 'upper'
                    elif formula[i] == '(':
                        stack.append('(')
                        state = 'l_p'
        if state == 'r_p':  # 考虑最后一个字符的情况，如果最后一个字符为右括号，那么要消除栈中相应的括号
            stack.pop()
            li = []
            while stack[-1] != '(':
                li.append(stack.pop())
            stack.pop()
            stack.extend(li)
        elif state == 'upper':  # 最后一个字符为大写字母，则将a原子入栈，数量为1个
            stack.append([a, 1])
        elif state == 'number':  # 最后为数字，那么需要更新栈中相应原子的数量
            if stack[-1] != ')':
                stack[-1][1] = n
            else:
                stack.pop()
                li = []
                while stack[-1] != '(':
                    x = stack.pop()
                    x[1] = n * x[1]
                    li.append(x)
                stack.pop()
                stack.extend(li)
        stack.sort()  # 字典序排序
        res = []
        for x in stack:
            if not res or x[0] != res[-1][0]:
                res.append([x[0], x[1]])
            elif x[0] == res[-1][0]:  # 相同原子数量合并
                res[-1][1] += x[1]
        ans = ''
        for x in res:
            ans += x[0]
            if x[1] > 1:
                ans += str(x[1])

        return ans


# https://leetcode-cn.com/problems/number-of-atoms/solution/yuan-zi-de-shu-liang-by-leetcode/
# 2官方 递归
class Solution(object):
    def countOfAtoms(self, formula):
        def parse():
            N = len(formula)
            count = collections.Counter()
            while (self.i < N and formula[self.i] != ')'):
                if (formula[self.i] == '('):
                    self.i += 1
                    for name, v in parse().items():
                        count[name] += v
                else:
                    i_start = self.i
                    self.i += 1
                    while (self.i < N and formula[self.i].islower()):
                        self.i += 1
                    name = formula[i_start: self.i]
                    i_start = self.i
                    while (self.i < N and formula[self.i].isdigit()):
                        self.i += 1
                    count[name] += int(formula[i_start: self.i] or 1)
            self.i += 1
            i_start = self.i
            while (self.i < N and formula[self.i].isdigit()):
                self.i += 1
            if (i_start < self.i):
                multiplicity = int(formula[i_start: self.i])
                for name in count:
                    count[name] *= multiplicity

            return count

        self.i = 0
        ans = []
        count = parse()
        for name in sorted(count):
            ans.append(name)
            multiplicity = count[name]
            if multiplicity > 1:
                ans.append(str(multiplicity))
        return "".join(ans)


# 3栈
class Solution(object):
    def countOfAtoms(self, formula):
        N = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))

#4正则表达式
import re
class Solution(object):
    def countOfAtoms(self, formula):
        parse = re.findall(r"([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [collections.Counter()]
        for name, m1, left_open, right_open, m2 in parse:
            if name:
              stack[-1][name] += int(m1 or 1)
            if left_open:
              stack.append(collections.Counter())
            if right_open:
                top = stack.pop()
                for k in top:
                  stack[-1][k] += top[k] * int(m2 or 1)

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))

Solution().countOfAtoms("K4(ON(SO3)2)2")
