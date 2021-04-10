'''一个N x N的网格(grid) 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：

0 表示这个格子是空的，所以你可以穿过它。
1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
-1 表示这个格子里有荆棘，挡着你的路。
你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：

从位置 (0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。
示例 1:

输入: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
输出: 5
解释：
玩家从（0,0）点出发，经过了向下走，向下走，向右走，向右走，到达了点(2, 2)。
在这趟单程中，总共摘到了4颗樱桃，矩阵变成了[[0,1,-1],[0,0,-1],[0,0,0]]。
接着，这名玩家向左走，向上走，向上走，向左走，返回了起始点，又摘到了1颗樱桃。
在旅程中，总共摘到了5颗樱桃，这是可以摘到的最大值了。
说明:

grid 是一个 N * N 的二维数组，N的取值范围是1 <= N <= 50。
每一个 grid[i][j] 都是集合 {-1, 0, 1}其中的一个数。
可以保证起点 grid[0][0] 和终点 grid[N-1][N-1] 的值都不会是 -1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cherry-pickup
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# 1二次动态规划 自顶向下
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0 or grid[-1][-1] == -1:
            return -1
        m = {}
        N = len(grid)

        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if r1 > N - 1 or c1 > N - 1 or c2 > N - 1 or r2 > N - 1 or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')
            if (r1, c1, c2) in m:
                return m[(r1, c1, c2)]
            if (r1, c1, c2) == (N - 1, N - 1, N - 1):
                return grid[N - 1][N - 1]
            val = grid[r1][c1]
            if c1 != c2: val += grid[r1 + c1 - c2][c2]
            m[(r1, c1, c2)] = val + max(dp(r1 + 1, c1, c2), dp(r1, c1 + 1, c2 + 1), dp(r1 + 1, c1, c2 + 1), dp(r1, c1 + 1, c2))  # 分别对应下下，右右，下右，右下
            return m[(r1, c1, c2)]

        return max(0, dp(0, 0, 0))


# 2动态规划 自底向上
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0 or grid[-1][-1] == -1 or grid[0][0] == -1:
            return -1
        N = len(grid)
        dp = [[float('-inf')] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2 * N - 1):  # t代表r+c总数,i,j分别代表c1,c2
            dp2=[[float('-inf')] * N for _ in range(N)]
            for i in range(max(t - (N - 1), 0), min(N, t+1)):  # 当t超过n-1，i最少为t-(N-1)，当i最大为N-1和t的最大值
                for j in range(i, min(N, t+1)):  # 设置c2总是大于或等于c1，因为每次只能走一步，所以这样是可行的，c1和c2是对称的哪个为c1或哪个为c2都可以
                    if grid[t - i][i] == -1 or grid[t - j][j] == -1:
                        continue
                    val = grid[t - i][i]
                    if i != j:
                        val += grid[t - j][j]
                    dp2[i][j] = val + max(dp[r][c] for r in (i, i - 1) for c in (j, j - 1) if r >= 0 and c >= 0)
            dp = dp2 #这里不用copy，因为dp2在下一个循环重新赋值了，如果只改变列表中某一个值是需要copy的
        return max(0,dp[-1][-1])


Solution().cherryPickup([[1,1,-1],[1,-1,1],[-1,1,1]])
