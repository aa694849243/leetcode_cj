'''给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：

任何左括号 ( 必须有相应的右括号 )。
任何右括号 ) 必须有相应的左括号 ( 。
左括号 ( 必须在对应的右括号之前 )。
* 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。
一个空字符串也被视为有效字符串。
示例 1:

输入: "()"
输出: True
示例 2:

输入: "(*)"
输出: True
示例 3:

输入: "(*))"
输出: True
注意:

字符串大小将在 [1，100] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parenthesis-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1贪心
# lo、hi表示「可能多余的左括号」，一个下界，一个上界，很直观。执行起来就是
#
# 遇到左括号：lo++, hi++
# 遇到星号：lo--, hi++（因为星号有三种情况）
# 遇到右括号：lo--, hi--
# lo要保持不小于0。（要理解lo的意思，考虑下这个例子(**)(
# 如果hi < 0，说明把星号全变成左括号也不够了，False
# 最後，如果lo > 0，说明末尾有多余的左括号，Fals
class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s:
            return True
        lo, hi = 0, 0
        for i in range(len(s)):
            if s[i] == '(':
                lo += 1
                hi += 1
            elif s[i] == ')':
                lo = lo - 1 if lo > 0 else 0
                hi -= 1
                if hi < 0: return False
            else:
                lo = lo - 1 if lo > 0 else 0
                hi += 1
        return lo==0


Solution().checkValidString("(*()()())**((*()*))((*()*)")
