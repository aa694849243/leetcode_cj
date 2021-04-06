'''给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
 

提示：

输入的字符串长度不会超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1普通方法
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = 0
        for i in range(len(s)):
            for j in range(i + 1):
                if s[j:i + 1] == s[j:i + 1][::-1]:
                    dp += 1
        return dp


# 2马拉车 manacher
class Solution:
    def countSubstrings(self, s: str) -> int:
        s = '#' + '#'.join(s) + '#'
        id = 0
        mx = 0
        p = [0] * len(s)
        for i in range(len(s)):
            if mx > i:
                p[i] = min(p[2 * id - i], mx - i)
            else:
                p[i] = 0
            while i + p[i] < len(s) and i - p[i] >= 0 and s[i + p[i]] == s[i - p[i]]:
                p[i] += 1
            mx, id = (i + p[i], i) if i + p[i] > mx else (mx, id)
        cnt = 0
        for i in range(len(p)):
            cnt += (p[i] // 2)
        return cnt


b = "aba"
Solution().countSubstrings(b)
