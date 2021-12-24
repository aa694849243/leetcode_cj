# -*- coding: utf-8 -*-
from typing import List
import collections
import functools
import itertools
import sortedcontainers
import bisect


# 给你一个二叉树的根结点，返回其结点按 垂直方向（从上到下，逐列）遍历的结果。
#
#  如果两个结点在同一行和列，那么顺序则为 从左到右。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[9],[3,15],[20],[7]]
#
#
#  示例 2：
#
#
# 输入：root = [3,9,8,4,0,1,7]
# 输出：[[4],[9],[3,0,1],[8],[7]]
#
#
#  示例 3：
#
#
# 输入：root = [3,9,8,4,0,1,7,null,null,null,2,5]
# 输出：[[4],[9,5],[3,0,1],[8,2],[7]]
#
#
#  示例 4：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中结点的数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#  Related Topics 树 深度优先搜索 广度优先搜索 哈希表 二叉树 👍 140 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        t = [(root, 0, 0, 0)]
        res = [(root, 0, 0, 0)]
        step = 0
        while 1:
            tree = []
            cur = 0
            step += 1
            for node, loc, x, y in t:
                if node.left:
                    tree.append((node.left, loc - 1, cur, step))
                    cur += 1
                if node.right:
                    tree.append((node.right, loc + 1, cur, step))
                    cur += 1
            if not tree:
                break
            res.extend(tree)
            t = tree
        res.sort(key=lambda x: [x[1], x[3], x[2]])
        ans = []
        tmp = []
        flag = float('-inf')
        for node, loc, x, y in res:
            if loc != flag:
                ans.append(tmp)
                flag = loc
                tmp = [node.val]
            else:
                tmp.append(node.val)
        ans.append(tmp)
        ans.pop(0)
        return ans


from trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[3,9,8,4,0,1,7,null,null,null,2,5]')
Solution().verticalOrder(a)
