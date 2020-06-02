"""'
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


def isPalindrome(x: int) -> bool:
    s = str(x)
    for i in range(len(s) // 2):  # 前一半和后一半对比
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


# -------------------2--以不转换为字符的方式做------------------------------
def isPalindrome(x: int) -> bool:
    b = x
    e = 0
    while b > 0:
        c = b % 10
        b = b // 10
        e = e * 10 + c
    if e == x:
        return True
    else:
        return False


# ----------------2--改良版----只抽1半--------------------------
def isPalindrome(x: int) -> bool:
    e = 0
    if x >= 0 and x < 10:  # 单个数字为回文
        return True
    if x < 0 or x % 10 == 0:  # 负数和0结尾的数字肯定不为回文
        return False
    while x > 0:
        c = x % 10
        x = x // 10
        e = e * 10 + c
        if e == x:  # 刚好到一半的情况
            return True
        if e > x:  # 过了一半的情况，此时数字长度为奇数，此时再多加一个判断即e//10是否与前半段相等
            break
    if e // 10 == x:
        return True
    else:
        return False


x = 121
isPalindrome(x)
a = b = 1
a = 3
b = 3

