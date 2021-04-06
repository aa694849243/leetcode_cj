'''给定两个字符串 a 和 b，寻找重复叠加字符串 a 的最小次数，使得字符串 b 成为叠加后的字符串 a 的子串，如果不存在则返回 -1。

注意：字符串 "abc" 重复叠加 0 次是 ""，重复叠加 1 次是 "abc"，重复叠加 2 次是 "abcabc"。

 

示例 1：

输入：a = "abcd", b = "cdabcdab"
输出：3
解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。
示例 2：

输入：a = "a", b = "aa"
输出：2
示例 3：

输入：a = "a", b = "a"
输出：1
示例 4：

输入：a = "abc", b = "wxyz"
输出：-1
 

提示：

1 <= a.length <= 104
1 <= b.length <= 104
a 和 b 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-string-match
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1 投机
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na = len(a)
        nb = len(b)  # b最多比a里面多两个
        q = (nb - 1) // na + 1
        if b in a * q:
            return q
        elif b in a * (q + 1):
            return q + 1
        return -1


# 2普通匹配
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        q = (len(b) - 1) // len(a) + 1
        i = 0
        A1 = a * q
        A2 = a * (q + 1)
        while i < len(A1):
            if A1[i:i + len(b)] == b:
                return q
            i += 1
        i = 0
        while i < len(A2):
            if A2[i:i + len(b)] == b:
                return q + 1
            i += 1
        return -1


# 3 Rabin-Karp
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        base, mod = 113, 10 ** 9 + 9 #base值和模

        def hash(s): #哈希值计算公式
            h = 0
            for i in range(len(s)):
                h = (h * base + ord(s[i])) % mod
            return h

        q = (len(b) - 1) // len(a) + 1
        A1 = a * q
        A2 = a * (q + 1)
        hashA1 = hash(A1[:len(b)])
        hashA2 = hash(A2[:len(b)])
        hashb = hash(b)
        i = len(b)
        mult = pow(base, len(b) - 1, mod)
        while i < len(A1):
            if hashA1 == hashb:
                if A1[i - len(b):i] == b: #hash值相等，进一步检查子串是否确实相同
                    return q
            hashA1 = ((hashA1 - ord(A1[i - len(b)]) * mult) * base + ord(A1[i])) % mod #不断更新A1子串hash值
            i += 1
        if hashA1 == hashb: #跳出循环后再检查一遍更新的hashA1和hahb
            if A1[i - len(b):i] == b:
                return q
        i = len(b)
        while i < len(A2):
            if hashA2 == hashb:
                if A2[i - len(b):i] == b:
                    return q + 1
            hashA2 = ((hashA2 - ord(A2[i - len(b)]) * mult) * base + ord(A2[i])) % mod #不断更新A2hash值
            i += 1
        if hashA2==hashb:
            if A2[i-len(b):i]==b:
                return q+1
        return -1

Solution().repeatedStringMatch("aaac", "aac")
