'''
给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

示例:

输入:
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

输出: ["eat","oath"]
说明:
你可以假设所有输入都由小写字母 a-z 组成。

提示:

你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-search-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List


# 回溯法 backtrack
class Solution:
    def __init__(self):
        self.look = {}
        self.ans = []

    def addword(self, word):
        tree = self.look
        for i in word:
            tree.setdefault(i, {})
            tree = tree[i]
        tree['#'] = word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        cols, rows = len(board[0]), len(board)
        for word in words:
            self.addword(word)

        def backtrack(i, j, parent):

            lttr = board[i][j]
            currNode = parent[lttr]
            if '#' in currNode:
                self.ans.append(currNode.pop('#'))
            board[i][j] = 0
            for d1, d2 in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + d1 < rows and 0 <= j + d2 < cols and board[i + d1][j + d2] in currNode:
                    backtrack(i + d1, j + d2, parent[lttr])
            board[i][j] = lttr
            # 剪枝，如果currNode为单词终点，且没有孩子节点了，则可以把该节点剪掉
            if not currNode:
                parent.pop(lttr)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] in self.look:
                    backtrack(i, j, self.look)

        return self.ans


words = ["ab"]
board =[["a","b"]]

Solution().findWords(board, words)
