'''
编写一个程序，通过已填充的空格来解决数独问题。

一个数独的解法需遵循如下规则：

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
空白格用 '.' 表示。



一个数独。



答案被标成红色。

Note:

给定的数独序列只包含数字 1-9 和字符 '.' 。
你可以假设给定的数独只有唯一解。
给定数独永远是 9x9 形式的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sudoku-solver
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# ------------回溯法---参考答案------------------------------------------------------------------------------------------
#---https://leetcode-cn.com/problems/sudoku-solver/solution/jie-shu-du-by-leetcode/
class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import defaultdict
        def could_place(d, row, col):
            return not (d in (rows[row], cols[col], boxes[box_index(row, col)]))

        def place_number(d, row, col):
            rows[row][d] += 1
            cols[col][d] += 1
            boxes[box_index(row, col)][d] += 1
            board[row][col] = str(d)

        def place_next_number(row, col):
            if row == 8 and col == 8:
                nonlocal sudoku_soloved
                sudoku_soloved= True
            elif col == 8:
                backtrack(row + 1, 0)
            else:
                backtrack(row, col + 1)

        def remove_number(d, row, col):
            del rows[row][d]
            del cols[col][d]
            del boxes[box_index(row, col)][d]
            board[row][col] = '.'

        def backtrack(row=0, col=0):
            if board[row][col] == '.':
                for d in range(1, 10):
                    if could_place(d, row, col):
                        place_number(d, row, col)
                        place_next_number(row, col)
                        if not sudoku_solved:
                            remove_number(d,row,col)
                    else:
                        place_next_number(row,col)

        rows = [defaultdict(int) for _ in range(9)]
        cols = [defaultdict(int) for _ in range(9)]
        boxes = [defaultdict(int) for _ in range(9)]
        box_index = lambda row, col: (row // 3) * 3 + col // 3
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    rows[row][int(board[row][col])] += 1
                    cols[col][int(board[row][col])] += 1
                    boxes[box_index(row, col)][int(board[row][col])] += 1
