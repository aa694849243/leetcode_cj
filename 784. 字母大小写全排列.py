'''给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

 

示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]
 

提示：

S 的长度不超过12。
S 仅由数字和字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-case-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1回溯法 时间复杂度O(N*2^N)
class Solution:
    def __init__(self):
        self.m = set()

    def letterCasePermutation(self, S: str) -> List[str]:

        def backtrack(s, i):
            if i >= len(s):
                return
            if s[i].isdigit():
                backtrack(s, i + 1)
            u = s[:i] + s[i].upper() + s[i + 1:]
            l = s[:i] + s[i].lower() + s[i + 1:]
            self.m |= {u, l}
            backtrack(u, i + 1)
            backtrack(l, i + 1)

        backtrack(S, 0)
        return list(self.m)


# 2位掩码
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        num = sum(ch.isalpha() for ch in S)
        ans = []
        for b in range(1 << num):
            word = []
            move = 0
            for ch in S:
                if ch.isalpha():
                    if (b>>move) & 1 == 1:
                        word.append(ch.lower())
                    else:
                        word.append(ch.upper())
                    move += 1
                else:
                    word.append(ch)
            ans.append(''.join(word))
        return ans
#3笛卡尔积
import itertools
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        f=lambda x:(x.upper(),x.lower()) if x.isalpha() else x
        return map(''.join,itertools.product(*map(f,S)))

Solution().letterCasePermutation("a1b2")