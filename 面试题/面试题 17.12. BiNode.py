#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉
# 搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。
#
#  返回转换后的单向链表的头节点。
#
#  注意：本题相对原题稍作改动
#
#
#
#  示例：
#
#  输入： [4,2,5,1,3,null,6,0]
# 输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
#
#
#  提示：
#
#
#  节点数量不会超过 100000。
#
#  Related Topics 栈 树 深度优先搜索 二叉搜索树 链表 二叉树
#  👍 79 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        h = TreeNode(-1)
        self.cur = h

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            node.left = None
            self.cur.right = node
            cur = node
            dfs(node.right)

        dfs(root)
        return h.right


# 迭代 栈方法
class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        stack = []
        h = TreeNode(-1)
        cur = h
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            root.left = None
            cur.right = root
            cur = root
            root = root.right
        return h.right
