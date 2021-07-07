# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一棵二叉树的根节点 root ，请你返回 层数最深的叶子节点的和 。
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# 输出：15
#
#
#  示例 2：
#
#
# 输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# 输出：19
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [1, 104] 之间。
#  1 <= Node.val <= 100
#
#  Related Topics 树 深度优先搜索 广度优先搜索 Binary Tree
#  👍 58 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        t=[root]
        ans=0
        while True:
            tree=[]
            for node in t:
                ans+=node.val
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            if not tree:
                break
            ans=0
            t=tree
        return ans
from leetcode.trick.treenode.T import stringToTreeNode
a=stringToTreeNode('[1,2,3,4,5,null,6,7,null,null,null,null,8]')
Solution().deepestLeavesSum(a)