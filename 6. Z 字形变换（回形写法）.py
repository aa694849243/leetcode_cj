'''
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

L   C   I   R
E T O E S I I G
E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);
示例 1:

输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"
示例 2:

输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"
解释:

L     D     R
E   O E   I I
E C   I H   N
T     S     G

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处
'''


def convert(s: str, numRows: int) -> str:
    if len(s) <= numRows or numRows == 1:  # 只有1行，或字母数小于行数则直接输出原序列
        return s

    l = [[] for _ in range(numRows + 1)]  # 构造列表l里面有numrows+1行是为了计数方便，第一个为0行不保存任何数据，最后删去
    x = numRows + numRows - 2  # x为基础数，如为4行的话，基础数应该为6，这样构成一个循环好计数，4为行数，往上在增加两行后再回到第1行
    for i in range(len(s)):
        j = (i + 1) % x  # i+1除以基础数进行观察
        if j <= numRows and j != 0:  # 如果余数小于等于行数，那么该处字母就存入余数那一行
            l[j].append(s[i])
        elif j == 0:  # 如果等于零，那么就正好在第2行，继续下去就回到第一行了
            l[2].append(s[i])
        else:  # 如果余数大于行数小于基础数，那么通过观察就能发现字母会 停留在（2*numrows)余数这一行
            j = 2 * numRows - j
            l[j].append(s[i])
    l.pop(0)
    s2 = ''
    for i in l:  # 对数据整合输出
        s2 += ''.join(i)
    return s2


# -----------------------------更简洁的方法--------leetcode题解-----------------------------------------------
def convert(s: str, numRows: int) -> str:
    if len(s) < 2: return s  # 小于2则输出原序列
    l = ['' for _ in range(numRows)]  # 直接构造字符形式的列表
    flag = -1  # 做标志，确定什么时候字符折返
    i = 0  # 代表行数起始
    for c in s:  # 回形写法技巧
        l[i] += c
        if i == 0 or i == numRows - 1:
            flag = -flag
        i += flag
    return ''.join(l)


s = 'A'
a = convert(s, 1)
a.pop(0)
x = ''
for i in a:
    x += ''.join(i)
a


