'''
所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。

 

示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# Rabin-Karp,列表中数值大小小于100，可以用此算法
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        base, mod = 113, 10 ** 9 + 9
        m = {}
        hash = 0
        for i in range(10):
            hash = (hash * base + ord(s[i])) % mod
        m[hash] = s[:10]
        mult = pow(base, 9, mod)
        ans = set()
        for i in range(10, len(s)):
            hash = ((hash - ord(s[i - 10]) * mult) * base + ord(s[i])) % mod
            if hash not in m:
                m[hash] = s[i - 9:i + 1]
            elif s[i - 9:i + 1] == m[hash]:
                ans.add(s[i - 9:i])
        return list(ans)


# 官方
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        L, n = 10, len(s)
        if n <= L:
            return []

        # rolling hash parameters: base a
        a = 4
        aL = pow(a, L)

        # convert string to array of integers
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        h = 0
        seen, output = set(), set()
        # iterate over all sequences of length L
        for start in range(n - L + 1):
            # compute hash of the current sequence in O(1) time
            if start != 0:
                h = h * a - nums[start - 1] * aL + nums[start + L - 1]
            # compute hash of the first sequence in O(L) time
            else:
                for i in range(L):
                    h = h * a + nums[i]
            # update output and hashset of seen sequences
            if h in seen:
                output.add(s[start:start + L])
            seen.add(h)
        return output


# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / repeated - dna - sequences / solution / zhong - fu - de - dnaxu - lie - by - leetcode /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# 位操作 掩码
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s)<10:
            return []
        mask = {'A': 0, 'G': 1, 'C': 2, 'T': 3}
        smask = [mask[s[i]] for i in range(len(s))]
        h, l = 0, len(s)
        seen, ans = set(), set()
        for i in range(l - 9):
            if i != 0:
                h <<= 2
                h |= smask[i + 9]
                h &= (~(1 << 2 * 10) & ~(1 << (2 * 10 + 1)))
                if h not in seen:
                    seen.add(h)
                else:
                    ans.add(s[i:i+10])
            else:
                for j in range(10):
                    h <<= 2
                    h |= smask[j]
                seen.add(h)
        return list(ans)


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Solution().findRepeatedDnaSequences(s)
