'''在一个大小在 (0, 0) 到 (N-1, N-1) 的2D网格 grid 中，除了在 mines 中给出的单元为 0，其他每个单元都是 1。网格中包含 1 的最大的轴对齐加号标志是多少阶？返回加号标志的阶数。如果未找到加号标志，则返回 0。

一个 k" 阶由 1 组成的“轴对称”加号标志具有中心网格  grid[x][y] = 1 ，以及4个从中心向上、向下、向左、向右延伸，长度为 k-1，由 1 组成的臂。下面给出 k" 阶“轴对称”加号标志的示例。注意，只有加号标志的所有网格要求为 1，别的网格可能为 0 也可能为 1。

 

k 阶轴对称加号标志示例:

阶 1:
000
010
000

阶 2:
00000
00100
01110
00100
00000

阶 3:
0000000
0001000
0001000
0111110
0001000
0001000
0000000
 

示例 1：

输入: N = 5, mines = [[4, 2]]
输出: 2
解释:

11111
11111
11111
11111
11011

在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。
 

示例 2：

输入: N = 2, mines = []
输出: 1
解释:

11
11

没有 2 阶加号标志，有 1 阶加号标志。
 

示例 3：

输入: N = 1, mines = [[0, 0]]
输出: 0
解释:

0

没有加号标志，返回 0 。
 

提示：

整数N 的范围： [1, 500].
mines 的最大长度为 5000.
mines[i] 是长度为2的由2个 [0, N-1] 中的数组成.
(另外,使用 C, C++, 或者 C# 编程将以稍小的时间限制进行​​判断.)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-plus-sign
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import copy
from leetcode.trick.oth.timefn import timefn


# caojie超时写法 时间复杂度和官方题解是一样的，但是多了几个循环
class Solution:
    @timefn
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        m = [[1] * N for _ in range(N)]
        for i, j in mines:
            m[i][j] = 0
        if N == 1:
            return m[0][0]
        elif N == 2:
            return 1 if any(m[i][j] for i in range(2) for j in range(2)) else 0
        ans = 0
        for i in range(N):
            if m[i][0] == 1:
                ans = 1
                break
        else:
            for j in range(N):
                if m[0][j] == 1:
                    ans = 1
                    break
        for i in range(N):
            for j in range(N):
                m[i][j] = [1, 1] if m[i][j] == 1 else [0, 0]
        mr = copy.deepcopy(m)
        mc = copy.deepcopy(m)
        for i in range(1, N):
            for j in range(N):
                if mr[i][j] != [0, 0]:
                    mr[i][j][0] = mr[i - 1][j][0] + 1
        for i in range(N - 2, -1, -1):
            for j in range(N):
                if mr[i][j] != [0, 0]:
                    mr[i][j][1] = mr[i + 1][j][1] + 1
        for i in range(N):
            for j in range(1, N):
                if mc[i][j] != [0, 0]:
                    mc[i][j][0] = mc[i][j - 1][0] + 1
        for i in range(N):
            for j in range(N - 2, - 1, -1):
                if m[i][j] != [0, 0]:
                    mc[i][j][1] = mc[i][j + 1][1] + 1

        for i in range(1, N - 1):
            for j in range(1, N - 1):
                if m[i][j] != [0, 0]:
                    ans = max(min(min(mr[i + 1][j]), min(mr[i - 1][j]), min(min(mc[i][j - 1]), min(mc[i][j + 1]))) + 1, ans)
        return ans


# 2官方题解
class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        mines = set(tuple(x) for x in mines)
        ans = 0
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            count = 0
            for j in range(N):
                count = 0 if (i, j)  in mines else count+1
                dp[i][j] = count

            count = 0
            for j in range(N-1,-1,-1):
                count = 0 if (i, j)  in mines else count+1
                dp[i][j] = min(count, dp[i][j])
        for j in range(N):
            count = 0
            for i in range(N):
                count = 0 if (i, j) in mines else count+1
                dp[i][j] = min(count,dp[i][j])

            count = 0
            for i in range(N-1,-1,-1):
                count = 0 if (i, j) in mines else count + 1
                dp[i][j] = min(count, dp[i][j])
                ans = max(ans, dp[i][j])
        return ans


