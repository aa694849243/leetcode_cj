'''
给出一个完全二叉树，求出该树的节点个数。

说明：

完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

示例:

输入:
    1
   / \
  2   3
 / \  /
4  5 6

输出: 6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-complete-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        que = deque()
        que.append(root)
        count = 0
        while que:
            a = que.popleft()
            if a:
                que.append(a.left)
                que.append(a.right)
                count += 1
        return count


# 二分法 二分查找
from leetcode.trick.treenode.T import stringToTreeNode
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def depth(root):
            d = -1
            while root:
                d += 1
                root = root.left
            return d

        def exist(idx, root, d):
            left, right = 0, 2 ** d - 1
            for _ in range(d):
                pivot = (left + right) // 2
                if idx <= pivot:
                    root = root.left
                    right = pivot
                else:
                    root = root.right
                    left = pivot
            return root is not None

        d = depth(root)
        if d == -1:
            return 0
        elif d == 0:
            return 1
        left, right = 0, 2 ** d - 1
        while left<=right:
            pivot = (left + right) // 2
            if exist(pivot, root, d):
                left = pivot+1
            else:
                right = pivot-1
        return 2 ** d - 1 + left
a='[1,2,3]'
b=stringToTreeNode(a)
Solution().countNodes(b)