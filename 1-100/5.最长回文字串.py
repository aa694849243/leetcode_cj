'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# -----------------------中心扩展法--caojie-----------------------------------------------------------
def longestPalindrome(s: str) -> str:
    smax = []
    stack = []
    if len(s) == 0:
        return ''
        # 空字符串返回空
    if len(s) == 1:
        return s[0]
        # 只有一个字符串，返回本身
    if len(s) == 2:
        if s[0] == s[1]:
            return s
        return s[0]
        # 有两个字符串，观察返回值
    for i in range(2, len(s)):
        # 字符串大于2的情况，每次以s[i]为中心，需要考虑两种情况，中心数为1个，和中心数为2个的情况
        if s[i] == s[i - 2]:
            # 如果中心数为单个值时的情况，如‘bab’
            n = 2
            j = i
            stack.append(s[i - 1])  # 将单个中心数先取出
            while j < len(s) and i - n >= 0 and s[j] == s[i - n]:
                stack.append(s[j])  # 将相同的数压入栈中
                n += 1
                j += 1
            stack = stack[::-1][:-1] + stack  # 将栈中的数扩充为原本的回文序列
            smax = stack if len(stack) > len(smax) else smax  # smax为最长的回文序列
            smax = smax.copy()  # 需要把smax拷贝出来，要不然stack和smax指向同一个序列，stack清空smax也会清空
            stack.clear()  # 清空栈，开始下一轮循环
        if s[i] == s[i - 1]:
            # 中心数为两个数的情况如‘baab’
            n = 1
            j = i
            while j < len(s) and i - n >= 0 and s[j] == s[i - n]:
                stack.append(s[j])
                j += 1
                n += 1
            stack = stack[::-1] + stack
            smax = stack if len(stack) > len(smax) else smax
            smax = smax.copy()
            stack.clear()
    if smax == []:  # 如果最后smax未存入任何数，表明从第3个数开始后没有发现任何回文数
        if s[0] == s[1]:  # 如果前2个数相同，那么前2个数就是最大回文数
            return s[:2]
        return s[0]  # 前2个数不同，则整个序列无大于等于2的回文，返回s[0]作为最大回文
    return ''.join(smax)


# -------------动态规划_填表法--------------------------------------------------------
def longestPalindrome(s: str) -> str:
    n = len(s)
    ans=''
    dp = [[False] * n for _ in range(n)]  # 做一张动态转移表dp
    for l in range(n):  # l+1为i-j的长度
        for i in range(n):  # 从i出发找回文
            j = i + l  # 每次找每次i:j中的回文序列
            if j > n - 1:  # j超过边界跳出循环
                break
            if l == 0:  # 起始状态1：l+1==1，即单个字符一定为回文序列
                dp[i][j] = True
            elif l == 1:  # 起始状态2：长度为2时，比对i和i+1出
                dp[i][j] = (s[i]==s[j])
            else:
                dp[i][j]=(dp[i+1][j-1] and s[i]==s[j]) #每次只要找到前一步定位的状态就可以确定此步的状态
                #状态转移方程
            if dp[i][j] and l+1>len(ans): #长度大于上一步保存的len(ans)则更新ans
                ans=s[i:j+1] #每次dp[i][j]为True,此时的长度都为l+1
    return ans

n = len('abchdll')
dp = [[False] * n for _ in range(n)]

s = 'aaaa'
s = 'babad'
longestPalindrome(s)
