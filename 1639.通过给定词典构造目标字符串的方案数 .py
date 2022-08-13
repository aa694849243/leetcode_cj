import collections
from typing import List

# https://leetcode.cn/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/solution/1639-cji-hu-shuang-bai-de-dong-tai-gui-h-jmp6/
# @solution-sync:begin
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mode=10**9+7
        m, n = len(words[0]), len(target)
        cnt = [collections.defaultdict(int) for _ in range(m)]
        for i in range(len(words)):
            for j in range(m):
                ch = words[i][j]
                cnt[j][ch] += 1
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = cnt[0][target[0]]
        for i in range(1,m):
            dp[i][0]=dp[i-1][0]+cnt[i][target[0]]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i-1][j]+dp[i-1][j-1]*cnt[i][target[j]]
                dp[i][j]%=mode
        return dp[-1][-1]
