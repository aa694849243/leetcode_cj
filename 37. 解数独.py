# 编写一个程序，通过填充空格来解决数独问题。
#
#  数独的解法需 遵循如下规则：
#
#
#  数字 1-9 在每一行只能出现一次。
#  数字 1-9 在每一列只能出现一次。
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
#
#
#  数独部分空格内已填入了数字，空白格用 '.' 表示。
#
#
#
#
#
#
#  示例：
#
#
# 输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5","."
# ,".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".","."
# ,"3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"
# ],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],["
# .",".",".",".","8",".",".","7","9"]]
# 输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"
# ],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["
# 4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","
# 6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","
# 5","2","8","6","1","7","9"]]
# 解释：输入的数独如上图所示，唯一有效的解决方案如下所示：
#
#
#
#
#
#
#  提示：
#
#
#  board.length == 9
#  board[i].length == 9
#  board[i][j] 是一位数字或者 '.'
#  题目数据 保证 输入数独仅有一个解
#
#
#
#
#  Related Topics 哈希表 回溯算法
#  👍 817 👎 0


from typing import List


# 回溯
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = [[0] * 9 for _ in range(9)]
        C = [[0] * 9 for _ in range(9)]
        Sub = [[0] * 9 for _ in range(9)]

        def dfs(index):
            if index == 81:
                return True
            i, j = index // 9, index % 9
            x, y = i // 3, j // 3
            if board[i][j] != '.':
                return dfs(index + 1)
            else:
                for k in range(1, 10):
                    if not R[i][k - 1] and not C[j][k - 1] and not Sub[x * 3 + y][k - 1]:
                        board[i][j] = str(k)
                        R[i][k - 1] = 1
                        C[j][k - 1] = 1
                        Sub[x * 3 + y][k - 1] = 1
                        self.cnt += 1
                        if dfs(index + 1):
                            return True
                        board[i][j] = '.'
                        R[i][k - 1] = 0
                        C[j][k - 1] = 0
                        Sub[x * 3 + y][k - 1] = 0
            return False

        for index in range(81):
            i, j = index // 9, index % 9
            x, y = i // 3, j // 3
            if board[i][j] != '.':
                num = int(board[i][j])
                R[i][num - 1] = 1
                C[j][num - 1] = 1
                Sub[x * 3 + y][num - 1] = 1
        dfs(0)
        return


# 2位操作
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        R = [0] * 9
        C = [0] * 9
        box = [0] * 9

        def flip(i, j, num):  # num最高为8
            R[i] ^= (1 << num)
            C[j] ^= (1 << num)
            x, y = i // 3, j // 3
            box[x * 3 + y] ^= (1 << num)

        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):
                valid = True
                return
            i, j = spaces[pos]
            mask = ~(R[i] | C[j] | box[(i // 3) * 3 + j // 3]) & 0x1ff
            while mask:
                bitmask = mask & (-mask)
                p = bin(bitmask).count('0') - 1
                flip(i, j, p)
                board[i][j] = str(p + 1)  # 这里的board[i][j]不用还原，因为记住了位置，每次在相应位置处直接修改
                dfs(pos + 1)
                mask &= (mask - 1)
                flip(i, j, p)
                if valid:
                    return

        spaces = []
        for index in range(81):
            i, j = index // 9, index % 9
            if board[i][j] != '.':
                flip(i, j, int(board[i][j]) - 1)
        while True:
            modified = False
            for index in range(81):
                i, j = index // 9, index % 9
                if board[i][j] == '.':
                    mask = ~(R[i] | C[j] | box[(i // 3) * 3 + j // 3]) & 0x1ff
                    if bin(mask).count('1') == 1:  # 只有1个1
                        digit = bin(mask).count('0') - 1
                        flip(i, j, digit)
                        board[i][j] = str(digit + 1)
                        modified = True
            if not modified:
                break
        for index in range(81):
            i, j = index // 9, index % 9
            if board[i][j] == '.':
                spaces.append((i, j))
        valid=False
        dfs(0)
        return


Solution().solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
