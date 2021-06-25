# -*- coding: utf-8 -*-
import collections, heapq, itertools, bisect
from typing import List
# 给你 root1 和 root2 这两棵二叉搜索树。
#
#  请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.
#
#
#
#  示例 1：
#
#
#
#  输入：root1 = [2,1,4], root2 = [1,0,3]
# 输出：[0,1,1,2,3,4]
#
#
#  示例 2：
#
#  输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
# 输出：[-10,0,0,1,2,5,7,10]
#
#
#  示例 3：
#
#  输入：root1 = [], root2 = [5,1,7,0,2]
# 输出：[0,1,2,5,7]
#
#
#  示例 4：
#
#  输入：root1 = [0,-10,10], root2 = []
# 输出：[-10,0,10]
#
#
#  示例 5：
#
#
#
#  输入：root1 = [1,null,8], root2 = [8,1]
# 输出：[1,1,8,8]
#
#
#
#
#  提示：
#
#
#  每棵树最多有 5000 个节点。
#  每个节点的值在 [-10^5, 10^5] 之间。
#
#  Related Topics 树 深度优先搜索 二叉搜索树 Binary Tree Sorting
#  👍 59 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node,li):
            if not node:
                return
            dfs(node.left,li)
            li.append(node.val)
            dfs(node.right,li)
        v1,v2=[],[]
        dfs(root1,v1)
        dfs(root2,v2)
        l,r=0,0
        ans=[]
        while l<len(v1) or r<len(v2):
            if l<len(v1) and (r==len(v2) or v1[l]<=v2[r]):
                ans.append(v1[l])
                l+=1
            else:
                ans.append(v2[r])
                r+=1
        return ans