# 返回与给定的前序和后序遍历匹配的任何二叉树。
#
#  pre 和 post 遍历中的值是不同的正整数。
#
#
#
#  示例：
#
#  输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#
#
#
#
#  提示：
#
#
#  1 <= pre.length == post.length <= 30
#  pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
#  每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。
#
#  Related Topics 树
#  👍 158 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# 保留索引的方法
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        def make(l, r, n):
            if n == 0:
                return None
            if n == 1:
                return TreeNode(pre[l])
            root = TreeNode(pre[l])
            for i in range(n - 1):
                if pre[l + 1] == post[r + i]:
                    break
            nxtn = i + 1
            root.left = make(l + 1, r, nxtn)
            root.right = make(l + 1 + nxtn, r + i + 1, n - nxtn - 1)
            return root

        return make(0, 0, len(pre))


# 2不保留索引，直接用列表递归，空间复杂度更高
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root
        l = post.index(pre[1])+1
        root.left=self.constructFromPrePost(pre[1:l+1],post[:l])
        root.right=self.constructFromPrePost(pre[l+1:],post[l:-1])
        return root

