'''
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# 特殊动态规划 一维动态规划 精妙动态规划
class Solution:
    def minCut(self, s: str) -> int:
        if not s:
            return 0
        lenth = len(s)
        dp = [-1]  # 起始位，如果序列整体对称的话为dp[0]+1=0,即不需要分割
        for i in range(1, lenth + 1):
            candi = []  # 候选序列
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:  # 以i为终点，由起点向终点收缩，如果发现一个对称序列，则计算最小分割数，加入候选序列
                    candi.append(dp[j] + 1)
                    continue
            dp.append(min([dp[-1] + 1] + candi))  # dp[-1]+1意味着前面最小分割数+1即为当前分割数，与candidate比较
        return dp[-1]


a = 'aabbaaaaaa'
Solution().minCut(a)
