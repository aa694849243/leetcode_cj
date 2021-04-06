'''给定一棵二叉树，返回所有重复的子树。对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

两棵树重复是指它们具有相同的结构以及相同的结点值。

示例 1：

        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
下面是两个重复的子树：

      2
     /
    4
和

    4
因此，你需要以列表的形式返回上述重复子树的根结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-duplicate-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1深度优先遍历 序列化
import collections


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        m = collections.defaultdict(int)
        ans = []

        def dfs(node):
            if not node:
                return '#'
            serial = '{},{},{}'.format(node.val, dfs(node.left), dfs(node.right))
            m[serial] += 1
            if m[serial] == 2:
                ans.append(node)
            return serial

        dfs(root)
        return ans


# 2标识符
# default_factory
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        ans = []
        m = collections.Counter()

        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left), lookup(node.right)]
                m[uid] += 1
                if m[uid] == 2:
                    ans.append(node)
                return uid
        lookup(root)
        return ans


from leetcode.trick.treenode.T import stringToTreeNode

a = stringToTreeNode('[1,2,3,4,null,2,4,null,null,4]')
Solution().findDuplicateSubtrees(a)
