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


# 动态规划思路
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        dp = [[[False] * (len(s1) + 1) for _ in range(len(s2))] for _ in range(len(s1))]
        # 初始化
        l1, l2 = len(s1), len(s2)
        for i in range(l1):
            for j in range(l2):
                dp[i][j][1] = s1[i] == s2[j]
        # 填制dp表,dp[i][j][l]为s1从i，s2从j开始长度为l的是否为scramble数组
        # 三个问题
        # 1：转移方程，设置长度为k的分割点 dp[i][j][l]需要考察(dp[i][j][k] and dp[i+k][j+k][l-k]) 或者 dp[i+k][j][l-k] and dp[i][j+l-k][k]
        # 2：为什么l从1开始？因为题目中明确规定子树为非空树，即使有空树，交换也是无意义的。
        # 3：为什么从0，0开始遍历，因为最高层为l，l为1时的所有情况已经在初始化的过程中设置完了。之后层次的所有值都可以从前一层次的值获取到
        for l in range(2, l1 + 1):  # 为什么要l1+1,因为到l1-1其实就得到我们所有想要的元素，可以求出dp[0][0][l1]的值了，但是需要多出计算的一步，公式是一致的，可以扩充一格存放结果值
            for i in range(l1 - l + 1):
                for j in range(l1 - l + 1):
                    for k in range(1, l):
                        if (dp[i][j][k] and dp[i + k][j + k][l - k]) or (dp[i + k][j][l - k] and dp[i][i + l - k][k]):
                            dp[i][j][l] = True  # 从k为1开始遍历，只要有一个为True,即dp[i][j][l]=True,有False值也不会修改
        return dp[0][0][l1]
