'''
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from leetcode.trick.treenode.T import stringToTreeNode


class Solution:
    def __init__(self):
        self.count = 0
        self.k = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return
        ans = []
        self.k = k

        def rec(root):
            if root:
                rec(root.left)
                if self.count < self.k:
                    ans.append(root.val)
                    self.count += 1
                rec(root.right)

        rec(root)
        return ans[-1]


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        count = 0
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            node = node.right
        return


# 递归 简洁 中序遍历
class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]


# 作者：LeetCode
# 链接：https: // leetcode - cn.com / problems / kth - smallest - element - in -a - bst / solution / er - cha - sou - suo - shu - zhong - di - kxiao - de - yuan - su - by - le /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
a = stringToTreeNode('[3,1,4,null,2]')
Solution().kthSmallest(a, 1)
