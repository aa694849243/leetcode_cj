'''
给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。
示例 1:

输入:
    2
   / \
  1   3
输出: true
示例 2:

输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
from leetcode.trick.treenode.T import stringToTreeNode

#caojie 递归 6%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def rec(root):
            trees = []
            if not root:
                return []
            trees.append(root.val)
            trees.extend(rec(root.left))
            trees.extend(rec(root.right))
            return trees

        def ans(root):
            if not root:
                return True
            for i in rec(root.right):
                if i <= root.val:
                    return False
            r2 = ans(root.right)
            for i in rec(root.left):
                if i >= root.val:
                    return False
            r1 = ans(root.left)
            return r1 and r2

        return ans(root)
#中序遍历 二叉搜索树中序遍历一定是升序的
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True


# 作者：LeetCode - Solution
# 链接：https: // leetcode - cn.com / problems / validate - binary - search - tree / solution / yan - zheng - er - cha - sou - suo - shu - by - leetcode - solution /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


a = stringToTreeNode('[10,5,15,null,null,6,20]')
Solution().isValidBST(a)
