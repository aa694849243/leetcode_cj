'''回忆一下祖玛游戏。现在桌上有一串球，颜色有红色(R)，黄色(Y)，蓝色(B)，绿色(G)，还有白色(W)。 现在你手里也有几个球。

每一次，你可以从手里的球选一个，然后把这个球插入到一串球中的某个位置上（包括最左端，最右端）。接着，如果有出现三个或者三个以上颜色相同的球相连的话，就把它们移除掉。重复这一步骤直到桌上所有的球都被移除。

找到插入并可以移除掉桌上所有球所需的最少的球数。如果不能移除桌上所有的球，输出 -1 。

 

示例 1：

输入：board = "WRRBBW", hand = "RB"
输出：-1
解释：WRRBBW -> WRR[R]BBW -> WBBW -> WBB[B]W -> WW
示例 2：

输入：board = "WWRRBBWW", hand = "WRBRW"
输出：2
解释：WWRRBBWW -> WWRR[R]BBWW -> WWBBWW -> WWBB[B]WW -> WWWW -> empty
示例 3：

输入：board = "G", hand = "GGGGG"
输出：2
解释：G -> G[G] -> GG[G] -> empty
示例 4：

输入：board = "RBYYBBRRB", hand = "YRBGB"
输出：3
解释：RBYYBBRRB -> RBYY[Y]BBRRB -> RBBBRRB -> RRRB -> B -> B[B] -> BB[B] -> empty
 

提示：

你可以假设桌上一开始的球中，不会有三个及三个以上颜色相同且连着的球。
1 <= board.length <= 16
1 <= hand.length <= 5
输入的两个字符串均为非空字符串，且只包含字符 'R','Y','B','G','W'。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zuma-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# 1深度优先搜索 dfs
# https://leetcode-cn.com/problems/zuma-game/solution/bao-li-ye-yao-you-ya-by-carudy/
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def simplified(s):
            if len(s) < 3:
                return s
            for i in range(len(s)):
                j = i
                while j < len(s) and s[i] == s[j]: j += 1
                if j - i >= 3: return simplified(s[:i] + s[j:])
            return s

        import collections
        m = collections.defaultdict(lambda: 6)
        c = collections.Counter(hand)
        m[board]=0
        def dfs(s):
            if not s:
                return ''
            for i in range(len(s) + 1):
                for ch in 'RYBGW':
                    if c[ch] > 0:
                        c[ch] -= 1
                        new = simplified(s[:i] + ch + s[i:])
                        if m[new] > m[s] + 1:
                            m[new] = m[s] + 1
                            if m[new] < 5:
                                dfs(new)
                        c[ch] += 1
        dfs(board)
        return m[''] if m['']<6 else -1
Solution().findMinStep("WWRRBBWW", "WRBRW")