'''
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        deq = [[root]]
        res = []
        flag = 1
        while deq:
            ans = []
            trees = []
            for i in deq.pop():
                if not i:
                    continue
                ans.append(i.val)
                trees.append(i.left)
                trees.append(i.right)
            if not trees:
                break
            if flag == 1:
                res.append(ans)
                flag = 2
            else:
                res.append(ans[::-1])
                flag=1
            deq.append(trees)
        return res
