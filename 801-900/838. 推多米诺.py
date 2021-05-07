# 一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。
#
#  在开始时，我们同时把一些多米诺骨牌向左或向右推。
#
#
#
#  每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。
#
#  同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
#
#  如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。
#
#  就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。
#
#  给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] = '
# R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。
#
#  返回表示最终状态的字符串。
#
#  示例 1：
#
#  输入：".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.."
#
#  示例 2：
#
#  输入："RR.L"
# 输出："RR.L"
# 说明：第一张多米诺骨牌没有给第二张施加额外的力。
#
#  提示：
#
#
#  0 <= N <= 10^5
#  表示多米诺骨牌状态的字符串只含有 'L'，'R'; 以及 '.';
#
#  Related Topics 双指针 动态规划
#  👍 97 👎 0

# 1动态规划
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) < 2:
            return dominoes
        dp = [x for x in dominoes]
        while True:
            l, r = 0, len(dp)
            ndp = ['.'] * r
            for i in range(r):
                if dp[i] != '.':
                    ndp[i] = dp[i]
                    continue
                if i == 0:
                    ndp[i] = 'L' if dp[i + 1] == 'L' else dp[i]
                elif i == r - 1:
                    ndp[i] = 'R' if dp[i - 1] == 'R' else dp[i]
                else:
                    if dp[i - 1] == 'R' and dp[i + 1] == 'L':
                        continue
                    elif dp[i - 1] == 'R':
                        ndp[i] = 'R'
                    elif dp[i + 1] == 'L':
                        ndp[i] = 'L'
            if ndp == dp:
                break
            dp = ndp
        return ''.join(ndp)


# 2O(n)方法 相邻标记
import itertools


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) < 2:
            return dominoes
        symobls = [(-1, 'L')] + [(i, x) for i, x in enumerate(dominoes) if x != '.'] + [(len(dominoes), 'R')]
        ans = list(dominoes)
        for (i, x), (j, y) in itertools.zip_longest(symobls[:-1], symobls[1:]):
            if x == y:
                for k in range(i + 1, j):
                    ans[k] = x
            elif x > y:  # Rl
                for k in range(i + 1, j):
                    ans[k] = '.' if k - i == j - k else 'R' if k - i < j - k else 'L'
        return ''.join(ans)


# 3受力分析
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) < 2:
            return dominoes
        n = len(dominoes)
        l, r = [0]*n, []
        flag = 0
        for i, ch in enumerate(dominoes):
            if ch == 'R':
                flag = n
            elif ch == 'L':
                flag = 0
            else:
                flag = max(flag - 1, 0)
            r.append(flag)
        flag = 0
        for i, ch in enumerate(dominoes[::-1]):
            if ch == 'L':
                flag = -n
            elif ch == 'R':
                flag = 0
            else:
                flag = min(flag + 1, 0)
            l[n-i-1]=flag
        ans = []
        for i in range(n):
            a='.' if l[i]+r[i]==0 else 'L' if l[i]+r[i]<0 else 'R'
            ans.append(a)
        return ''.join(ans)


Solution().pushDominoes(".L.R...LR..L..")
