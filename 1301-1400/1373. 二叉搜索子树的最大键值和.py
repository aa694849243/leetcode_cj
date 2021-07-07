# -*- coding: utf-8 -*-
import collections


# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
#
#  二叉搜索树的定义如下：
#
#
#  任意节点的左子树中的键值都 小于 此节点的键值。
#  任意节点的右子树中的键值都 大于 此节点的键值。
#  任意节点的左子树和右子树都是二叉搜索树。
#
#
#
#
#  示例 1：
#
#
#
#
# 输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。
#
#
#  示例 2：
#
#
#
#
# 输入：root = [4,3,null,1,2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。
#
#
#  示例 3：
#
#
# 输入：root = [-4,-2,-5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。
#
#
#  示例 4：
#
#
# 输入：root = [2,1,3]
# 输出：6
#
#
#  示例 5：
#
#
# 输入：root = [5,4,8,3,null,6,3]
# 输出：7
#
#
#
#
#  提示：
#
#
#  每棵树有 1 到 40000 个节点。
#  每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
#
#  Related Topics 树 深度优先搜索 二叉搜索树 动态规划 二叉树
#  👍 50 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        m = collections.defaultdict(lambda: float('-inf'))
        mi = collections.defaultdict(lambda: float('inf'))
        s = collections.defaultdict(lambda: float('-inf'))

        def dfs(node):
            if not node:
                return 0, float('-inf'), float('inf')
            sl, ml, mil = dfs(node.left)
            sr, mr, mir = dfs(node.right)
            m[node] = max(node.val, ml, mr)
            mi[node] = min(node.val, mil, mir)
            s[node] = node.val + sl + sr
            return s[node], m[node], mi[node]

        dfs(root)
        self.ans = 0

        def judge(node):
            if not node:
                return True
            l, r = node.left, node.right
            a = judge(l)
            b = judge(r)
            if a and b:
                if l:
                    if node.val <= m[l]:  # 大于左子树的最大值
                        return False
                if r:
                    if node.val >= mi[r]:  # 小于右子树的最小值
                        return False
                self.ans = max(self.ans, s[node])
                return True
            return False

        judge(root)
        return self.ans



from leetcode.trick.treenode.T import stringToTreeNode

a = stringToTreeNode(' [1,null,10,-5,20]')
Solution().maxSumBST(a)
