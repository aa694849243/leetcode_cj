# -*- coding: utf-8 -*-
import collections


# 请实现两个函数，分别用来序列化和反序列化二叉树。
#
#  你需要设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字
# 符串反序列化为原始的树结构。
#
#  提示：输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方
# 法解决这个问题。
#
#
#
#  示例：
#
#
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
#
#
#
#
#  注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-b
# inary-tree/
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树
#  👍 213 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        inlist = []
        prelist = []
        map = {}
        m = collections.defaultdict(int)

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            m[node.val] += 1
            unqstr = str(node.val) + ';' + str(m[node.val])
            map[node] = unqstr
            inlist.append(unqstr)
            inorder(node.right)

        def preorder(node):
            if not node:
                return
            prelist.append(map[node])
            preorder(node.left)
            preorder(node.right)

        inorder(root)
        preorder(root)
        return ','.join(inlist) + '+' + ','.join(prelist)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        inlist, prelist = data.split('+')
        inlist = inlist.split(',')
        prelist = prelist.split(',')
        index = {upstr: i for i, upstr in enumerate(inlist)}

        def build(pb, pe, ib, ie):
            if pb>pe:
                return None
            val = int(prelist[pb].split(';')[0])
            node = TreeNode(val)
            im = index[prelist[pb]]
            n = im - ib  # 左子树有n个节点
            l = build(pb + 1, pb + n, ib, im - 1)
            r = build(pb + n + 1, pe, im + 1, ie)
            node.left = l
            node.right = r
            return node
        return build(0,len(prelist)-1,0,len(inlist)-1)

from leetcode.trick.treenode.T import stringToTreeNode
a=stringToTreeNode('[1,2,3,null,null,4,5]')
a=Codec().serialize(a)
Codec().deserialize(a)
