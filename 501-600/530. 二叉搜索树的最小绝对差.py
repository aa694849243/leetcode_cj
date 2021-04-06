'''给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。
本题与 783 https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/ 相同

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.li = []

    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:
            return 2 ** 31 - 1

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.li.append(node.val)
            dfs(node.right)

        dfs(root)
        ans = float('inf')
        if len(self.li) == 1:
            return 2 ** 31 - 1
        for i in range(1, len(self.li)):
            ans = min(ans, self.li[i] - self.li[i - 1])
        return ans


# 2递归
class Solution:
    ans = 2 ** 31 - 1
    pre = 2 ** 31 - 1

    def getMinimumDifference(self, root: TreeNode) -> int:
        def rec(node):
            if not node:
                return
            rec(node.left)
            self.ans = min(abs(self.pre - node.val), self.ans)
            self.pre = node.val
            rec(node.right)

        rec(root)
        return self.ans


from leetcode.trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[236,104,701,null,227,null,911]')
Solution().getMinimumDifference(a)
