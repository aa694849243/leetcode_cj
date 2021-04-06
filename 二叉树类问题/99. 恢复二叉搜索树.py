'''
二叉搜索树中的两个节点被错误地交换。

请在不改变其结构的情况下，恢复这棵树。

示例 1:

输入: [1,3,null,null,2]

   1
  /
 3
  \
   2

输出: [3,1,null,null,2]

   3
  /
 1
  \
   2
示例 2:

输入: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

输出: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
进阶:

使用 O(n) 空间复杂度的解法很容易实现。
你能想出一个只使用常数空间的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from leetcode.trick.treenode.T import stringToTreeNode


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def inorder(root):
            stack = []
            ans = TreeNode(float('-inf'))
            flag = -1
            res = TreeNode(0)
            while stack or root:
                while root:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                if root.val > ans.val and flag == -1:  # 如果不存在逆序值，则正常扫描
                    ans = root
                elif root.val < ans.val and flag == -1:  # 如果逆序了，用res保存逆序数前一个节点，并做好标记，之后去找最低值
                    flag = 1
                    res = ans
                    ans = root
                elif root.val < ans.val and flag == 1:  # 找保存的节点之后的最低值
                    ans = root
                root = root.right
            res.val, ans.val = ans.val, res.val  # 交换值

        inorder(root)


# morris遍历，空间复杂度为1
#如果cur无左孩子，cur向右移动（cur=cur.right）
# 如果cur有左孩子，找到cur左子树上最右的节点，记为mostright
# 如果mostright的right指针指向空，让其指向cur，cur向左移动（cur=cur.left）
# 如果mostright的right指针指向cur，让其指向空，cur向右移动（cur=cur.right）

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # predecessor is a Morris predecessor.
        # In the 'loop' cases it could be equal to the node itself predecessor == root.
        # pred is a 'true' predecessor,
        # the previous node in the inorder traversal.
        x = y = predecessor = pred = None

        while root:
            # If there is a left child
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step left
                # and then right till you can.
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right

                # set link predecessor.right = root
                # and go to explore left subtree
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                # break link predecessor.right = root
                # link is broken : time to change subtree and go right
                else:
                    # check for the swapped nodes
                    if pred and root.val < pred.val:
                        y = root
                        if x is None:
                            x = pred
                    pred = root

                    predecessor.right = None
                    root = root.right
            # If there is no left child
            # then just go right.
            else:
                # check for the swapped nodes
                if pred and root.val < pred.val:
                    y = root
                    if x is None:
                        x = pred
                pred = root

                root = root.right

        x.val, y.val = y.val, x.val


# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / recover - binary - search - tree / solution / hui - fu - er - cha - sou - suo - shu - by - leetcode /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


a = stringToTreeNode('[146,71,-13,55,null,231,399,321,null,null,null,null,null,-33]')
Solution().recoverTree(a)
