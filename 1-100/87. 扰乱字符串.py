'''
给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。

下图是字符串 s1 = "great" 的一种可能的表示形式。

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。

例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
我们将 "rgeat” 称作 "great" 的一个扰乱字符串。

同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
我们将 "rgtae” 称作 "great" 的一个扰乱字符串。

给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。

示例 1:

输入: s1 = "great", s2 = "rgeat"
输出: true
示例 2:

输入: s1 = "abcde", s2 = "caebd"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/scramble-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 递归思路
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False
        l = len(s1)
        for i in range(1, l):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or self.isScramble(s1[:i], s2[-i:]) \
                    and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False


# 三维动态规划思路
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        l = len(s1)
        dp = [[[False for _ in range(l)] for _ in range(l)] for _ in range(l + 1)]
        for i in range(l - 1, -1, -1):
            for j in range(l - 1, -1, -1):
                for K in range(1, l + 1):
                    if i + K > l or j + K > l:
                        continue
                    if s1[i:i + K] == s2[j:j + K]:
                        dp[K][i][j] = True
                    elif K == 1:
                        continue
                    else:
                        for k in range(1, K):
                            if dp[k][i][j] and dp[K - k][i + k][j + k]:
                                dp[K][i][j] = True
                                break
                            elif dp[k][i][j + K - k] and dp[K - k][i + k][j]:
                                dp[K][i][j] = True
                                break
        return dp[l][0][0]
