'''在一个 2 x 3 的板上（board）有 5 块砖瓦，用数字 1~5 来表示, 以及一块空缺用 0 来表示.

一次移动定义为选择 0 与一个相邻的数字（上下左右）进行交换.

最终当板 board 的结果是 [[1,2,3],[4,5,0]] 谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

示例：

输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成
输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板
输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]
输入：board = [[3,2,4],[1,5,0]]
输出：14
提示：

board 是一个如上所述的 2 x 3 的数组.
board[i][j] 是一个 [0, 1, 2, 3, 4, 5] 的排列.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sliding-puzzle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List
import itertools
import collections


# bfs
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = tuple(itertools.chain(*board))
        zero = start.index(0)
        R, C = 2, 3
        target = tuple(list(range(1, 6)) + [0])
        m = {start}
        t = [(start, zero)]
        step = 0
        while t:
            tree = []
            for node, o in t:
                if node == target:
                    return step
                for change in (1, -1, C, -C):
                    if abs((o + change) // C - o // C) + abs((o + change) % C - o % C) != 1:
                        continue
                    if 0 <= o + change < 6:
                        li = list(node)
                        li[o], li[o + change] = li[o + change], li[o]
                        if tuple(li) == target:
                            return step + 1
                        if tuple(li) in m:
                            continue
                        m.add(tuple(li))
                        tree.append((tuple(li), o + change))
            if not tree:
                break
            step += 1
            t = tree
        return -1


# A*搜索
import heapq


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        R, C = 2, 3
        start = tuple(itertools.chain(*board))
        o = start.index(0)
        target = tuple(list(range(1, 6)) + [0])
        wrong = tuple([1, 2, 3, 5, 4, 0])
        q = [(0, 0, start, o)]
        expected = {(r * C + c + 1) % (R * C): (r, c) for r in range(R) for c in range(C)}

        def heuristic(board):
            ans = 0
            for i in range(R):
                for j in range(C):
                    val = board[i * C + j]
                    if val == 0:
                        continue
                    nr, nc = expected[val]
                    dis = abs(nr - i) + abs(nc - j)
                    ans += dis
            return ans

        m = {start: heuristic(start)}
        while q:
            cost, g, pos, o = heapq.heappop(q)
            if pos == target:
                return cost
            elif pos == wrong:
                return -1
            for move in (1, -1, C, -C):
                if abs((o + move) // C - o // C) + abs((o + move) % C - o % C) != 1:
                    continue
                if 0 <= o + move < 6:
                    li = list(pos)
                    li[o], li[o + move] = li[o + move], li[o]
                    ncost = g + 1 + heuristic(tuple(li))
                    if ncost < m.get(tuple(li), float('inf')):
                        m[tuple] = ncost
                        heapq.heappush(q, (ncost, g + 1, tuple(li), o + move))
        return -1


# class Solution(object):
#     def slidingPuzzle(self, board):
#         R, C = len(board), len(board[0])
#         start = tuple(itertools.chain(*board))
#         target = tuple(list(range(1, R * C)) + [0])
#         target_wrong = tuple([1, 2, 3, 5, 4, 0])
#         pq = [(0, 0, start, start.index(0))]
#
#
#         expected = {(C * r + c + 1) % (R * C): (r, c)
#                     for r in range(R) for c in range(C)}
#
#         def heuristic(board):
#             ans = 0
#             for r in range(R):
#                 for c in range(C):
#                     val = board[C * r + c]
#                     if val == 0: continue
#                     er, ec = expected[val]
#                     ans += abs(r - er) + abs(c - ec)
#             return ans
#         cost={start:heuristic(start)}
#         while pq:
#             # f = estimated distance (priority)
#             # g = actual distance travelled (depth)
#             f, g, board, zero = heapq.heappop(pq)
#             if board == target: return g
#             if board == target_wrong: return -1
#             if f > cost[board]: continue
#
#             for delta in (-1, 1, -C, C):
#                 nei = zero + delta
#                 if abs(zero / C - nei / C) + abs(zero % C - nei % C) != 1:
#                     continue
#                 if 0 <= nei < R * C:
#                     board2 = list(board)
#                     board2[zero], board2[nei] = board2[nei], board2[zero]
#                     board2t = tuple(board2)
#                     ncost = g + 1 + heuristic(board2t)
#                     if ncost < cost.get(board2t, float('inf')):
#                         cost[board2t] = ncost
#                         heapq.heappush(pq, (ncost, g + 1, board2t, nei))
#
#         return -1


Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]])
