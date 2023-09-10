# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
#
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。
#
#
#
#  示例 1：
#
#
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f",
# "l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
#  示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n == board[i].length
#  1 <= m, n <= 12
#  board[i][j] 是一个小写英文字母
#  1 <= words.length <= 3 * 10⁴
#  1 <= words[i].length <= 10
#  words[i] 由小写英文字母组成
#  words 中的所有字符串互不相同
#
#
#  Related Topics 字典树 数组 字符串 回溯 矩阵
#  👍 783 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Trie:
    def __init__(self):
        self.f = {}

    def insert(self, word):
        cur = self.f
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = word

    def search(self, word):
        cur = self.f
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

from typing import List
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        trie = Trie()
        for word in words:
            trie.insert(word)
        self.res = []

        def dfs(r, c, cur):
            ch = board[r][c]
            if '#' in cur[ch]:
                self.res.append(cur[ch].pop('#'))
            for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= nr < R and 0 <= nc < C and board[nr][nc] in cur[ch]:
                    board[r][c] = 0
                    dfs(nr, nc, cur[ch])
                    board[r][c] = ch
            if not cur[ch]:  # 剪枝，删去没有后代的节点
                cur.pop(ch)

        cur = trie.f
        for r in range(R):
            for c in range(C):
                if board[r][c] in cur:
                    dfs(r, c, cur)
        return self.res


# leetcode submit region end(Prohibit modification and deletion)
print(
    Solution().findWords(
        [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        ["oath", "pea", "eat", "rain"])
)
