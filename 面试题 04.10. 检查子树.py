#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。
#
#  如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。
#
#  注意：此题相对书上原题略有改动。
#
#  示例1:
#
#
#  输入：t1 = [1, 2, 3], t2 = [2]
#  输出：true
#
#
#  示例2:
#
#
#  输入：t1 = [1, null, 2, 4], t2 = [3, 2]
#  输出：false
#
#
#  提示：
#
#
#  树的节点数目范围为[0, 20000]。
#
#  Related Topics 树 深度优先搜索 二叉树 字符串匹配 哈希函数
#  👍 41 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def dfs1(node1, node2):
            if not node1 or not node2:
                return not node1 and not node2
            if node1.val != node2.val:
                return False
            l = dfs1(node1.left,node2.left)
            r = dfs1(node1.right,node2.right)
            return l and r
        def dfs2(node1,node2):
            if not node1:
                return not node2
            return dfs1(node1,node2) or dfs2(node1.left,node2) or dfs2(node1.right,node2)
        return dfs2(t1,t2)
