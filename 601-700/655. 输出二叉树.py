'''在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：

行数 m 应当等于给定二叉树的高度。
列数 n 应当总是奇数。
根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（左下部分和右下部分）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
每个未使用的空间应包含一个空的字符串""。
使用相同的规则输出子树。
示例 1:

输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]
示例 2:

输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
示例 3:

输入:
      1
     / \
    2   5
   /
  3
 /
4
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
注意: 二叉树的高度在范围 [1, 10] 中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/print-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 1递归
class Solution:
    mlevel = 0

    def printTree(self, root: TreeNode) -> List[List[str]]:

        def curlevel(node, level):
            if not node:
                return
            level += 1
            self.mlevel = max(level, self.mlevel)
            curlevel(node.left, level)
            curlevel(node.right, level)

        curlevel(root, 0)
        m = [[''] * (2 ** self.mlevel - 1) for _ in range(self.mlevel)]

        def fill(node, level, l, r):
            if not node:
                return
            m[level][(l + r) // 2] = str(node.val)
            fill(node.left, level + 1, l, (l + r) // 2)
            fill(node.right, level + 1, (l + r) // 2 + 1, r)

        fill(root, 0, 0, 2 ** self.mlevel - 1)
        return m


# 2队列
class Params:
    def __init__(self, node, i, l, r):
        self.node = node
        self.i = i
        self.l = l
        self.r = r


import collections


class Solution:
    mlevel = 0

    def printTree(self, root: TreeNode) -> List[List[str]]:
        def curlevel(node, level):
            if not node:
                return
            level += 1
            self.mlevel = max(level, self.mlevel)
            curlevel(node.left, level)
            curlevel(node.right, level)

        curlevel(root, 0)
        m = [[''] * (2 ** self.mlevel - 1) for _ in range(self.mlevel)]
        q = collections.deque()
        p = Params(root, 0, 0, 2 ** self.mlevel - 1)
        q.append(p)
        while q:
            p = q.popleft()
            m[p.i][(p.l + p.r) // 2] = str(p.node.val)
            if p.node.left:
                q.append(Params(p.node.left, p.i + 1, p.l, (p.l + p.r) // 2))
            if p.node.right:
                q.append(Params(p.node.right, p.i + 1, (p.l + p.r) // 2 + 1, p.r))
        return m
