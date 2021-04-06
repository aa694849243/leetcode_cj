'''给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。

例如，给定一个 3叉树 :

 



 

返回其层序遍历:

[
     [1],
     [3,2,4],
     [5,6]
]
 

说明:

树的深度不会超过 1000。
树的节点总数不会超过 5000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

#官方 https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/solution/ncha-shu-de-ceng-xu-bian-li-by-leetcode/
from typing import List
# 1广度优先搜索 宽度优先搜索 隔离
import collections


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        tree = collections.deque([root])
        res = []
        while tree:
            n = len(tree)
            l = []
            for _ in range(n):
                a = tree.popleft()
                l.append(a.val)
                tree.extend(a.children)
            res.append(l)
        return res


# 2广度优先搜索 宽度优先搜索不用队列 隔离2

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        pre = [root]
        while pre:
            cur = []
            res.append([])
            for node in pre:
                res[-1].append(node.val)
                cur.extend(node.children)
            pre = cur
        return res


# 3递归广度优先遍历 递归宽度优先遍历
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        result = []

        def rec(nodes, level):
            if not nodes:
                return
            if len(result) == level:
                result.append([])
            for node in nodes:
                m = []
                result[level].append(node.val)
                for c in node.children:
                    m.append(c)
                rec(m, level + 1)

        rec([root], 0)
        return result
def levelOrder(self, root: 'Node') -> List[List[int]]:

    def traverse_node(node, level):
        if len(result) == level:
            result.append([])
        result[level].append(node.val)
        for child in node.children:
            traverse_node(child, level + 1)

    result = []

    if root is not None:
        traverse_node(root, 0)
    return result

# 作者：LeetCode
#链接：https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/solution/ncha-shu-de-ceng-xu-bian-li-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
