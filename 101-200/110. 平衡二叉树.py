'''
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 递归 caojie 99%
class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: TreeNode) -> bool:
        def height(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 1
            elif not root.right:
                a = height(root.left)
                if a > 1:
                    self.ans = False
                return 1 + a
            elif not root.left:
                a = height(root.right)
                if a > 1:
                    self.ans = False
                return 1 + a
            else:
                a, b = height(root.left), height(root.right)
                if abs(a - b) > 1:
                    self.ans = False
                return 1 + max(a, b)

        height(root)
        return self.ans
# 自底向上和自顶向下区别
# https://leetcode-cn.com/problems/balanced-binary-tree/solution/ping-heng-er-cha-shu-by-leetcode/
