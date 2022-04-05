#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 给你二叉树的根节点 root 和一个整数 distance 。
#
#  如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。
#
#  返回树中 好叶子节点对的数量 。
#
#
#
#  示例 1：
#
#
#
#
#
#  输入：root = [1,2,3,null,4], distance = 3
# 输出：1
# 解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。
#
#
#  示例 2：
#
#
#
#  输入：root = [1,2,3,4,5,6,7], distance = 3
# 输出：2
# 解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。
#
#
#  示例 3：
#
#  输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# 输出：1
# 解释：唯一的好叶子节点对是 [2,5] 。
#
#
#  示例 4：
#
#  输入：root = [100], distance = 1
# 输出：0
#
#
#  示例 5：
#
#  输入：root = [1,1,1], distance = 2
# 输出：1
#
#
#
#
#  提示：
#
#
#  tree 的节点数在 [1, 2^10] 范围内。
#  每个节点的值都在 [1, 100] 之间。
#  1 <= distance <= 10
#
#  Related Topics 树 深度优先搜索 二叉树
#  👍 93 👎 0


# Definition for a binary tree node.
import bisect


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0

        def cal(A, B):
            A, B = sorted(A), sorted(B)
            ans = 0
            for a in A:
                b = distance - a
                index = bisect.bisect_right(B,b)
                if index == 0:
                    break
                ans += index
            return ans

        def rec(node):
            if not node.left and not node.right:
                return [0]
            if not node.left:
                rs = rec(node.right)
                return [*map(lambda x: x + 1, rs)]
            elif not node.right:
                ls = rec(node.left)
                return [*map(lambda x: x + 1, ls)]
            else:
                ls = rec(node.left)
                rs = rec(node.right)
                ls, rs = [*map(lambda x: x + 1, ls)], [*map(lambda x: x + 1, rs)]
                self.res += cal(ls, rs)
                return ls + rs

        rec(root)
        return self.res


from leetcode.trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[1,2,3,4,5,6,7]')
Solution().countPairs(a, 3)
