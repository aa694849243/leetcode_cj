'''给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。

假定 BST 有如下定义：

结点左子树中所含结点的值小于等于当前结点的值
结点右子树中所含结点的值大于等于当前结点的值
左子树和右子树都是二叉搜索树
例如：
给定 BST [1,null,2,2],

   1
    \
     2
    /
   2
返回[2].

提示：如果众数超过1个，不需考虑输出顺序

进阶：你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-mode-in-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


class Solution:
    def __init__(self):
        self.maxcnt = 0
        self.cnt = 1
        self.prev='#'
        self.res = []

    def findMode(self, root: TreeNode) -> List[int]:

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            if root.val == self.prev:
                self.cnt += 1
            else:
                self.cnt = 1
                self.prev=root.val
            if self.cnt == self.maxcnt:
                self.res.append(root.val)
            elif self.cnt > self.maxcnt:
                self.maxcnt = self.cnt
                self.res = [root.val]
            in_order(root.right)
            return root.val

        in_order(root)
        return self.res


from leetcode.trick.treenode.T import stringToTreeNode

s = stringToTreeNode('[1,null,2,2,3,null,null,null,3,null,3]')
Solution().findMode(s)
