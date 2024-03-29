'''
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            while left<len(s) and not (s[left].isdigit() or s[left].isalnum()):
                left += 1
            while right>=0 and not (s[right].isdigit() or s[right].isalnum()):
                right -= 1
            if left < right:
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                return True
        return True
Solution().isPalindrome("A man, a plan, a canal: Panama")
