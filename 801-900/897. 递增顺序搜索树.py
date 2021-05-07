# 给你一棵二叉搜索树，请你 按中序遍历 将其重新排列为一棵递增顺序搜索树，使树中最左边的节点成为树的根节点，并且每个节点没有左子节点，只有一个右子节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
#
#
#  示例 2：
#
#
# 输入：root = [5,1,7]
# 输出：[1,null,5,null,7]
#
#
#
#
#  提示：
#
#
#  树中节点数的取值范围是 [1, 100]
#  0 <= Node.val <= 1000
#
#  Related Topics 树 深度优先搜索 递归
#  👍 219 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.dummynode = TreeNode(-1)
        self.resnode = self.dummynode
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.resnode.right = node
            self.resnode = node
            node.left=None
            inorder(node.right)
        inorder(root)
        return self.dummynode.right
from leetcode.trick.treenode.T import stringToTreeNode
from leetcode.trick.treenode.T import treeNodeToString

a = stringToTreeNode('[4,1,7,0,2,5,8,null,null,null,3,null,6,null,9]')
b = Solution().increasingBST(a)
treeNodeToString(b)
