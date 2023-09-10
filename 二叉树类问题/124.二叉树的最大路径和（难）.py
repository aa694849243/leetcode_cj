# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxscore = float('-inf')

        def f(node):
            if not node:
                return 0
            left = max(f(node.left), 0)
            right = max(f(node.right), 0)
            self.maxscore = max(self.maxscore, left + right + node.val)
            return max(left, right) + node.val
        f(root)
        return self.maxscore
# leetcode submit region end(Prohibit modification and deletion)
