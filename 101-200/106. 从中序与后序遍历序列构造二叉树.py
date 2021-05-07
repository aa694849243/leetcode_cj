'''
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List

from leetcode.trick.treenode.T import stringToTreeNode


# 递归
# 官方 https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/submissions/
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        index = {val: i for i, val in enumerate(inorder)}

        def mybuild(ileft, iright):
            if iright < ileft:
                return None
            rootval = postorder.pop()
            node = TreeNode(rootval)
            i=index[rootval]
            node.right = mybuild(i+1,iright)
            node.left = mybuild(ileft, i-1)
            return node

        return mybuild(0, len(inorder) - 1)
#存储数量+坐标
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def mybuild(l,r,n):
            if n==0:
                return None
            elif n==1:
                return pre


        return mybuild(0, len(inorder) - 1)
inorder=[9,3,15,20,7]
postorder=[9,15,7,20,3]
Solution().buildTree(inorder, postorder)
