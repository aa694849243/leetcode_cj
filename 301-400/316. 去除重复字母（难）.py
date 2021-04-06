'''给你一个仅包含小写字母的字符串，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证返回结果的字典序最小（要求不能打乱其他字符的相对位置）。

 

示例 1:

输入: "bcabc"
输出: "abc"
示例 2:

输入: "cbacdcbc"
输出: "acdb"
 

注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters 相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-letters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        a = collections.Counter(s)
        stack = []
        m = set()
        for i in range(len(s)):
            if not stack or s[i] > stack[-1]:
                if s[i] in m:
                    a[s[i]] -= 1
                else:
                    stack.append(s[i])
                    m |= {s[i]}
            else:
                if s[i] in m:
                    a[s[i]] -= 1
                else:
                    while stack and s[i] <= stack[-1] and a[stack[-1]] > 1:
                        a[stack[-1]] -= 1
                        m -= {stack[-1]}
                        stack.pop()
                    stack.append(s[i])
                    m |= {s[i]}

        return ''.join(stack)


# 精妙递归
import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c=collections.Counter(s)
        pos=0
        for i in range(len(s)):
            if s[i]<s[pos]:pos=i
            c[s[i]]-=1
            if c[s[i]]==0:
                break
        return s[pos]+self.removeDuplicateLetters(s[pos:].replace(s[pos],'')) if s else ''


b = "cbacdcbc"
Solution().removeDuplicateLetters(b)
