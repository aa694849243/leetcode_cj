# -*- coding: utf-8 -*-


# 我们从一块字母板上的位置 (0, 0) 出发，该坐标对应的字符为 board[0][0]。
#
#  在本题里，字母板为board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]，如下所示。
#
#
#
#  我们可以按下面的指令规则行动：
#
#
#  如果方格存在，'U' 意味着将我们的位置上移一行；
#  如果方格存在，'D' 意味着将我们的位置下移一行；
#  如果方格存在，'L' 意味着将我们的位置左移一列；
#  如果方格存在，'R' 意味着将我们的位置右移一列；
#  '!' 会把在我们当前位置 (r, c) 的字符 board[r][c] 添加到答案中。
#
#
#  （注意，字母板上只存在有字母的位置。）
#
#  返回指令序列，用最小的行动次数让答案和目标 target 相同。你可以返回任何达成目标的路径。
#
#
#
#  示例 1：
#
#  输入：target = "leet"
# 输出："DDR!UURRR!!DDD!"
#
#
#  示例 2：
#
#  输入：target = "code"
# 输出："RR!DDRR!UUL!R!"
#
#
#
#
#  提示：
#
#
#  1 <= target.length <= 100
#  target 仅含有小写英文字母。
#
#  Related Topics 哈希表 字符串
#  👍 31 👎 0


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        dirs = [(0, 1, 'R'), (0, -1, 'L'), (-1, 0, 'U'), (1, 0, 'D')]
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        def alphaval(ch):
            return (ord(ch) - 97) // 5, (ord(ch) - 97) % 5

        def cal(sr, sc, tch):
            # sch=alphaval(sr,sc)
            if board[sr][sc]==tch:
                return '!'
            t = [(sr, sc, '')]
            while True:
                tree = []
                seen = set()
                for r, c, route in t:
                    for dr, dc, ch in dirs:
                        nr, nc = r + dr, c + dc
                        if nr * 5 + nc < 26 and 0 <= nr < 6 and 0 <= nc < 5 and (nr, nc) not in seen:
                            tree.append((nr, nc, route + ch))
                            seen.add((nr,nc))
                            if board[nr][nc] == tch:
                                return route + ch + '!'
                t=tree
        ans = ''
        sr, sc = 0, 0
        for ch in target:
            ans += cal(sr, sc, ch)
            sr, sc = alphaval(ch)
        return ans
Solution().alphabetBoardPath("leet")