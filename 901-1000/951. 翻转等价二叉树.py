import collections, heapq, itertools
from typing import List


# 我们可以为二叉树 T 定义一个翻转操作，如下所示：选择任意节点，然后交换它的左子树和右子树。
#
#  只要经过一定次数的翻转操作后，能使 X 等于 Y，我们就称二叉树 X 翻转等价于二叉树 Y。
#
#  编写一个判断两个二叉树是否是翻转等价的函数。这些树由根节点 root1 和 root2 给出。
#
#
#
#  示例：
#
#  输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,n
# ull,null,null,8,7]
# 输出：true
# 解释：我们翻转值为 1，3 以及 5 的三个节点。
#
#
#
#
#
#  提示：
#
#
#  每棵树最多有 100 个节点。
#  每棵树中的每个值都是唯一的、在 [0, 99] 范围内的整数。
#
#
#
#  Related Topics 树
#  👍 90 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node1, node2: TreeNode):
            if not node1 or not node2:
                return not node1 and not node2
            if node1.val == node2.val:
                al = node1.left
                ar = node1.right
                bl = node2.left
                br = node2.right
                return dfs(al,bl) and dfs(ar,br) or dfs(ar,bl) and dfs(al,br)
            return False
        return dfs(root1,root2)
