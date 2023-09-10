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
class Solution:  # 剪枝条件，dfs
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s):
            # 消除桌面上需要消除的球
            n = 1
            while n:
                s, n = re.subn(r"(.)\1{2,}", "", s)
            return s

        m = collections.defaultdict(lambda: 6)
        cnts = collections.Counter(hand)
        cs = set(cnts)
        board = clean(board)
        m[board] = 0

        def dfs(s):
            if not s:
                return
            for i in range(len(s) + 1):
                for c in cs:  # 剪枝1：相同的球只插一次
                    if cnts[c] > 0:
                        if i > 0 and s[i - 1] == c:  # 剪枝2：插入位点左边相同颜色的球跳过，因为，将插入位点左偏一格结果是相同的
                            continue
                        if i > 0 and i < len(s) and s[i - 1] != s[i] != c:  # 剪枝3： 插入位点与左右两侧的球颜色都不同，这是没有意义的，因为既不能消除，也不能隔断，这样先插入颜色与两侧任意侧相同颜色球的结果不会改变
                            continue
                        cnts[c] -= 1
                        tmp = clean(s[:i] + c + s[i:])
                        if m[tmp] > m[s] + 1:
                            m[tmp] = m[s] + 1
                            if m[tmp] + 1 < m['']:
                                dfs(tmp)
                        cnts[c] += 1

        dfs(board)
        return m[''] if m[''] < 6 else -1
Solution().findMinStep("WWRRBBWW", "WRBRW")