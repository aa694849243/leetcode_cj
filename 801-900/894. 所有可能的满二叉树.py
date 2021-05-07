# 满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。
#
#  返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。
#
#  答案中每个树的每个结点都必须有 node.val=0。
#
#  你可以按任何顺序返回树的最终列表。
#
#
#
#  示例：
#
#  输入：7
# 输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0
# ,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
# 解释：
#
#
#
#
#
#  提示：
#
#
#  1 <= N <= 20
#
#  Related Topics 树 递归
#  👍 195 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def __init__(self):
        self.m = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n not in self.m:
            ans = []
            for L in range(n):
                R = n - 1 - L
                for l in self.allPossibleFBT(L):
                    for r in self.allPossibleFBT(R):
                        node = TreeNode(0)
                        node.left = l
                        node.right = r
                        ans.append(node)
            self.m[n] = ans

        return self.m[n]


# 2 利用生成器
class Solution:

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        m = {0: [], 1: [TreeNode(0)]}

        def solve(num):
            if num in m:
                yield from m[num]
            else:
                ans = []
                for L in range(num):
                    R = num - 1 - L
                    for l in solve(L):
                        for r in solve(R):
                            node = TreeNode(0)
                            node.left = l
                            node.right = r
                            ans.append(node)
                m[num] = ans
                yield from m[num]

        return list(solve(n))


Solution().allPossibleFBT(5)
