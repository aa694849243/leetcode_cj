# -*- coding: utf-8 -*-
from typing import List


# 返回与给定前序遍历 preorder 相匹配的二叉搜索树（binary search tree）的根结点。
#
#  (回想一下，二叉搜索树是二叉树的一种，其每个节点都满足以下规则，对于 node.left 的任何后代，值总 < node.val，而 node.right
#  的任何后代，值总 > node.val。此外，前序遍历首先显示节点 node 的值，然后遍历 node.left，接着遍历 node.right。）
#
#  题目保证，对于给定的测试用例，总能找到满足要求的二叉搜索树。
#
#
#
#  示例：
#
#  输入：[8,5,1,7,10,12]
# 输出：[8,5,10,1,7,null,12]
#
#
#
#
#
#  提示：
#
#
#  1 <= preorder.length <= 100
#  1 <= preorder[i] <= 10^8
#  preorder 中的值互不相同
#
#  Related Topics 树
#  👍 147 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(nums):
            if not nums:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])
            flag = nums[0]
            for i in range(1, len(nums)):
                if nums[i] > flag:
                    break
            node = TreeNode(nums[0])
            if nums[i] > flag:
                node.left = dfs(nums[1:i])
                node.right = dfs(nums[i:])
            else:
                node.left = dfs(nums[1:])
            return node
        return dfs(preorder)
