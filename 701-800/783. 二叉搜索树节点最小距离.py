'''给定一个二叉搜索树的根节点 root，返回树中任意两节点的差的最小值。

 

示例：

输入: root = [4,2,6,1,3,null,null]
输出: 1
解释:
注意，root是树节点对象(TreeNode object)，而不是数组。

给定的树 [4,2,6,1,3,null,null] 可表示为下图:

          4
        /   \
      2      6
     / \
    1   3

最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
 

注意：

二叉树的大小范围在 2 到 100。
二叉树总是有效的，每个节点的值都是整数，且不重复。
本题与 530：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/ 相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        def rec_l(node):
            if not node.left:
                return node.val
            return rec_l(node.left)

        def rec_r(node):
            if not node.right:
                return node.val
            return rec_r(node.right)

        def rec(node):
            if not node.left and not node.right:
                return
            if not node.left:
                self.ans = min(self.ans, rec_l(node.right)-node.val)
                rec(node.right)
            elif not node.right:
                self.ans = min(self.ans, node.val- rec_r(node.left))
                rec(node.left)
            else:
                self.ans = min(self.ans, rec_l(node.right)-node.val, node.val-rec_r(node.left))
                rec(node.left)
                rec(node.right)
        rec(root)
        return self.ans

