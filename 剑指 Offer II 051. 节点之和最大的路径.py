# -*- coding: utf-8 -*-
# author： caoji
# datetime： 2023-02-08 23:06 
# ide： PyCharm
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -math.inf

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.ans = max(self.ans, left + right + node.val, node.val)
            return max(left, right) + node.val

        dfs(root)
        return self.ans
# leetcode submit region end(Prohibit modification and deletion)

