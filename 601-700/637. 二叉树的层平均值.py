'''给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from typing import List

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        m=[root]
        ans=[root.val]
        while True:
            tree=[]
            s=0
            for node in m:
                if node.left:
                    tree.append(node.left)
                    s+=node.left.val
                if node.right:
                    tree.append(node.right)
                    s+=node.right.val
            if not tree:
                break
            ans.append(s/len(tree))
            m=tree
        return ans
from leetcode.trick.treenode.T import stringToTreeNode
a=stringToTreeNode('[3,9,20,15,7]')
Solution().averageOfLevels(a)