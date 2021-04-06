'''给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-univalue-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    ans = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def rec(node):
            if not node:
                return 0
            l_length = rec(node.left)
            r_length = rec(node.right)
            a = b = 0
            if node.left and node.left.val == node.val:
                a = l_length + 1
            if node.right and node.right.val == node.val:
                b = r_length + 1
            self.ans = max(a + b, self.ans)
            return max(a,b)

        rec(root)
        return self.ans
