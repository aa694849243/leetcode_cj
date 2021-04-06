'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]



 

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from leetcode.trick.treenode.T import stringToTreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def check(ancestor, node):
            if ancestor:
                if ancestor.left and ancestor.left.val == node.val:
                    return ancestor
                elif ancestor.right and ancestor.right.val == node.val:
                    return ancestor
                else:
                    a = check(ancestor.left, node)
                    b = check(ancestor.right, node)
                    return a if a else b

        while p != q and p != root and q != root:
            if check(p, q):
                return p
            elif check(q, p):
                return q
            p = check(root, p)
            q = check(root, q)
        return root if p == root or q == root else p


# 哈希法 哈希表法
'''
从根节点开始遍历整棵二叉树，用哈希表记录每个节点的父节点指针。
从 p 节点开始不断往它的祖先移动，并用数据结构记录已经访问过的祖先节点。
同样，我们再从 q 节点开始不断往它的祖先移动，如果有祖先已经被访问过，即意味着这是 p 和 q 的深度最深的公共祖先，即 LCA 节点。
'''


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        s = {}
        st = []
        node = root
        s[root.val]=None
        while node or st:
            while node:
                st.append(node.right)
                if node.left:
                    s[node.left.val] = node
                if node.right:
                    s[node.right.val] = node
                node = node.left
            node = st.pop()
        m =set()
        while p:
            m.add(p)
            p = s[p.val]
        while q not in m:
            q=s[q.val]

        return q


root = stringToTreeNode('[3,5,1,6,2,0,8,null,null,7,4]')
p = 5;
q = 4
Solution().lowestCommonAncestor(root, TreeNode(p), TreeNode(q))
