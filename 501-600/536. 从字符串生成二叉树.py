#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 你需要从一个包括括号和整数的字符串构建一棵二叉树。
#
#  输入的字符串代表一棵二叉树。它包括整数和随后的 0 ，1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。
#
#  若存在左子结点，则从左子结点开始构建。
#
#
#
#  示例：
#
#  输入："4(2(3)(1))(6(5))"
# 输出：返回代表下列二叉树的根节点:
#
#        4
#      /   \
#     2     6
#    / \   /
#   3   1 5
#
#
#
#
#  提示：
#
#
#  输入字符串中只包含 '(', ')', '-' 和 '0' ~ '9'
#  空树由 "" 而非"()"表示。
#
#
#
#  Related Topics 树 深度优先搜索 字符串 二叉树
#  👍 74 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def dfs(word):
            if not word:
                return None
            if '(' not in word:
                return TreeNode(int(word))
            ind = word.index('(')
            node = TreeNode(int(word[:ind]))
            bal = 0
            l,r=None,None
            for i in range(ind, len(word)):
                if word[i] == '(':
                    bal += 1
                elif word[i] == ')':
                    bal -= 1
                if bal == 0:
                    l = dfs(word[ind + 1:i])
                    rind = i
                    break
            if rind + 1 < len(word):
                if word[rind + 1] == '(':
                    r = dfs(word[rind + 2:-1])
                else:
                    r = dfs(word[rind + 1:])
            node.left=l
            node.right=r
            return  node
        return dfs(s)
