'''给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 二叉搜索树的特性
# 本题需要注意：递归到节点本身时，本身是无法自己删除本身的，如果设置node=None则会新建一个None的节点，其本身不会变化
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def successor(node):
            node = node.right
            while node.left:
                node = node.left
            return node.val

        def predecessor(node):
            node = node.left
            while node.right:
                node = node.right
            return node.val

        def delete(node, key):
            if not node:
                return None
            if node.val == key:
                if not node.left and not node.right:
                    node = None
                elif node.right:
                    node.val = successor(node)
                    node.right = delete(node.right, node.val)
                elif node.left:
                    node.val = predecessor(node)
                    node.left = delete(node.left, node.val)
            elif node.val > key:
                node.left = delete(node.left, key)
            elif node.val < key:
                node.right = delete(node.right, key)
            return node
        root=delete(root,key)
        return root


from leetcode.trick.treenode.T import stringToTreeNode

a = '[2,1]'
root = stringToTreeNode(a)
key = 0
Solution().deleteNode(root, 2)
