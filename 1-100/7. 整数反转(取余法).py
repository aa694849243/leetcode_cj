"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# ----------------------------转字符串方法--caojie------------------------------------------------------------
def reverse(x: int) -> int:
    s = ''
    if x > 0:
        x = str(x)
        for i in range(len(x) - 1, -1, -1):
            s += x[i]
        s = s.lstrip('0')
        x2 = int(s)
        if x2 <= (2 ** 31 - 1):
            return x2
        else:
            return 0
    elif x < 0:
        x = str(-x)
        for i in range(len(x) - 1, -1, -1):
            s += x[i]
        s = s.strip('0')
        x2 = int(s)
        x2 = -x2 if x2 <= (2 ** 31) else 0
    else:  # 等于0时直接输出
        x2 = x
    return x2


# ---------------------------取余法---------------------------------------------------------------------------
def reverse(x: int) -> int:
    flag = 1
    ans = 0
    if x < 0:
        x, flag = -x, -flag
    while x != 0:
        cur = x % 10
        ans = cur + ans * 10
        x //= 10
    return ans * flag if -2 ** 31 <= ans * flag < 2 ** 31 else 0  # '**'优先级高于单元运算符‘-’
a=123
reverse(a)
