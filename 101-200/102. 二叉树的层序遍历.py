'''
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。

 

示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List
from collections import deque
from leetcode.trick.treenode.T import stringToTreeNode


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        deq = [[root]]
        res = []
        while deq:
            trees = []
            ans = []
            for root in deq.pop():
                if not root:
                    continue
                trees.append(root.left)
                trees.append(root.right)
                ans.append(root.val)
            if not trees:
                break
            deq.append(trees)
            res.append(ans)
        return res


a = stringToTreeNode('[3,9,20,null,null,15,7]')
Solution().levelOrder(a)
