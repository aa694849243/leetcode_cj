'''给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1模拟法
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) < 3:
            return True
        if s == s[::-1]:
            return True
        n = len(s)
        flag = 0
        a = b = True
        i = 0
        while i < n // 2:
            if s[i] != s[n - 1 - flag - i] and flag == 1:
                a = False
                break
            elif s[i] != s[n - 1 - flag - i]:
                flag = 1
                continue
            i += 1
        s_ = s[::-1]
        flag = 0
        i = 0
        while i < n // 2:
            if s_[i] != s_[n - 1 - flag - i] and flag == 1:
                b = False
                break
            elif s_[i] != s_[n - 1 - flag - i]:
                flag = 1
                continue
            i += 1
        return a or b


# 2官方方法更简洁 贪心+递归
# https://leetcode-cn.com/problems/valid-palindrome-ii/solution/yan-zheng-hui-wen-zi-fu-chuan-ii-by-leetcode-solut/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(low, high):
            i, j = low, high
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        low, high = 0, len(s) - 1
        while low < high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                return checkPalindrome(low + 1, high) or checkPalindrome(low, high - 1)
        return True


Solution().validPalindrome("abc")
