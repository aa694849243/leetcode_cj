'''您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[root.val]
        tree=[root]
        while True:
            tree_=[]
            m=[]
            for node in tree:
                if node.left:
                    tree_.append(node.left)
                    m.append(node.left.val)
                if node.right:
                    tree_.append(node.right)
                    m.append(node.right.val)
            if not tree_:
                break
            res.append(max(m))
            tree=tree_
        return res


