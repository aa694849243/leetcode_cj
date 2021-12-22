# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect

# 给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，并返回该子树的大小。其中，最大指的是子树节点数最多的。
#
#  二叉搜索树（BST）中的所有节点都具备以下属性：
#
#
#
#  左子树的值小于其父（根）节点的值。
#
#
#  右子树的值大于其父（根）节点的值。
#
#
#
#  注意:
#
#
#  子树必须包含其所有后代。
#
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [10,5,15,1,8,null,7]
# 输出：3
# 解释：本例中最大的 BST 子树是高亮显示的子树。返回值是子树的大小，即 3 。
#
#  示例 2：
#
#
# 输入：root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
# 输出：2
#
#
#
#
#  提示：
#
#
#  树上节点数目的范围是 [0, 10⁴]
#  -10⁴ <= Node.val <= 10⁴
#
#
#
#
#  进阶: 你能想出 O(n) 时间复杂度的解法吗？
#  Related Topics 树 深度优先搜索 二叉搜索树 动态规划 二叉树 👍 118 👎 0

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 1

        def rec(node):
            if not node.left and not node.right:
                return node.val, node.val, 1
            if not node.left:
                rmin, rmax, rnum = rec(node.right)
                if node.val < rmin:
                    self.res = max(self.res, rnum + 1)
                    return node.val, rmax, rnum + 1
                else:
                    return float('-inf'), float('inf'), 0
            elif not node.right:
                lmin, lmax, lnum = rec(node.left)
                if node.val > lmax:
                    self.res = max(self.res, lnum + 1)
                    return lmin, node.val, lnum + 1
                else:
                    return float('-inf'), float('inf'), 0
            else:
                rmin, rmax, rnum = rec(node.right)
                lmin, lmax, lnum = rec(node.left)
                if rnum != 0 and lnum != 0 and node.val<rmin and node.val>lmax:
                    self.res = max(rnum + lnum + 1, self.res)
                    return lmin, rmax, rnum + lnum + 1
                else:
                    return float('-inf'), float('inf'), 0
        if not root:
            return 0
        rec(root)
        return self.res
from trick.treenode.T import stringToTreeNode
a=stringToTreeNode('[3,1,2]')
Solution().largestBSTSubtree(a)