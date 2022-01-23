#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 设计一个算法，可以将 N 叉树编码为二叉树，并能将该二叉树解码为原 N 叉树。一个 N 叉树是指每个节点都有不超过 N 个孩子节点的有根树。类似地，一个二叉
# 树是指每个节点都有不超过 2 个孩子节点的有根树。你的编码 / 解码的算法的实现没有限制，你只需要保证一个 N 叉树可以编码为二叉树且该二叉树可以解码回原始 N
#  叉树即可。
#
#  例如，你可以将下面的 3-叉 树以该种方式编码：
#
#
#
#
#
#
#
#  注意，上面的方法仅仅是一个例子，可能可行也可能不可行。你没有必要遵循这种形式转化，你可以自己创造和实现不同的方法。
#
#  注意：
#
#
#  N 的范围在 [1, 1000]
#  不要使用类成员 / 全局变量 / 静态变量来存储状态。你的编码和解码算法应是无状态的。
#
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 二叉树
#  👍 48 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        if not root:
            return None
        rootNode = TreeNode(root.val)
        if root.children:
            first = root.children[0]
            rootNode.left = self.encode(first)
        curr = rootNode.left
        for nxt in root.children[1:]:
            curr.right = self.encode(nxt)
            curr = curr.right
        return rootNode

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        if not data:
            return None
        node = Node(data.val, [])
        curr = data.left
        while curr:
            node.children.append(self.decode(curr))
            curr = curr.right
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
# leetcode submit region end(Prohibit modification and deletion)
