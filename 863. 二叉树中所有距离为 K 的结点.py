# 给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。
#
#  返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。
#
#
#
#
#
#
#  示例 1：
#
#  输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 输出：[7,4,1]
# 解释：
# 所求结点为与目标结点（值为 5）距离为 2 的结点，
# 值分别为 7，4，以及 1
#
#
#
# 注意，输入的 "root" 和 "target" 实际上是树上的结点。
# 上面的输入仅仅是对这些对象进行了序列化描述。
#
#
#
#
#  提示：
#
#
#  给定的树是非空的。
#  树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
#  目标结点 target 是树上的结点。
#  0 <= K <= 1000.
#
#  Related Topics 树 深度优先搜索 广度优先搜索
#  👍 273 👎 0

from typing import List


# 二叉树路径 二叉树距离
# 1 添加父节点
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def add_par(node, par=None):
            node.par = par
            if node.left:
                add_par(node.left, node)
            if node.right:
                add_par(node.right, node)

        add_par(root)
        q = collections.deque([(target, 0)])
        seen = {target}
        while q:
            if q[0][1] == K:
                return [a.val for a, dist in q]
            node, dist = q.popleft()
            for nei in (node.left, node.right, node):
                if nei and nei not in seen:
                    seen.add(nei)
                    q.append((nei, dist + 1))
        return []


# 2计算距离
# 定义两个函数，主函数dfs找某节点左右子树里是否有目标节点，如果有，返回距离，并在另一子树里通过add_subtree找到距离符合的节点
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        ans = []

        def add_subtree(node, dist):
            if not node:
                return
            if dist == K:
                ans.append(node.val)
            else:
                add_subtree(node.left, dist + 1)
                add_subtree(node.right, dist + 1)

        def dfs(node):
            if not node:
                return -1
            if node.val == target.val:
                add_subtree(node, 0)
                return 1
            l, r = dfs(node.left), dfs(node.right)
            if l != -1:
                if l == K:
                    ans.append(node.val)
                add_subtree(node.right, l + 1)
                return l + 1
            elif r != -1:
                if r == K:
                    ans.append(node.val)
                add_subtree(node.left, r + 1)
                return r + 1
            else:
                return -1

        dfs(root)
        return ans


from leetcode.trick.treenode.T import stringToTreeNode

Solution().distanceK()
