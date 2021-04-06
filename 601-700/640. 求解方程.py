'''求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。

如果方程没有解，请返回“No solution”。

如果方程有无限解，则返回“Infinite solutions”。

如果方程中只有一个解，要保证返回值 x 是一个整数。

示例 1：

输入: "x+5-3+x=6+x-2"
输出: "x=2"
示例 2:

输入: "x=x"
输出: "Infinite solutions"
示例 3:

输入: "2x=x"
输出: "x=0"
示例 4:

输入: "2x+3x-6x=x+2"
输出: "x=-1"
示例 5:

输入: "x=x+2"
输出: "No solution"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/solve-the-equation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


class Solution:
    def solveEquation(self, equation: str) -> str:
        a, b = equation.split('=')
        co = 0
        constant = 0
        m = 0
        flag = 1
        for i in range(len(a)):
            if a[i].isdigit():
                m *= 10
                m += int(a[i])
            elif a[i] == 'x':
                if m == 0 and i > 0 and a[i - 1] != '0':
                    co += flag * 1
                elif m == 0 and i == 0:
                    co += flag * 1
                else:
                    co += flag * m
                constant -= m * flag
            elif a[i] == '+':
                constant += flag * m
                m = 0
                flag = 1
            elif a[i] == '-':
                constant += flag * m
                m = 0
                flag = -1
        constant += flag * m
        flag = -1
        m = 0
        for i in range(len(b)):
            if b[i].isdigit():
                m *= 10
                m += int(b[i])
            elif b[i] == 'x':
                if m == 0 and i > 0 and b[i - 1] != '0':
                    co += flag * 1
                elif m == 0 and i == 0:
                    co += flag * 1
                else:
                    co += flag * m
                constant -= flag * m
            elif b[i] == '+':
                constant += flag * m
                m = 0
                flag = -1
            elif b[i] == '-':
                constant += flag * m
                m = 0
                flag = 1
        constant += flag * m
        if co == 0 and constant == 0:
            return 'Infinite solutions'
        elif co == 0 and constant != 0:
            return 'No solution'
        else:
            return 'x=' + str((-1 * constant) // co)


Solution().solveEquation("x+5-3+x=6+x-2")
