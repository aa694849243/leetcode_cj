'''给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def rec(node1, node2):
            if not node1:
                return not node2
            if not node2:
                return not node1
            if node1.val == node2.val:
                if check(node1.left, node2.left) and check(node1.right, node2.right):
                    return True
            if rec(node1.left, node2):
                return True
            if rec(node1.right, node2):
                return True
            return False

        def check(node1, node2):
            if not node1:
                return not node2
            if not node2:
                return not node1
            if node1.val != node2.val:
                return False
            if check(node1.left,node2.left) and check(node1.right,node2.right):
                return True
            return False
        return rec(s, t)


from leetcode.trick.treenode.T import stringToTreeNode

s = stringToTreeNode('[3,4,5,1,null,2]')
t = stringToTreeNode('[3,1,2]')
Solution().isSubtree(s, t)
