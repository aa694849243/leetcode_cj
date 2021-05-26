import collections, heapq, itertools
from typing import List


# 给定一个二叉树，确定它是否是一个完全二叉树。
#
#  百度百科中对完全二叉树的定义如下：
#
#  若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：
# 第 h 层可能包含 1~ 2h 个节点。）
#
#
#
#  示例 1：
#
#
#
#  输入：[1,2,3,4,5,6]
# 输出：true
# 解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
#
#
#  示例 2：
#
#
#
#  输入：[1,2,3,4,5,null,7]
# 输出：false
# 解释：值为 7 的结点没有尽可能靠向左侧。
#
#
#
#
#  提示：
#
#
#  树中将会有 1 到 100 个结点。
#
#  Related Topics 树
#  👍 123 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        t = [(root, False)]
        status = False
        while True:
            tree = []
            for node, st in t:
                if node:
                    if status:
                        return False
                    if node.left and node.right:
                        tree.extend([(node.left, False), (node.right, False)])
                    elif node.left:
                        tree.append((node.left, True))
                    elif node.right:
                        return False
                    else:
                        tree.append((None, True))
                if st:
                    status = True
            if not tree:
                break
            t = tree
        return True


from learn.leetcode.trick.treenode.T import stringToTreeNode


# 完全二叉树是没有间隙的
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        t = collections.deque([(root, 1)])
        cnt = 0
        while t:
            node, i = t.popleft()
            cnt += 1
            if node.left:
                t.append((node.left, 2 * i))
            if node.right:
                t.append((node.right, 2 * i + 1))
        return cnt == i


a = stringToTreeNode('[1,2,3,4,5,6,7,8,9,10,11,12,13,null,null,15]')
Solution().isCompleteTree(a)
