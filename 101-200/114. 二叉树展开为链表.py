'''
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        H = root
        while root:
            root.left, root.right = root.right, root.left
            pred = root
            while pred.right:
                pred = pred.right
            pred.right = root.left
            root.left=None
            root = root.right
        return H
#未按题目要求做
#精妙递归 lambda递归  lambda表达式递归
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        a = lambda root: [] if not root else [root.val]+a(root.left)+a(root.right)
        TL = lambda lst: TreeNode(lst[0], None, TL(lst[1:])) if lst else None
        tmp = a(root)
        root.left = None
        root.right = TL(tmp[1:])

# 作者：ting-ting-28
# 链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/solution/python3-di-gui-by-ting-ting-28/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。