'''你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个 m x n 的矩阵表示， 在这个矩阵中：

0 表示障碍，无法触碰
1 表示地面，可以行走
比 1 大的数 表示有树的单元格，可以行走，数值表示树的高度
每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。

你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 1（即变为地面）。

你将从 (0, 0) 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 -1 。

可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

 

示例 1：


输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
示例 2：


输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。
示例 3：

输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。
 

提示：

m == forest.length
n == forest[i].length
1 <= m, n <= 50
0 <= forest[i][j] <= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cut-off-trees-for-golf-event
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# https://leetcode-cn.com/problems/cut-off-trees-for-golf-event/solution/wei-gao-er-fu-bi-sai-kan-shu-by-leetcode/
# 1bfs 广度优先搜索 宽度优先搜索
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def dis(sr, sc, tr, tc):
            if (sr, sc) == (tr, tc):
                return 0
            m = [(sr, sc)]
            M = {(sr, sc)}
            cnt = 0
            while True:
                t = []
                cnt += 1
                for r, c in m:
                    for i, j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                        if 0 <= i < R and 0 <= j < C and forest[i][j] > 0 and (i, j) not in M:
                            if (i, j) == (tr, tc):
                                return cnt
                            M.add((i, j))
                            t.append((i, j))
                if not t:
                    break
                m = t
            return -1

        if not forest or len(forest[0]) == 0:
            return 0
        R, C = len(forest), len(forest[0])
        a = sorted([(r, c) for r in range(R) for c in range(C) if forest[r][c] > 1], key=lambda x: forest[x[0]][x[1]])
        sr, sc = 0, 0
        step = 0
        for tr, tc in a:
            d = dis(sr, sc, tr, tc)
            if d == -1:
                return -1
            step += d
            sr, sc = tr, tc
        return step


# 2A*搜索
import heapq


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def astar(sr, sc, tr, tc):
            if (sr, sc) == (tr, tc):
                return 0
            a = []
            dis = abs(tr - sr) + abs(tc - sc)
            heapq.heappush(a, [dis, 0, sr, sc])
            m = {(sr, sc): dis}
            while a:
                h, g, r, c = heapq.heappop(a)
                for i, j in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                    if 0 <= i < R and 0 <= j < C and forest[i][j] > 0:
                        cost = g + 1 + abs(tr - i) + abs(tc - j)  # abs(tr - i) + abs(tc - j)这个表示后续的最短距离
                        if (i, j) == (tr, tc):
                            return cost
                        if cost < m.get((i, j), 9999):
                            m[(i, j)] = cost
                            heapq.heappush(a, (cost, g + 1, i, j))
            return -1

        if not forest or len(forest[0]) == 0:
            return 0
        R, C = len(forest), len(forest[0])
        a = sorted([(r, c) for r in range(R) for c in range(C) if forest[r][c] > 1], key=lambda x: forest[x[0]][x[1]])
        sr, sc = 0, 0
        step = 0
        for tr, tc in a:
            d = astar(sr, sc, tr, tc)
            if d == -1:
                return -1
            step += d
            sr, sc = tr, tc
        return step


# 3Hadlock算法 迂回节点
import collections


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        def hadlock(sr, sc, tr, tc):
            if (sr, sc) == (tr, tc):
                return 0
            a = collections.deque([(sr, sc, 0)])
            m = set()
            while a:
                r, c, detours = a.popleft()
                if (r, c) not in m:
                    m.add((r, c))
                    for i, j, closer in [(r + 1, c, tr > r), (r - 1, c, tr < r), (r, c + 1, tc > c), (r, c - 1, tc < c)]:
                        if 0 <= i < R and 0 <= j < C and forest[i][j] > 0 and (i, j) not in m:
                            if (i, j) == (tr, tc):
                                return abs(tr - sr) + abs(tc - sc) + 2 * detours
                            if closer:
                                a.appendleft((i, j, detours))
                            else:
                                a.append((i, j, detours + 1))
            return -1

        if not forest or len(forest[0]) == 0:
            return 0
        R, C = len(forest), len(forest[0])
        a = sorted([(r, c) for r in range(R) for c in range(C) if forest[r][c] > 1], key=lambda x: forest[x[0]][x[1]])
        sr, sc = 0, 0
        step = 0
        for tr, tc in a:
            d = hadlock(sr, sc, tr, tc)
            if d == -1:
                return -1
            step += d
            sr, sc = tr, tc
        return step


Solution().cutOffTree([[1, 3, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1], [1, 1, 1, 1, 0, 1], [1, 1, 0, 1, 0, 0], [1, 1, 4, 1, 2, 1]])
