'''
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List


# caojie 30%
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        stack = [root]
        res = []
        while True:
            trees = []
            ans = []
            for node in stack:
                if not node:
                    continue
                ans.append(node.val)
                trees.append(node.left)
                trees.append(node.right)
            if not trees:
                break
            stack = trees
            res.append(ans)
        res.reverse()
        return res


# 以队列实现
class Solution:
    def levelOrderBottom(self, root):
        queue = []                                                  # 结果列表
        cur = [root]                                                # 接下来要循环的当前层节点，存的是节点
        while cur:                                                  # 当前层存在结点时
            cur_layer_val = []                                      # 初始化当前层结果列表为空，存的是val
            next_layer_node = []                                    # 初始化下一层结点列表为空
            for node in cur:                                        # 遍历当前层的每一个结点
                if node:                                            # 如果该结点不为空，则进行记录
                    cur_layer_val.append(node.val)                  # 将该结点的值加入当前层结果列表的末尾
                    next_layer_node.extend([node.left, node.right]) # 将该结点的左右孩子结点加入到下一层结点列表
            if cur_layer_val:                                       # 只要当前层结果列表不为空
                queue.insert(0, cur_layer_val)                      # 则把当前层结果列表插入到队列首端
            cur = next_layer_node                                   # 下一层的结点变成当前层，接着循环
        return queue

# 作者：yi-xi-4
# 链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/solution/python3-dui-lie-shi-xian-by-yi-xi-4/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
# from leetcode.trick.treenode.T import stringToTreeNode
from leetcode.trick.treenode.T import stringToTreeNode
root = stringToTreeNode('[3,9,20,null,null,15,7]')
Solution().levelOrderBottom(root)
