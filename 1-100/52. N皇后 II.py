'''
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。



上图为 8 皇后问题的一种解法。

给定一个整数 n，返回 n 皇后不同的解决方案的数量。

示例:

输入: 4
输出: 2
解释: 4 皇后问题存在如下两个不同的解法。
[
 [".Q..",  // 解法 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // 解法 2
  "Q...",
  "...Q",
  ".Q.."]
]
 

提示：

皇后，是国际象棋中的棋子，意味着国王的妻子。皇后只做一件事，那就是“吃子”。当她遇见可以吃的棋子时，就迅速冲上去吃掉棋子。当然，她横、竖、斜都可走一或七步，可进可退。（引用自 百度百科 - 皇后 ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-queens-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def totalNQueens(self, n: int) -> int:
        def could_place(row, col):
            return not cols[col] and col + row not in m_diagonal and col - row not in p_diagonal

        def place(row, col):
            cols[col] += 1
            m_diagonal.add((col + row))
            p_diagonal.add((col - row))

        def remove(row, col):
            cols[col] = 0
            m_diagonal.remove(col + row)
            p_diagonal.remove(col - row)

        def backtrack(row):
            for col in range(n):
                if could_place(row, col):
                    place(row, col)
                    if row + 1 == n:
                        self.count += 1
                    else:
                        backtrack(row + 1)
                    remove(row, col)

        self.count = 0
        cols = [0] * n
        m_diagonal = set()
        p_diagonal = set()
        backtrack(0)
        return self.count


class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(r, c, diag1, diag2):
            if r == n:
                return 1
            status = ((1 << n) - 1) & (~(c | diag1 | diag2))
            ans = 0
            while status:
                p = status & (-status)
                status &= (status - 1)
                ans += dfs(r + 1, c | p, (diag1 | p) << 1, (diag2 | p) >> 1)
            return ans

        return dfs(0, 0, 0, 0)


Solution().totalNQueens(5)
