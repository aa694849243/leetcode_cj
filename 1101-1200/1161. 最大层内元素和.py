# -*- coding: utf-8 -*-
# 给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。
#
#  请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。
#
#
#
#  示例 1：
#
#
#
#  输入：root = [1,7,0,7,-8,null,null]
# 输出：2
# 解释：
# 第 1 层各元素之和为 1，
# 第 2 层各元素之和为 7 + 0 = 7，
# 第 3 层各元素之和为 7 + -8 = -1，
# 所以我们返回第 2 层的层号，它的层内元素之和最大。
#
#
#  示例 2：
#
#  输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
# 输出：2
#
#
#
#
#  提示：
#
#
#  树中的节点数介于 1 和 10^4 之间
#  -10^5 <= node.val <= 10^5
#
#  Related Topics 树 广度优先搜索
#  👍 44 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        t = [root]
        ans = 1
        maxsum = float('-inf')
        step = 1
        while True:
            tree = []
            f = 0
            for node in t:
                f += node.val
                if node.left:
                    tree.append(node.left)
                if node.right:
                    tree.append(node.right)
            if f > maxsum:
                ans = step
                maxsum = f
            step += 1
            if not tree:
                break
            t = tree
        return ans


from leetcode.trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[1,7,0,7,-8,null,null]')
Solution().maxLevelSum(a)
