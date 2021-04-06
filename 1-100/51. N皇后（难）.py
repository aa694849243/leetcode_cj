'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

示例:

输入: 4
输出: [
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
解释: 4 皇后问题存在两个不同的解法。
 

提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一到七步，可进可退。（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

#回溯--caojie-11%-
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        ans = ['.' * n for _ in range(n)]

        def could_place(i, j, ans):
            if 'Q' not in ans[i][:] and 'Q' not in [ans[k][j] for k in range(n)]:
                j1, j2, j3, j4 = j, j, j, j
                i1, i2, i3, i4 = i, i, i, i
                while j1 + 1 < n and i1 + 1 < n:
                    if ans[i1 + 1][j1 + 1] == 'Q':
                        return
                    i1 += 1
                    j1 += 1
                while j2 + 1 < n and i2 - 1 >= 0:
                    if ans[i2 - 1][j2 + 1] == 'Q':
                        return
                    j2 += 1
                    i2 -= 1
                while j3 - 1 >= 0 and i3 + 1 < n:
                    if ans[i3 + 1][j3 - 1] == 'Q':
                        return
                    j3 -= 1
                    i3 += 1
                while j4 - 1 >= 0 and i4 - 1 >= 0:
                    if ans[i4 - 1][j4 - 1] == 'Q':
                        return
                    j4 -= 1
                    i4 -= 1
                return True

        def place_Q(i, j, ans):
            ans[i] = ans[i][:j] + 'Q' + ans[i][j + 1:]
            return ans.copy()

        def place_next_Q(i, ans):
            if i == n - 1:
                res.append(ans)
            else:
                backtrack(i + 1, ans.copy())

        def backtrack(i, ans):
            for j in range(n):
                if could_place(i, j, ans):
                    place_next_Q(i, place_Q(i, j, ans.copy()))

        backtrack(0, ans)
        return res

# 官方写的更精巧
# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / n - queens / solution / nhuang - hou - by - leetcode /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row=0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output



Solution().solveNQueens(4)
