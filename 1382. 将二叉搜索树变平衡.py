# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
#
#  如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
#
#  如果有多种构造方法，请你返回任意一种。
#
#
#
#  示例：
#
#
#
#  输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
#
#
#
#
#  提示：
#
#
#  树节点的数目在 1 到 10^4 之间。
#  树节点的值互不相同，且在 1 到 10^5 之间。
#
#  Related Topics 贪心 树 深度优先搜索 二叉搜索树 分治 二叉树
#  👍 66 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        li=[]
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            li.append(node.val)
            inorder(node.right)
        inorder(root)
        def build(l,r):
            if l>=r:
                return None
            mid=(l+r)//2
            node=TreeNode(li[mid])
            node.left=build(l,mid)
            node.right=build(mid+1,r)
            return node
        return build(0,len(li))
