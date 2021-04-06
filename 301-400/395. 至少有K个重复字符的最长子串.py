'''找到给定字符串（由小写字符组成）中的最长子串 T ， 要求 T 中的每一字符出现次数都不少于 k 。输出 T 的长度。

示例 1:

输入:
s = "aaabb", k = 3

输出:
3

最长子串为 "aaa" ，其中 'a' 重复了 3 次。
示例 2:

输入:
s = "ababbc", k = 2

输出:
5

最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

# 1 递归
import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        m = collections.Counter(s)
        for c in m:
            if m[c]<k:
                return max([self.longestSubstring(i,k) for i in s.split(c)])
        return len(s)

# 2 栈 for else用法
# for循环结束后执行else，break可跳过else
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        stack=[s]
        ma=0
        while stack:
            a=stack.pop()
            m=collections.Counter(a)
            for c in m:
                if m[c]<k:
                    stack.extend(a.split(c))
                    break
            else:
                ma=max(ma,len(a))
        return ma


