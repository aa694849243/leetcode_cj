"""
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
示例 3:

输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
示例 4:

输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
示例 5:

输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# --------------------------------回溯法---------------------------------------------------------------------------------
def isMatch(s: str, p: str) -> bool:
    if not p: return not s  # p为空时，s为空才匹配
    first_match = len(s) > 0 and p[0] in ('.', s[0])
    if len(p) >= 2 and p[1] == '*':  # 遇到‘*’号时处理方式
        return isMatch(s, p[2:]) or (isMatch(s[1:], p) and first_match)  # p[2]及其之后的继续比对，如果第一个对上了，则将s[0]删掉，继续比对
    else:
        return isMatch(s[1:], p[1:]) and first_match  # 没遇到星号（第二个数不为星号）则都删掉第一个数继续比对


# -----------动态规划---------自底向上：填表法--------------------------------------------------------------------------------------
# --https://leetcode-cn.com/problems/regular-expression-matching/solution/tong-guo-dong-tu-jian-ming-jiang-jie-hui-su-he-don/
# https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/
def isMatch(s: str, p: str) -> bool:
    n, m = len(s) + 1, len(p) + 1
    memo = [[False] * n for _ in range(m)]  # 初始化表格
    memo[-1][-1] = True
    for i in range(n - 1, -1, -1):
        for j in range(m - 2, -1, -1):  # j从倒数第二格往前找
            first_match = i < len(s) and (
                    p[j] == '.' or p[j] == s[i])  # 对当前字符配对,如果si==[]时，只有p[i]==[]才True，有*情况由memo[j+2][i]处理
            if j + 1 < len(p) and p[j + 1] == "*":
                memo[j][i] = memo[j + 2][i] or first_match and memo[j][i + 1]  # j+1为星号(j+1最大值为m-2),j=j+2或者i前移1格继续比
            else:
                memo[j][i] = first_match and memo[j + 1][i + 1]  # 没有星号整体前移一格继续比
    return memo[0][0]


# ------------动态规划------------自顶向下------------------------------------------------------------------------------------
def isMatch(s: str, p: str) -> bool:
    memo = {}  # 从空表加东西

    def match(j, i):

        if (j, i) not in memo:  # 如果不在则向下搜索
            if j == len(p):  # j匹配到了尽头，i一定要进入尽头才为真，尽头处代表空值
                ans = i == len(s)
            else:
                if j + 1 < len(p) and p[j + 1] == '*':
                    ans = match(j + 2, i) or (p[j] in ('.', s[i]) and i < len(s))
                else:
                    ans = (i < len(s) and p[j] in ('.', s[i])) and match(j + 1, i + 1)
            memo[j, i] = ans

        return memo[j, i]

    return match(0, 0)


s = 'aa'
p = 'a'
isMatch(s, p)
